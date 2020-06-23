#!/bin/bash
# build PyPI distribution
scriptname=${BASH_SOURCE[0]##*/}  # just keep basename part
scriptdir=$(dirname "$BASH_SOURCE")
pushd $scriptdir
if [ -d ./dist ]; then
    rm -rf ./dist
fi
if [ -d ./build ]; then
    rm -rf ./build
fi
python setup.py sdist
#python setup.py bdist_wheel
popd > /dev/null
echo "INFO: build-dist.bash done."
