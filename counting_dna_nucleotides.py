from dna_toolkit import *
import random

def count_dna_nucleotides(sequence):
    if validate_sequence(sequence) == False: return

    count = {'A' : 0,
             'T' : 0,
             'C' : 0,
             'G' : 0,
             }

    for nucleotide in sequence:
        count[nucleotide] += 1
    
    return count




