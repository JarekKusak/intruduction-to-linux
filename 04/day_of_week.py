#!/usr/bin/env python3

import sys
import datetime

def date_to_day(file):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for line in file:
        if line == "" or line == "\n":
            continue
        newstring = line.split(None, 1) # divides line into two segments: (possible) date and rest of line
        datum = newstring[0].split("-") # tries to split the possible date by "-" into three parts - year, month, day
        if len(datum) != 3: # if it doesn't have the format -> not a string
            print(line[:-1])
            continue
        dt = datetime.datetime(int(datum[0]), int(datum[1]), int(datum[2])) # convert strings to datetime
        wd = dt.weekday() # n. of weekday
        if len(newstring) > 1: # if rest of the sentence exists
            line = days[wd]+" "+ newstring[1][:-1] # print day + rest of the sentence (withou \n - was messing the output)
        else: # print only date
            line = days[wd]
        print(line) # print the result
        

def main():
    noveVety = []
    exit_code = 0
    if len(sys.argv) == 1:
        date_to_day(sys.stdin)
    else:
        for filename in sys.argv[1:]:
            try:
                with open(filename, "r") as file:
                    date_to_day(file)
            except IOError as e:
                print(f"Error reading file {filename}: {e}", file=sys.stderr)
                exit_code = 1           
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

