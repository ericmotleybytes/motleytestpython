#!/bin/bash
# Build documentation for web.
scriptname=${BASH_SOURCE[0]##*/}  # just keep basename part
scriptdir=$(dirname "$BASH_SOURCE")
pushd $scriptdir/sphinx
./build-sphinx.bash
popd > /dev/null
echo "INFO: build-docs.bash done."
