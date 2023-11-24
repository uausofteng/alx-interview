#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split()
    if len(parts) >= 9:
        return int(parts[-1])
    return 0

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            file_size = parse_line(line)
            total_size += file_size

            status_code = line.split()[8]
            if status_code.isdigit() and int(status_code) in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_codes[int(status_code)] = status_codes.get(int(status_code), 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

