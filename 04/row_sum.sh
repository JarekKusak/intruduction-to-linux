#!/bin/bash

set -eou pipefail

tr -s ' ' | cut -d ' ' -f 2- | tr '|' '0' | tr ' ' '+' | bc
