#!/usr/bin/env python3

import sys
import re

found_ip=True
interface=""
ip=""

for line in sys.stdin:
    words_in_line = line.split()
    if len(words_in_line) == 0: continue
    if re.match(r"^[0-9]+:", words_in_line[0]): # řádek začíná číslem rozhraní
        if found_ip == False:
            sys.stdout.write(f"{interface} 0.0.0.0/0\n")
        found_ip = False
        interface=words_in_line[1][:-1] # uloží název rozhraní bez dvojtečky
    elif re.match(r"^inet(?![6])", words_in_line[0]):
        found_ip = True
        ip=words_in_line[1]
        sys.stdout.write(f"{interface} {ip}\n")
    else:
        continue

if found_ip == False: # poslední kontrola, zda bylo přidělena rozhraní ip adresa
    sys.stdout.write(f"{interface} 0.0.0.0/0\n")