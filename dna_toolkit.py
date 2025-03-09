import random

NUCLEOTIDES = ['A', 'C', 'G', 'T']
COMPLEMENT_NUCLEOTIDES = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}


# Checks sequence to make sure it is a DNA string
def validate_sequence(dna_sequence):
    standard_sequence = dna_sequence.upper()
    for nucleotide in standard_sequence:
        if nucleotide not in NUCLEOTIDES:
            return False
    return standard_sequence

def generate_random_dna_sequence(length):
    sequence = ''.join([random.choice(NUCLEOTIDES) for i in range(length + 1)])
    return sequence

