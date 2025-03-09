from dna_toolkit import *
import collections

random_dna_sequence = validate_sequence(generate_random_dna_sequence(50))

def count_dna_nucleotides(sequence):

    count = {'A' : 0,
             'C' : 0,
             'G' : 0,
             'T' : 0,
             }

    for nucleotide in sequence:
        count[nucleotide] += 1
    
    return ' '.join([str(count[nucleotide]) for nucleotide in count])

    # return dict(collections.Counter(sequence))

print(count_dna_nucleotides(random_dna_sequence))




