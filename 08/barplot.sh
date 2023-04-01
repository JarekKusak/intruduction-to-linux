#!/bin/bash

#set -ueo pipefail

FILE=$1
[ -s $FILE ] || exit 0
COLUMN=${COLUMNS:-"80"}
LONGEST_LINE=$(cat $FILE | tr -s " " | wc -L | cut -d " " -f 1)
MAX=$(cat $FILE | sort -n | tail -1 | cut -d " " -f 1)
ROW_LENGTH_WITH_MAX=$(grep $MAX $FILE | wc -L | cut -d ' ' -f 1)
MAX_HASHES=$( echo "scale=0; $COLUMN - $ROW_LENGTH_WITH_MAX - 5" | bc -l ) # závorky, mezery a pipelina
while read -r line; do	
	LABEL=$(echo $line | cut -d " " -f 2-)
	NUMBER=$(echo $line | cut -d " " -f 1)
	printf "$LABEL ($NUMBER)"
	SPACES=$( expr $LONGEST_LINE - ${#LABEL}  - ${#NUMBER})
	for i in $(seq $SPACES); do 
		printf " "
	done
	printf "|"
	HASHES=$(echo "scale=0; ($NUMBER * $MAX_HASHES) / $MAX" | bc -l)
 	if [[ $HASHES -ne 0 ]]; then
		printf " "
		for i in $(seq $HASHES); do
			printf "#"
		done
	fi
	printf "\n"
	
done < $FILE

