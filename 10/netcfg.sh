#!/bin/bash

set -ueo pipefail

while read -r line; do echo "$line" >> temp; done

for i in $(cat temp | sed -En 's/^[0-9]*: (.*):.*/\1/p'); do
    ROW=""
    if ! [ -z "$(cat temp | grep -E "inet.*$i$")" ]; then
        ROW=$(cat temp | grep -E "inet.*$i$")
        IP=$(echo $ROW | cut -d " " -f 2)
        echo "$i $IP"
    else
        echo "$i 0.0.0.0/0"
    fi
done

rm temp
