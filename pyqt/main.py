# This Python file uses the following encoding: utf-8
import sys, os
import requests
import qdarktheme
import logging

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import Qt, QStringListModel, QThread, QModelIndex, QObject, Signal
from PySide6 import QtGui

from pyimdbmoviefinder.ImdbSearcher import ImdbSearcher
from pyimdbmoviefinder.TorrentSearcher import TorrentSearcher
from pyimdbmoviefinder.TorrentDownloader import TorrentDownloader

from pyqt.app_settings import SettingsHelper, SettingsWindow
from pyqtconfig import QSettings

logger = logging.getLogger('pyqtmoviefinder')

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from .ui.ui_main import Ui_Main

def resource_path(relative_path):
    '''Resource path helper needed for one file pyinstaller executable'''
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("resources/")

    return os.path.join(base_path, relative_path)

class ImdbSearchWorker(QObject):
    '''
    Worker to be ran in a separate Thread because of its execution time
    QSignal 'finished' is emitted on completion with params (byID, input)
    '''
    finished = Signal(bool, str)
    def __init__(self, imdbSearcher:ImdbSearcher, input:str, byID=False, includeTv=False):
        super().__init__()
        self.input = input
        self.byID = byID
        self.imdb = imdbSearcher
        self.includeTv = includeTv
        self.searchResult = []

    def run(self):
        """Long-running task."""
        if self.byID:
            self.imdb.search_by_id(self.input)
        else:
            self.imdb.search_by_title(self.input, includeTv=self.includeTv)
        self.finished.emit(self.byID, self.input)

class TorrentSearchWorker(QObject):
    '''
    Worker to be ran in a separate Thread because of its execution time
    QSignal 'finished' is emitted on completion
    '''
    finished = Signal(str)
    def __init__(self, torrentSearcher:TorrentSearcher, imdbId:str, title:str, yts:bool=True, 
                 jackett:bool=True, jackettApiKey:str='', jackettHost:str=''):
        super().__init__()
        self.imdbId = imdbId
        self.title = title 
        self.tor = torrentSearcher
        torrentSearcher.set_search(imdbId, title, yts, jackett, jackettApiKey, jackettHost)

    def run(self):
        """Long-running task."""
        self.tor.run()
        self.finished.emit(self.imdbId)

class MainWindow(QWidget):
    '''This is the main application window'''
    def __init__(self, settingsWindow:QWidget, settingsObj:QSettings, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.settingsWindow = settingsWindow
        self.settingsObj = settingsObj
        self.currentMovieSelection = None
        self.currentTorrentSelection = None
        self.currentTorrentsResults = None

        imdb_pixmap = QPixmap(resource_path("imdb.png"))
        pixmap_scaled = imdb_pixmap.scaledToHeight(self.ui.ratingImdbLogo.height(), Qt.SmoothTransformation)
        self.ui.ratingImdbLogo.setPixmap(pixmap_scaled)
        self.ui.ratingImdbLogo.hide()
        self.setWindowIcon(QIcon(resource_path("imdb.png")))
        self.ui.torrentSearchButton.setEnabled(False)
        # adding signal and slot
        self.ui.searchImdbButton.clicked.connect(self.searchImdbClicked)
        self.ui.imdbResultListView.clicked.connect(self.imdbListItemClicked)
        self.ui.torrentSearchButton.clicked.connect(self.searchTorrentClicked)
        self.ui.torrentResultListView.clicked.connect(self.torrentListItemClicked)
        self.ui.torrentSendButton.clicked.connect(self.sendTorrentClicked)
        self.ui.settingsButton.clicked.connect(self.settingsWindow.show)
        
        # Object to be used for performing IMDb searches
        self.imdbSearcher = ImdbSearcher()
        # Object to be used for performing torrent searches
        self.torrentSearcher = TorrentSearcher()

        # ListViewModels
        self.imdbResultListModel = QStringListModel()
        self.torrentResultListModel = QStringListModel()
        # Set models to view
        self.ui.imdbResultListView.setModel(self.imdbResultListModel)
        self.ui.torrentResultListView.setModel(self.torrentResultListModel)

        # Hide settings window and connect signal
        self.settingsWindow.hide()
        self.settingsWindow.newSettingsApplied.connect(self.newSettingsApplied)
        
        # Spinner
        palette = qdarktheme.load_palette(theme="light")
        stylesheet = qdarktheme.load_stylesheet(theme="light")
        for spinner in [self.ui.spinnerImdb, self.ui.spinnerTorrent]:
            spinner.setRoundness(70.0)
            spinner.setMinimumTrailOpacity(15.0)
            spinner.setTrailFadePercentage(70.0)
            spinner.setNumberOfLines(12)
            spinner.setLineLength(10)
            spinner.setLineWidth(5)
            spinner.setInnerRadius(10)
            spinner.setRevolutionsPerSecond(1)
            #spinner.setColor(QColor(81, 4, 71))
            spinner.setStyleSheet(stylesheet)
            spinner.setPalette(palette)
        # Dialog box
        self.msgBox = QMessageBox()
        self.msgBox.buttonClicked.connect(self.dialogButtonClicked)
        # Thread
        self.imdbThread = QThread()
        self.imdbWorker = None
        self.torrentThread = QThread()
        self.torrentWorker = None
        # Group box borders
        self.ui.imdbSearchGroupBox.setStyleSheet("QGroupBox#imdbSearchGroupBox {border:0;}")
        self.ui.torrentSearchGroupBox.setStyleSheet("QGroupBox#torrentSearchGroupBox {border:0;}")

    def clearImdbSearch(self):
        '''
        Clear the current search
        '''
        self.imdbSearcher.clear()
        self.imdbResultListModel.setStringList([])
        self.ui.torrentSearchButton.setEnabled(False)

    def clearTorrentUI(self, keepTitle=False):
        self.torrentResultListModel.setStringList([])
        self.ui.torrentInfoLabel.clear()
        self.ui.torrentUrlLabel.clear()
        self.ui.torrentSearchButton.setEnabled(False)
        self.ui.torrentResultListView.setEnabled(False)
        self.ui.torrentSendButton.setEnabled(False)
        if not keepTitle:
            self.ui.torrentSearchGroupBox.setTitle("First select a movie from IMDb")
        self.currentTorrentSelection = None

    def updatePoster(self, url: str):
        '''
        Update the poster image on the UI from an URL
        '''
        self.ui.moviePosterLabel.clear()
        if url is not None:
            image = QImage()
            image.loadFromData(requests.get(url).content)
            pixmap = QPixmap(image)
            self.ui.moviePosterLabel.setPixmap(pixmap.scaled(self.ui.moviePosterLabel.width(), 
                                                self.ui.moviePosterLabel.height()))
            self.ui.moviePosterLabel.show()
        else:
            logger.warning("No cover for movie")

    ###########################################################################################
    ## IMDb Search
    ###########################################################################################
    def imdbWorkerFinished(self, byID:bool, input:str):
        '''
        Connected to the finished signal of the IMDb search Worker
        '''
        logger.debug("IMDb Thread finished !")
        self.ui.spinnerImdb.stop()
        self.ui.searchImdbButton.setEnabled(True)
        self.ui.imdbResultListView.setEnabled(True)
        if byID:
            self.imdbItemClickedResult(input)
        else:
            self.searchImdbClickedResult()

    def setupImdbThread(self, input, byID=False, includeTv=False):
        '''
        Setup a thread for the IMDb search which is quite long
        input: the input to be passed to the search
        byID: Set to True if input refers to a movie ID
        '''
        # Setup IMDb thread
        # UI stuff first
        self.ui.spinnerImdb.start()
        self.ui.searchImdbButton.setEnabled(False)
        self.ui.imdbResultListView.setEnabled(False)
        # Create a QThread object
        if not self.imdbThread.isRunning():
            # Create a worker object
            self.imdbWorker = ImdbSearchWorker(self.imdbSearcher, input=input, byID=byID, includeTv=includeTv)
            # Move worker to the thread
            self.imdbWorker.moveToThread(self.imdbThread)
            # Connect signals and slots
            self.imdbThread.started.connect(self.imdbWorker.run)
            self.imdbWorker.finished.connect(self.imdbThread.quit)
            self.imdbWorker.finished.connect(self.imdbWorker.deleteLater)
            # Final resets
            self.imdbWorker.finished.connect(self.imdbWorkerFinished)
            return True
        return False

    def searchImdbClicked(self):
        '''
        Called when the user clicks the search button (or enter)
        '''
        self.clearImdbSearch()
        self.clearTorrentUI()
        input = self.ui.searchEdit.text()
        includeTv = self.ui.seriesCheckBox.isChecked()
        # Search movie
        # We enforce that the previous search must be finished first
        if self.setupImdbThread(input, includeTv=includeTv):
            self.imdbThread.start()

    def imdbListItemClicked(self, index:QModelIndex):
        '''
        Called when an item from the IMDb listView is clicked by user
        '''
        self.clearTorrentUI()
        #self.ui.torrentSearchButton.setEnabled(False)
        # Search movie
        title = self.imdbResultListModel.stringList()[index.row()]
        includeTv = self.ui.seriesCheckBox.isChecked()
        mov = self.imdbSearcher.get_movie_from_title(title)
        self.currentMovieSelection = mov
        self.ui.torrentSearchGroupBox.setTitle("Search for {}".format(title))
        # We enforce that the previous search must be finished first
        if mov.fullySearched:
            self.updateImdbResultUI()
        else:
            if self.setupImdbThread(mov.imdbId, byID=True, includeTv=includeTv):
                self.imdbThread.start()

    def searchImdbClickedResult(self):
        '''
        Called when the IMDb search Worker has finished, if byID is False
        '''
        movieList = self.imdbSearcher.moviesList
        titles_list = [movieList[i].title for i in range(len(movieList))]
        # Populate list widget
        self.imdbResultListModel.setStringList(titles_list)

    def imdbItemClickedResult(self, input):
        '''
        Called when the IMDb search Worker has finished, if byID is True
        input is the actual input that was previously passed to the search
        '''
        movieObj = self.imdbSearcher.get_movie_from_id(input)
        logger.info(f"Finished query for {movieObj.title} input: {input}")
        self.updateImdbResultUI()

    def updateImdbResultUI(self):
        movie = self.currentMovieSelection
        self.updatePoster(movie.coverUrl)

        self.ui.ratingLabel.setText(str(movie.rating)+"/10" if movie.rating else "")
        if movie.rating:
            self.ui.ratingImdbLogo.show()
        else:
            self.ui.ratingImdbLogo.hide()
        self.ui.summaryLabel.setText(movie.summary + "\r\n" + (movie.plot if movie.plot else ""))
        s_link = "<a href=\"https://www.imdb.com/title/tt" + movie.imdbId + "\">IMDb Page</a>"
        self.ui.imdbLinkLabel.setText(s_link)
        # Enable torrent search button
        self.ui.torrentSearchButton.setEnabled(True)

    ###########################################################################################
    ## Torrent Search
    ###########################################################################################
    def setupTorrentThread(self, imdbId, title):
        '''
        Setup a thread for the Torrent search which is quite long
        input: the input to be passed to the search
        '''
        # Setup IMDb thread
        # UI stuff first
        self.ui.spinnerTorrent.start()
        self.ui.torrentSearchButton.setEnabled(False)
        self.ui.torrentResultListView.setEnabled(False)
        # We use the same thread as IMDb since they cannot run concurrently
        if not self.torrentThread.isRunning():
            settings = SettingsHelper.retrieveSettings(self.settingsObj)
            # Create a worker object
            self.torrentWorker = TorrentSearchWorker(self.torrentSearcher, 
                                                     imdbId, 
                                                     title, 
                                                     yts=self.ui.ytsCheckBox.isChecked(), 
                                                     jackett=self.ui.jackettCheckBox.isChecked(),
                                                     jackettApiKey=settings.jackettApiKey,
                                                     jackettHost=settings.jackettHost)
            # Move worker to the thread
            self.torrentWorker.moveToThread(self.torrentThread)
            # Connect signals and slots
            self.torrentThread.started.connect(self.torrentWorker.run)
            self.torrentWorker.finished.connect(self.torrentThread.quit)
            self.torrentWorker.finished.connect(self.torrentWorker.deleteLater)
            # Final resets
            self.torrentWorker.finished.connect(self.searchTorrentClickedResult)
            return True
        return False
    
    def searchTorrentClicked(self):
        '''
        Called when the user clicks the torrent search button
        '''
        self.clearTorrentUI(keepTitle=True)
        mov = self.currentMovieSelection
        logger.info(f"Searching torrent for {mov.imdbId} : {mov.title}")
        if self.setupTorrentThread(mov.imdbId, mov.title):
            self.torrentThread.start()

    def torrentListItemClicked(self, index:QModelIndex):
        '''
        Called when an item from the torrent listView is clicked by user
        '''
        input = self.torrentResultListModel.stringList()[index.row()]
        selection = None
        for desc in self.currentTorrentsResults:
            if desc.description == input:
                selection = desc
                break
        assert selection, "Torrent selection not found, this should not happen"
        # Format torrent details
        s = 'Torrent\n=====\nTitle: %s\n' % selection.name
        s += 'Quality: %s\n' % selection.quality
        s += 'Type: %s\n' % selection.type
        s += 'Size: %s\n' % selection.size
        s += 'Seeds: %s\n' % str(selection.seeds)
        s += 'Provider: %s\n' % selection.provider
        self.ui.torrentInfoLabel.setText(s)
        s_link = "<a href=\""+ selection.url + "\">Torrent Link</a>"
        self.ui.torrentUrlLabel.setText(s_link)
        # Check validity of RPC settings and enable download button if they are
        self.ui.torrentSendButton.setEnabled(SettingsHelper.rpcSettingsValid(self.settingsObj))
        # Set as currently selected torrent
        self.currentTorrentSelection = selection

    def sendTorrentClicked(self):
        '''
        Called when the user clicks the download button
        '''
        tor = self.currentTorrentSelection
        settings = SettingsHelper.retrieveSettings(self.settingsObj)
        SettingsHelper.showSettings(settings)
        logger.info(f"Sending torrent to transmission client : {tor.name} url: {tor.url}")
        client = TorrentDownloader(settings.hostname, settings.username, settings.password, settings.downloadDir if settings.downloadDir != "" else None)
        result, info = client.add_torrent_magnet(tor.url)
        self.showDialog(info, error=result==False)

    def newSettingsApplied(self):
        '''
        Called when new settings are applied by the user
        '''
        self.ui.torrentSendButton.setEnabled(SettingsHelper.rpcSettingsValid(self.settingsObj) 
                                             and self.currentTorrentSelection is not None)
        
    def searchTorrentClickedResult(self, imdbId):
        '''
        Called when the torrent search has completed
        '''
        self.ui.spinnerTorrent.stop()
        self.ui.torrentSearchButton.setEnabled(True)
        self.ui.torrentResultListView.setEnabled(True)
        torrents = self.torrentSearcher.get_torrents_from_id(imdbId)
        if torrents:
            desc_list = [torrents[i].description for i in range(len(torrents)) if torrents[i] is not None]
            self.torrentResultListModel.setStringList(desc_list)
            self.currentTorrentsResults = torrents
        else:
            self.showDialog("No torrent found for selection :(")

    def dialogButtonClicked(self):
        '''
        Close the dialog when user confirms
        '''
        self.msgBox.hide()

    def showDialog(self, text:str, error=False):
        '''
        Shows a dialog containing the input text
        '''
        if error:
            self.msgBox.setIcon(QMessageBox.Critical)
        else:
            self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText(text)
        self.msgBox.setWindowTitle("Message")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.show()

def main_pyqt():
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    app.setApplicationName("MovieFinder")
    app.setOrganizationName("rnrd")

    settings = QSettings("MovieFinder", "rnrd")
    settingsWindow = SettingsWindow(settings)
    mainWindow = MainWindow(settingsWindow, settings)

    # For testing, keep commented
    #SettingsHelper.clearSettings(settings)
    QtGui.QImageReader.setAllocationLimit(0)
    mainWindow.show()
    mainWindow.setFixedSize(1530, 655)
    sys.exit(app.exec())

if __name__ == "__main__":
    main_pyqt()