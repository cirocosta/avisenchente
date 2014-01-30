#!/bin/bash

# Deploys the application to the specified email with appengine


ROOTDIR=$(pwd)
$ROOTDIR/lib/google_appengine/appcfg.py update src/