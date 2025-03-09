from dna_toolkit import *
import random

random_dna_sequence = ''.join([random.choice(Nucleotides) for nucleotide in range(20)])
print(validate_sequence(random_dna_sequence))

