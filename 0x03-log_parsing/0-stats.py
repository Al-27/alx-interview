#!/usr/bin/python3
""" Log Parsing """
import fileinput
import re
import signal


def ctrl_c(sig, frame):
    print_stats()


status_codes = {}
total_size = 0


def print_stats():
    print(f"File size: {total_size}")
    for k, v in status_codes.items():
        if v != 0:
            print(f"{k}: {v}")


signal.signal(signal.SIGINT, ctrl_c)


for code in [200, 301, 400, 401, 403, 404, 405, 500]:
    status_codes.update({str(code): 0})

lines_processed = 0
for line in fileinput.input():
    pattern = re.compile(
        r'^(\d+\.){3}\d+ - \[(\d+-){2}\d+ (\d+:){2}\d+.\d+\]\
        "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$')

    if (pattern.findall(line)):
        match = [g for g in pattern.findall(line)[0]]
        # match 0 -> Status Code
        # match 1 -> File Size
        for i in range(3):
            match.pop(0)

        i = 1
        if (len(match) == 2):
            status_codes[match[0]] += 1
        else:
            i = 0
        total_size += int(match[i])
        lines_processed += 1

        if (lines_processed % 10 == 0):
            print_stats()
print_stats()
