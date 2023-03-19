#!/bin/bash

set -ueo pipefail

DIRECTORY=${BACKUP_DIR:-~/backup}
FILE_NAME=$1
REAL_PATH=$(realpath $FILE_NAME | tr "/" "~")
DATE=$(date +"%Y-%m-%d_%H-%M-%S_")
cp -R $FILE_NAME $DIRECTORY/$DATE$REAL_PATH
ls $DIRECTORY/$DATE$REAL_PATH
