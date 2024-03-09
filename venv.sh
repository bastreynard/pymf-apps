#!/bin/bash
if [ ! -d "venv" ]; then
    echo "Creating virtual env..."
    python -m venv venv
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        source venv/bin/activate
    else
        source venv/Scripts/activate
    fi
else
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        source venv/bin/activate
    else
        source venv/Scripts/activate
    fi
fi

Dev=0
while getopts ":d" option; do
   case $option in
      d) # app name
         Dev=1;;
   esac
done

pip install -r requirements.txt
pip install -e pyqt/QtWaitingSpinner
if [[ $Dev -eq 1 ]]; then
pip install -e ../pyimdbmoviefinder
fi