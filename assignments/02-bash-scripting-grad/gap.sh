#/usr/bin/env bash

## Bash Script for Gap Outputs: 2nd Assignment Grad Student
## Written by: Wen Yu (Amy) Wong

## Script for relative path to gapminder folder

RUN_PATH=$(pwd)

cd ../../data/gapminder


## 1) If no arguments are found, print all the basenames of the files
## 2) If there is an argument, treat like regular expression and find files where the basename matches at the
##  beginning of the string in a case-insensitive manner and print them in sorted order
## 3) If no files are found, print a message telling the user

DIR=$(ls)
EXP=$1
RESULTS_FILE="$RUN_PATH/RESULTS.txt"

if [[ $# -eq 0 ]]; then
	ls $DIR|cut -f1 -d"." 
	exit 0
elif [[ $# -gt 0 ]]; then
	ls|grep -i "^$EXP"|sort|uniq|cut -f1 -d"."|awk 'BEGIN {OFS="\t"} {print NR, $0}' > $RESULTS_FILE
	if [[ -s "$RESULTS_FILE" ]]; then
                cat $RESULTS_FILE
        else
            	echo 'There are no countries starting with "'$EXP'"'
		exit 1
        fi
	exit 0
fi
