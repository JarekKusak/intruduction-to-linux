#!/bin/bash

set -ueo pipefail

printThisDirectory(){
    CURR_DIR_FILES=$(ls $PWD)
    for file in $CURR_DIR_FILES 
    do
        if [ -d $file ]; then 
            echo $file "<dir>"
        elif [ -f $file ]; then
            echo $file $(stat --printf="%s\n" $file)
        else
            echo $file "<special>"
        fi
    done | column --table --table-noheadings --table-columns FILENAME,SIZE --table-right SIZE
}

# zpracování options:
if [ $# -eq 0 ]; then
    printThisDirectory
fi
for file in "$@"
    do
        if ! [ -e $file ]; then
        echo "$file: no such file or directory." >&2
        exit 1
        fi
        
        if [ -d $file ]; then 
            echo $file "<dir>"
        elif [ -f $file ]; then
            echo $file $(stat --printf="%s\n" $file)
        else
            echo $file "<special>"
        fi
    done | column --table --table-noheadings --table-columns FILENAME,SIZE --table-right SIZE
