#!/usr/bin/env python3

import sys
import re


ip_count = set()
term_count = {}

def read_log(logfile):
    with open (logfile, 'r') as f:
        for line in f:
            read_src(line)
            read_dst(line)
            protocols(line)

def read_dst(line):
    search = re.search(r"DST=\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
    if search != None:
        ip = search[0]
        ip_count.add(ip[4:])

def read_src(line):
    search = re.search(r"SRC=\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
    if search != None:
        ip = search[0]
        ip_count.add(ip[4:])

def protocols(line):
    search = re.search(r"PROTO=.{3,4}", line)
    if search != None:
        term = search[0][6:]
        if term in term_count.keys():
            term_count[term] += 1
        else:
            term_count.update({term : 1})

def main():
    logfile = sys.argv[1]
    read_log(logfile)
    print(term_count)
    print(len(ip_count))
#    print(ip_count)



if __name__ == '__main__':
    main()

# doing it in bash
# grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" [insert file name here] | sort | u
# grep -oE "PROTO=\w+b" [insert file name here] | sort | uniq -c
# grep -roEh "([0-1]{1,3}\.){3}[0-9]{1,3}" | sort | uniq -c | sort -n

# grep for IP address recursively and provide file name with IP.
# grep -rl [ip address]

# grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" [insert file name here] | sort | uniq | wc -l


