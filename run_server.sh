#!/bin/bash

# Runs the server as it should

ROOTDIR=$(pwd)
source .env/bin/activate
$ROOTDIR/lib/google_appengine/dev_appserver.py --host=0.0.0.0 $ROOTDIR/src/