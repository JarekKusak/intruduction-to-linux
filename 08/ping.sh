#!/bin/bash

#set -ueo pipefail

opts_short="w:vd:"
opts_long="verbose,delimiter:"

getopt -Q -o "$opts_short" -l "$opts_long" -- "$@" || exit 1

eval set -- "$( getopt -o "$opts_short" -l "$opts_long" -- "$@" )"

DELIMITER=" "
C=1
VERBOSE_FLAG=0
OUT_FILE=/dev/null
while [ $# -gt 0 ]; do
    case "$1" in
        -d|--delimiter) 
            DELIMITER=$2
            shift
            ;;
        -w) # něco jiného než výchozí jedna sekunda
            C=$2
            shift
            ;;
        -v|--verbose)
            VERBOSE_FLAG=1
            OUT_FILE=/dev/stdout
            ;;
        --) shift
            break
            ;;
        *)
            echo "Unknown option $1" >&2
            exit 1
            ;;
    esac
    shift
done

EXIT_CODE=0

for arg in "$@"; do
    ping -c $C $arg > $OUT_FILE 2>/dev/null
    if [  $? -eq 0 ]; then 
        echo "$arg$DELIMITER""UP" 
    else 
        echo "$arg$DELIMITER""DOWN"
        EXIT_CODE=$(echo "scale=0; $EXIT_CODE+1" | bc -l)
    fi
done

exit $EXIT_CODE