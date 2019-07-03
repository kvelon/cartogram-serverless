#!/bin/bash

VIRTUALENV_LOCATION=${VIRTUALENV_LOCATION:=venv-local}
PYTHON=${PYTHON:=`which python3`}

if [ ! -d "$VIRTUALENV_LOCATION" ]; then

    echo "Setting up Python virtualenv..."

    virtualenv -p "$PYTHON" "$VIRTUALENV_LOCATION/"

fi

source "$VIRTUALENV_LOCATION/bin/activate"

source ./envsettings.sh

echo "Installing software components..."

pip install -r requirements.txt

echo -n "Setting environment variables... "

source ./envsettings.sh

if [ $? -eq 0 ]; then

    echo "OK"
else

    echo "FAIL"
    echo
    echo "Please make sure that envsettings.sh exists."
    deactivate
fi