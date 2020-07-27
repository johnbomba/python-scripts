#!/usr/bin/env python3

import re
import os
import hashlib as h
import sys
from pprint import pprint

HASH_LIST = []

'''
Hash algos:
    - md5
    - sha-512
    - sha-128 (sha1)
    - sha2-256
    - sha2-384
    - sha-224
'''
HASH_ALGOS = [h.md5, h.sha512, h.sha1,h.sha256, h.sha384, h.sha224]

HASH_DICT = {}

def file_paths(root_dir):
    file_paths = []
    dirs = os.walk(root_dir)
    for root, dir, files in dirs:
        for name in files:
            file_paths.append(os.path.join(root, name))
#    print(file_paths)
    return file_paths

def read_hash(hash_file):
    with open (hash_file, 'r') as f:
        for line in f:
            HASH_LIST.append(line.strip())

def hash_files(file_path):
#    print(file_path)
    for hash in HASH_ALGOS:
        for file in file_path:
            with open (file, 'rb') as f:
                contents = f.read()
                HASH_DICT.setdefault(hash(contents).hexdigest(), list()).append(file)

#    pprint(HASH_DICT)

def compair_hashes(HASH_LIST, HASH_DICT):
    for hash in HASH_LIST:
        if hash in HASH_DICT.keys():
            print(f'Found the file {HASH_DICT[hash][0]} with the hash of {hash}')

def main():
    hash_file = sys.argv[1]
    root_dir = sys.argv[2]
    read_hashes = read_hash(hash_file)
    file_path = file_paths(root_dir)
    hashed_file = hash_files(file_path)
    compair_hashes(HASH_LIST, HASH_DICT)

if __name__ == '__main__':
    # TODO usage if statement
    main()
