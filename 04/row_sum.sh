#!/bin/bash

set -eou pipefail

tr '|' '0' | tr ' ' '+' | bc
