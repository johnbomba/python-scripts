#!/usr/bin/env python3

import sys
import re
import operator
from pprint import pprint


log_dict = {}

def read_log(logfile):
    with open (logfile, 'r') as f:
        for line in f:
            search = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            if search != None:
                search = search[0]
                if search != '0.0.0.0':
                    append_dict(search)

def append_dict(line, count=1):
    if line in log_dict.keys():
        log_dict[line] += count
    else:
        log_dict.update({line : count})

def percent(log_dict):
    total_sum = sum(log_dict.values())
    return total_sum

def format(log_dict, sum):
    print('-------------------------------------')
    print('| Percent | Count |              IP |')
    print('-------------------------------------')
    sorted_log = sorted(log_dict.items(), key=lambda x: x[1])
#    print(sorted_log)
    sorted_log.sort (key= operator.itemgetter(1,0))

    for i  in sorted_log:
        percent = f'{i[1]/sum*100:.4f}'
        percent = f'{percent[0:6]}'
        val = str(i[1])
        key = i[0]
        print(f'|{percent:>8} |{val:>6} |{key:>16} |')
    print('-------------------------------------')
    total = str(sum)
    print(f'|   Total |{total:>6} |                 |')
    print('-------------------------------------')

def main():
    logfile = sys.argv[1]
    read_log(logfile)
    sum = percent(log_dict)
    format(log_dict, sum)


if __name__ == '__main__':
    main()
