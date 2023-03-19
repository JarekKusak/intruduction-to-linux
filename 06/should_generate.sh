#!/bin/bash

set -ueo pipefail

function should_generate() {
	MD_FILE=$1
	NAME=$(echo $MD_FILE | cut -d "." -f 1)
	return $(test $MD_FILE -nt $NAME.html)
}

