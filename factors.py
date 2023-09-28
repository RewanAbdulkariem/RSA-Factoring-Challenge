#!/usr/bin/python3
import sys
import math

def factorize_number(n):
    for i in range(2, n):
        if n % i == 0:
            print("{:d}={:d}*{:d}".format(n, n // i, i))
            break;

def main(file_path):
    try:
        with open(file_path, "r") as fptr:
            for line in fptr:
                line = int(line.strip())
                factorize_number(line)
    except FileNotFoundError:
        print(f"Error: can't open file {filename}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

