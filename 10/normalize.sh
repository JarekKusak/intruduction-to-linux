#!/bin/bash

set -ue

path=$1
REALPATH=$(echo "$path" | sed ':x; s|/\./|/|; s|[^/]*/\.\./||; s|//|/|; tx')
echo "$REALPATH"
