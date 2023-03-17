#!/bin/bash

set -ueo pipefail

test -f $1 || exit 1
stat --printf="%y" $1 | cut -d " " -f 1

