#!/bin/bash

if [ -z "$1" ];then
    echo "Usage: $0 <target_ip>"
    exit 1
fi

target_ip=$1
nmap --script vuln $target_ip
