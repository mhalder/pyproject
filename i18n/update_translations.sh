#!/bin/bash

if [ $# -ne 0 ]; then
    echo "Usage: $0"
    echo ""
    echo "No parameters required." 
    exit 65
fi

POT_FILE=`ls *.pot`

for f in *.po
do
    msgmerge --no-location --update ${f} ${POT_FILE}
done

