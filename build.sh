#!/bin/bash
rm -rf dist/ build/
source venv.sh
pip install -e pyqt/QtWaitingSpinner
pyinstaller run_pyqt.py --name MovieFinder --icon=resources/imdb.ico --windowed --clean --add-data 'resources/imdb.png;.' --onefile
