#!/bin/bash

# create archive directory if it doesn't exist
if [ -d "archive" ]
then
    echo "Archive folder already exists. Proceeding with archival..."
else
    echo "Creating archive folder..."
    mkdir archive
fi

# the archival process
timestamp=$(date +%Y%m%d-%H%M%S)

if [ ! -f "grades.csv" ]
then
    echo "Error: grades.csv not found. Nothing to archive."
    exit 1
fi

mv grades.csv archive/grades_${timestamp}.csv

# workspace reset
touch grades.csv

# logging
echo -e "Archival completed at ${timestamp} \t Original filename: grades.csv \t Archived filename: grades_${timestamp}.csv" >> organizer.log