#!/bin/bash

set -ueo pipefail

test -f .NO_HEADER && exit 0
test -f HEADER && cat HEADER && exit 0
echo "Error: HEADER not found." 1>&2
exit 1
