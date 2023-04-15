#!/usr/bin/env python3

import argparse
import sys

def splitter(line, field_separator, key_column, value_column):
    parts = line.split(field_separator)
    return (parts[key_column - 1], parts[value_column - 1])

def sum_file(inp, results, line_splitter):
    for line in inp:
        (key, number) = line_splitter(line)
        results[key] = results.get(key, 0) + int(number)

def main():
    args = argparse.ArgumentParser(description='Group sum')
    args.add_argument(
        '-t', '--input-separator',
        dest='input_field_separator',
        default=None,
        metavar='SEP',
    )
    args.add_argument(
        '-d', '--output-separator',
        dest='output_field_separator',
        default=None,
        metavar='SEP',
    )
    args.add_argument(
        '-k', '--key',
        dest='key_column',
        type=int,
        default=1,
        metavar='INTEGER',
    )
    args.add_argument(
        '-v', '--value',
        dest='value_column',
        type=int,
        default=2,
        metavar='INTEGER',
    )
    args.add_argument(
        nargs='*',
        default=[],
        dest='sources',
        metavar='FILE',
    )

    config = args.parse_args()
    if config.output_field_separator is None:
        config.output_field_separator = config.input_field_separator
        if config.output_field_separator is None:
            config.output_field_separator = '\t'

    line_splitter = lambda line: splitter(line, config.input_field_separator, config.key_column, config.value_column)

    sums = {}
    if not config.sources:
        sum_file(sys.stdin, sums, line_splitter)
    else:
        for filename in config.sources:
            with open(filename, "r") as inp:
                sum_file(inp, sums, line_splitter)

    for key, value in sums.items():
        print(f"{key}{config.output_field_separator}{value}")

if __name__ == "__main__":
    main()

