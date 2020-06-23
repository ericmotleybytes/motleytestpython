#!/bin/bash
# Build sphinx documentation for web.
scriptname=${BASH_SOURCE[0]##*/}  # just keep basename part
scriptdir=$(dirname "$BASH_SOURCE")
pushd $scriptdir
if [ -d ./napgen ]; then
    rm -rf ./napgen
fi
mkdir ./napgen
if [ -d ./docs/gen ]; then
    rm -rf ./docs/gen
fi
mkdir ./docs/gen
cp conf.py napgen/conf.py
cp index.rst napgen/index.rst
sphinx-apidoc -f -o  ./napgen ../src/motleydatetime
sphinx-build -b html -c . ./napgen ../docs/gen
popd > /dev/null
echo "INFO: build-sphinx.bash done."
