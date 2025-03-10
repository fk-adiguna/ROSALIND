from dna_toolkit import *

def reverse_complement(sequence):
    sequence_complement = [COMPLEMENT_NUCLEOTIDES[nucleotide] for nucleotide in sequence]
    sequence_complement.reverse()
    return ''.join(sequence_complement)

test_function(reverse_complement)



