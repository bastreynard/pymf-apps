# PyMovieFinder

Client for searching torrents that match an IMDb search.
The torrent found can be sent to a [transmission](https://github.com/transmission/transmission) daemon running on a remote server using RPC protocol.
It can also be simply locally downloaded.

Desktop app

![image](https://user-images.githubusercontent.com/26840072/222936655-11bbd588-3f36-4945-a679-6713af254c39.png)

Web app (Flask, Docker)

![image](https://user-images.githubusercontent.com/26840072/224577612-58509e81-0584-46b6-ab03-1eeace5d90cb.png)

## Getting started

### Prerequisite 

- Python3

- PyQT

### Run / Build

Clone the repo with `--recursive`. There are 3 applications based on the libs contained in the `pymoviefinder` directory. These applications are in the `apps` directory.

- PyQt application : A desktop GUI application
- Flask application : Can be run on a webserver and renders a templated HTML ui
- CLI application : Command line only tool to search movies

#### PyQT

`./run_pyqt.sh` : To setup the venv, install the dependencies, translate the ui with pyside6 and launch the pyqt app
  
`./build.sh` : build the pyqt app into an executable using [pyinstaller](https://github.com/pyinstaller)

#### Flask

The Flask application can be run as a Docker container application:

```bash
docker compose build
docker compose up -d
```
It will use the `config.ini` file placed in `config/config.ini.sample` and will run on port 5000.

Alternatively it's possible to just run the python script itself directly:

`./run_flask.sh` : Setup the venv, install the dependencies, launch the flask app on port 5000.

### Troubleshooting

It was tested only with `Python3.10.1`, on Windows and Ubuntu 22.04 running on WSL 2.

The only problem I encountered was this error on Linux (WSL):

    libegl.so.1 cannot open shared object file no such file or directory
It can be fixed with:

    sudo apt install libegl1

## Dependencies

This app makes use of these projects:
* [QtWaitingSpinner](https://github.com/z3ntu/QtWaitingSpinner)

## Just a note about Transmission
To use the transmission RPC feature, the remote server must have transmission installed and transmission daemon running.

### Daemon configuration
Make sure the configuration of the transmission-daemon is correct with RPC enabled and password protected.
Usually the settings file is under `/var/lib/transmission-daemon/.config/settings.json` or `/etc/transmission-daemon/settings.json` on linux.

Here is an example of a working configuration:
```json
"rpc-authentication-required": true,
"rpc-bind-address": "0.0.0.0",
"rpc-enabled": true,
"rpc-host-whitelist": "localhost",
"rpc-host-whitelist-enabled": true,
"rpc-password": "change me",
"rpc-port": 9091,
"rpc-url": "/transmission/rpc",
"rpc-username": "change me",
"rpc-whitelist": "127.0.0.1",
"rpc-whitelist-enabled": true,
```

Always stop the daemon before making changes in `settings.json`

    /etc/init.d/transmission-daemon stop


### Apache configuration
Additionaly, the webserver must be correctly configured with a reverse proxy. For Apache, the config would look like this :

    ProxyPass /transmission/rpc http://127.0.0.1:9091/transmission/rpc
    ProxyPassReverse /transmission/rpc http://127.0.0.1:9091/transmission/rpc

The port must be adapted to the actual configuration in `settings.json`
