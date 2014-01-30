#!/bin/sh

# Sets up the development environment.
# It requires the previous installation of Python2.7+,
# PyPI for running and creating the virtualenv and
# git for getting the iot-sdk-python lib from github.

VERSION="1.8.9"
ROOTDIR=$( cd $(dirname $0) && pwd )
LIBDIR=$ROOTDIR/lib


cd $ROOTDIR

# Creates the virtualenv
virtualenv $ROOTDIR/.env

mkdir $LIBDIR $ROOTDIR/build

# Download the SDK
curl http://googleappengine.googlecode.com/files/google_appengine_${VERSION}.zip \
	 -o /tmp/google_appengine_${VERSION}.zip

# Unzip it
cd $ROOTDIR/build
unzip -q /tmp/google_appengine_${VERSION}.zip
rm  /tmp/google_appengine_${VERSION}.zip

# Move it to the library folder
cd $ROOTDIR
mv -v $ROOTDIR/build/google_appengine lib

# Link the binaries to the virtualenv bin directory
ln -sv $LIBDIR/google_appengine/*.py $ROOTDIR/.env/bin/

# Set the .pth files
cp resources/autogenerated $ROOTDIR/.env/lib/python2.7/site-packages/src.pth
echo "$ROOTDIR/src/" >> $ROOTDIR/.env/lib/python2.7/site-packages/src.pth

cp resources/autogenerated $ROOTDIR/.env/lib/python2.7/site-packages/gae.pth
echo "$LIBDIR/google_appengine/" >> \
	  $ROOTDIR/.env/lib/python2.7/site-packages/gae.pth
echo "import dev_appserver; dev_appserver.fix_sys_path()" >> \
	  $ROOTDIR/.env/lib/python2.7/site-packages/gae.pth

# Activates the virtualenv environment

. $ROOTDIR/.env/bin/activate
pip install -r $ROOTDIR/resources/requirements.txt