#!/bin/bash
# upload PyPI distribution
scriptname=${BASH_SOURCE[0]##*/}  # just keep basename part
scriptdir=$(dirname "$BASH_SOURCE")
pushd $scriptdir
# for uploading to test.pypi.org.
##twine register dist/%pkg%-%vers%.tar.gz -r testpypi
##twine upload dist/* -r testpypi
# for production upload to pypi.org.
##twine register dist/%pkg%-%vers%.tar.gz
twine upload dist/*
echo "INFO: upload-dist.bash done."
