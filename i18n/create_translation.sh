#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 LANGUAGE"
    echo ""
    echo "This creates a new language .po file for the given language locale. "
    exit 65
fi

msginit --no-translator -l $1
