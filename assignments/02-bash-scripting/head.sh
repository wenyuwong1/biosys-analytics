#!/usr/bin/env bash

## Bash Scripting Homework Head.sh Assignment
## Written By: Wen Yu (Amy) Wong


# Test check if an argument is provided

if [[ $# -eq 0 ]]; then
        echo "Usage: head.sh FILE NUM_OF_LINES"
        exit 1
fi


## Assigning Variable Names to Arguments and Defaulting $2 to value=3

FILE=$1
NUM_OF_LINES=${2:-3}

## If the first argument(FILE) is not provided, it will error. Elif it is a file, read LINE

if [[ ! -f "$FILE" ]]; then
        echo "$FILE is not a file"
        exit 1
elif [[ -f "$FILE" ]]; then
        i=0
	while read -r LINE; do
                echo $LINE
                i=$((i+1))
                if [[ $i -eq $NUM_OF_LINES ]]; then
                        break
                fi
        done <"$FILE"
fi





