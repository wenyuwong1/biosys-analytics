#!/usr/bin/env bash

## Bash Script for Hello Outputs: 2nd Assignment Grad Student
## Written by: Wen Yu (Amy) Wong

## Script to determine if an argument is entered

if [[ $# -eq 0 ]]; then
	echo "Usage: hello.sh GREETING [NAME]"
	exit 1
fi

## Assigning Variable Names to Arguments and Defaulting $2 to value Human
GREETING=$1
NAME=${2:-"Human"}

## If the first argument (GREETING) is not provided, it will error. Otherwise it will proceed. 
## If the second argument (NAME) is provided, it will be incorporated.
## If a third argument is provided, it will error

if [[ $# -eq 1 ]] || [[ $# -eq 2 ]]; then
	echo "$GREETING, $NAME!"
	exit 0
elif  [[ $# -gt 2 ]]; then
	echo "Usage: hello.sh GREETING [NAME]"
	exit 1
fi


