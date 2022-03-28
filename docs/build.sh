#!/bin/bash

fast=false
while getopts :f opt;
    do
        case $opt in
            f) fast=true
    esac
done

if $fast; then
    echo "Fast building"
else
    make clean
fi

make html
python -m http.server 8000 -d _build/html/
