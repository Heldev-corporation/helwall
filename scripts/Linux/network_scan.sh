#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <target_ip/subnet>"
    exit 1
fi

target_ip=$1
nmap -sP $target_ip
