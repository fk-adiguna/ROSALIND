from dna_toolkit import *
from dna_structures import *

FASTA_file = read_file('test_data/consensus.txt')

data = FASTA_sort(FASTA_file)
sequences = [fasta for key, fasta in data.items()]


def f(sequences):
    #loops through every position
    #creates an array where the ith element is a string composed of the ith character in each sequence
    positions = [''.join([seqeunce[index] for seqeunce in sequences]) for index in range(len(sequences[0]))]
    #sets the base to an array where the ith element is the number of times that base appears in the ith string of the positions array
    count = {base: [position.count(base) for position in positions] for base in NUCLEOTIDES}

    #grabs the most common character in each element of the positions array
    #concats this to the consensus string
    consensus = ''.join([max(position, key=position.count) for position in positions])
    #formatting for ROSALIND submission
    print(consensus)
    for base in NUCLEOTIDES:
        print(f'{base}: {' '.join(str(number) for number in count[base])}')

f(sequences)


