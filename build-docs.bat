@echo off
rem Build documentation for web.
set thisbuilddocdir=%~dp0
pushd %thisbuilddocdir%\sphinx
build-sphinx.bat
popd
cd %thisbuilddocdir%
echo build-docs.bat done.
