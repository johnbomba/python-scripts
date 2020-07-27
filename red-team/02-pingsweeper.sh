#!/bin/bash

#SUBNET=192.168.1.

# read -p "Enter first 3 octets: " SUBNET
SUBNET=$1

rm pingsweep.txt

for IP in $(seq 1 254); do
ping -c 1 $SUBNET$IP | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1  >> pingsweep.txt &
done
