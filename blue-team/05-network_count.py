#!/usr/bin/env python3

import sys
import re
import os
from pprint import pprint


ip_count = {}
error_files = []

def file_path(root_dir):
    file_paths = []
    dirs = os.walk(root_dir)
    for root, dir, files in dirs:
        for name in files:
            file_paths.append(os.path.join(root, name))
    return file_paths

def read_log(file_paths):
    for file in file_paths:
        try:
            with open (file, 'r') as f:
                for line in f:
                    read_line(line, file_paths)
        except:
            error_files.append(file)

def read_line(line, file_paths):
    search = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
    if search != None:
        append_dict(search,file_paths)

def append_dict(search, file_paths):
    for ip in search:
        if ip in ip_count.keys():
            ip_count[ip][0] += 1
        else:
            ip_count.update({ip :[1, file_paths]})

def most_common(ip_count):
    most_common_ip = ""
    counter = 0
    ip_locations = []
    for k, v in ip_count.items():
        if v[0] > counter:
            counter = v[0]
            most_common_ip = k
            ip_locations = v[1]
    print(f'most common ip {most_common_ip}\ncount: {counter}')
    print('locations:')
    pprint(ip_locations)

def main():
    root_dir= sys.argv[1]
    file_paths = file_path(root_dir)
    read_log(file_paths)
    most_common(ip_count)
    print()
    print(f'These files could not be read {error_files}')

if __name__ == '__main__':
    main()


#TODO in bash
# grep -rl 11.11.79.67
