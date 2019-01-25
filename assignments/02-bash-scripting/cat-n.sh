#!/usr/bin/env bash

## Script for Assignment #2 - Bash Scripting
## By: Wen Yu (Amy) Wong

## Script to determine if an argument is entered

if [[ $# -eq 0 ]]; then
	echo "Usage: cat-n.sh FILE"
	exit 1
fi


## Script to determine if there is a FILE argument; if there is a FILE, it will read LINE of FILE 

FILE=$1

if [[ ! -f "$FILE" ]]; then
        echo "$FILE is not a file"
        exit 1
elif  [[ -f "$FILE" ]]; then
	i=0
	while read -r LINE; do
		i=$((i+1))
		echo "$i $LINE"
	done<"$FILE"
	exit 0
fi




