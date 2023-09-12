#!/bin/sh

# Define the filename of the ciphertext
ciphertext_file="ciphertext.txt"

# Define an array of n-gram sizes to analyze
ngram_sizes=("1" "2" "3")

# Define the prefix for output files
prefix="seed"

# Loop through the n-gram sizes and run the analysis script
for n in "${ngram_sizes[@]}"
do
    python3.9 task1analysis.py "$ciphertext_file" "$n" "$prefix"
done
