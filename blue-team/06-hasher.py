#!/usr/bin/env python3

import re
import os
import hashlib
import sys
from pprint import pprint

def file_path(root_dir):
    # find files in dir
    file_paths = []
    file_names = []
    dirs = os.walk(root_dir)
    #print(dirs)
    for root, dir, files in dirs:
        for name in files:
            file_paths.append(os.path.join(root, name))
            file_names.append(name)

    file_names = sorted(file_names)
    return file_paths, file_names

#TODO fix this shit
def sorted_paths(file_paths, file_names):
    sort_paths = []
    for name in file_names:
        for path in file_paths:
            if name in path:
                sort_paths.append(path)
#        expression = re.search(name, file_paths)
#        sort_paths.append(expression)
    return sort_paths



def file_hash(sort_paths):
    hash_list = []
    BUF_SIZE = 65536
    for file in sort_paths:
        # hash file
        sha1 = hashlib.sha1()
        with open(file, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
                hash_list.append(sha1.hexdigest())
#    print(hash_list)
    return hash_list

def mega_hash(file_hashes):
    # iterate through list
    sha1 = hashlib.sha1()
    for hash in file_hashes:
    # hash everyhing
        sha1.update(hash.encode())
    # return mega hash
    return sha1.hexdigest()

def main():
    hash_dir = sys.argv[1]
    file_paths, file_names = file_path(hash_dir)
    sort_paths = sorted_paths(file_paths, file_names)
    file_hashes = file_hash(sort_paths)
    mega_hashes = mega_hash(file_hashes)
    print(mega_hashes)

if __name__ == '__main__':
    main()
