from flask import Flask, render_template, request
import configparser, pathlib, json
from pymoviefinder.ImdbSearcher import ImdbSearcher
from pymoviefinder.TorrentSearcher import TorrentSearcher
from pymoviefinder.TorrentDownloader import TorrentDownloader
import argparse
from waitress import serve

app = Flask(__name__)
docker=False
config = None

@app.route('/', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        # IMDb titles search
        if request.form.get('search_imdb_title'):
            include_serie = request.form.get('series_check')
            imdbResult = ImdbSearcher().searchByTitle(request.form.get('search_imdb_title'), no_series = not include_serie)
            return render_template('main.html', imdbResult=imdbResult)
        # IMDb ID + Torrent search
        if request.form.get('search_imdb_id'):
            # Search by ID
            inputs = json.loads(request.form.get('search_imdb_id'))
            if type(inputs) is dict:
                movieId, yts, jackett = inputs['movieId'], inputs['yts'], inputs['jackett']
                idResult = ImdbSearcher().searchById(movieId)
                # Get Jackett config if needed
                [jHost, jApiKey] = None, None
                if jackett:
                    try:
                        [jHost, jApiKey] = getJackettConfig()
                    except Exception as e:
                        return render_template('main.html', downloadResult=str(e))
                # Search torrent
                searcher = TorrentSearcher()
                searcher.setSearch(movieId, idResult.title, yts=yts, jackett=jackett, jackettApiKey=jApiKey, jackettHost=jHost)
                torrentResult = searcher.run()
                return render_template('main.html', idResult=idResult, torrentResult=torrentResult)
        # Add torrent through RPC
        if request.form.get('send_torrent'):
            try:
                [host, usr, pw] = getRpcConfig()
            except Exception as e:
                return render_template('main.html', downloadResult=str(e))
            dl = TorrentDownloader(host, usr, pw)
            downloadResult = dl.add_torrent_magnet(request.form.get('send_torrent'))
            return render_template('main.html', downloadResult=downloadResult)
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('main.html')
    
    return render_template('main.html')

def getRpcConfig():
    if config.has_section("RPC"):
        print("Using config.ini for RPC configuration")
        return [config.get('RPC','Host'), config.get('RPC','User'), config.get('RPC','Password')]
    else:
        raise Exception("No config found for RPC")
    
def getJackettConfig():
    if config.has_section("Jackett"):
        return [config.get('Jackett','Host'), config.get('Jackett','ApiKey')]
    else:
        raise Exception("No config found for Jackett")
    
def main_flask():
    parser = argparse.ArgumentParser(description="Flask app for movie search")
    parser.add_argument("-d","--docker", help="Run flask for Docker", action='store_true')
    args = vars(parser.parse_args())
    global docker, config
    docker = args['docker']
    
    # Check config
    config = configparser.ConfigParser()
    config_path = str(pathlib.Path(__file__).parent) + "/config/config.ini" if docker else \
        str(pathlib.Path(__file__).parent.parent) + "/config/config.ini"
    config.read(config_path)
    if len(config) == 0:
        raise Exception("Config file not found")
    
    host = "0.0.0.0" if docker else "127.0.0.1"
    serve(app, host=host, port=5000)

if __name__ == "__main__":
    main_flask()