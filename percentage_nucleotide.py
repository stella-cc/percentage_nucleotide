#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

# Create the ArgumentParser object
parser = ArgumentParser(description="Classify a sequence as DNA or RNA and search for a motif.")

# Add arguments for the sequence and motif
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search for in the sequence")


# Parse the arguments
args = parser.parse_args()

# Convert sequence to uppercase for consistency (both DNA and RNA can be entered in any case)
args.seq = args.seq.upper()

# Function to calculate percentage of each nucleotide in the sequence
def calculate_percentage(sequence, nucleotide):
    return (sequence.count(nucleotide) / len(sequence)) * 100

# Classify the sequence as DNA, RNA, or neither
if re.search('^[ACGT]+$', args.seq):  # Check if it contains only A, C, G, T
    print('The sequence is DNA')
elif re.search('^[ACGU]+$', args.seq):  # Check if it contains only A, C, G, U (for RNA)
    print('The sequence is RNA')
else:
    print('The sequence is neither DNA nor RNA')

# If a motif is provided, search for it in the sequence
if args.motif:
    args.motif = args.motif.upper()  # Convert motif to uppercase for consistency
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"')
    if re.search(args.motif, args.seq):
        print("Motif FOUND")
    else:
        print("Motif NOT FOUND")

# Calculate and print the percentage of each nucleotide in the sequence
if 'A' in args.seq:
    print(f"Percentage of A: {calculate_percentage(args.seq, 'A'):.2f}%")
if 'T' in args.seq:
    print(f"Percentage of T: {calculate_percentage(args.seq, 'T'):.2f}%")
if 'C' in args.seq:
    print(f"Percentage of C: {calculate_percentage(args.seq, 'C'):.2f}%")
if 'G' in args.seq:
    print(f"Percentage of G: {calculate_percentage(args.seq, 'G'):.2f}%")
if 'U' in args.seq:
    print(f"Percentage of U: {calculate_percentage(args.seq, 'U'):.2f}%")
