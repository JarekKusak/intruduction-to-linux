#!/bin/bash

set -ueo pipefail

test -f .NO_HEADER && exit 0
test -f HEADER && cat HEADER && exit 0
echo "Error: HEADER not found."
exit 1
