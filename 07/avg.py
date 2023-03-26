#!/usr/bin/env python3

import sys

def main():
    values = list(map(int, sys.argv[1:]))
    if (values == []):
        print(0)
        exit(0)
    avg = sum(values) / len(values)
    print(avg)

if __name__ == "__main__":
    main()
