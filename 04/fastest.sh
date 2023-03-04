#!/bin/bash

set -oeu pipefail

sort -r -t , -k 2 -g | cut -d , -f 1 | tail -n 1

