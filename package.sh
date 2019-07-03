#!/bin/bash

set -x
rm -f cartogram.zip

OLDWD=$(pwd)

cd lambda_package/venv/lib/python3.6/site-packages
zip -r9 $OLDWD/cartogram.zip .

cd $OLDWD/lambda_package
zip -g $OLDWD/cartogram.zip cartogram *.py

set +x
