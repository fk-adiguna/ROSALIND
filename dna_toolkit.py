Nucleotides = ['A', 'C', 'G', 'T']

# Checks sequence to make sure it is a DNA string
def validate_sequence(dna_sequence):
    standard_sequence = dna_sequence.upper()
    for nucleotide in standard_sequence:
        if nucleotide not in Nucleotides:
            return False
    return standard_sequence

