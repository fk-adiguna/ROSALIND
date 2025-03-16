from dna_toolkit import *
from dna_structures import *

FASTA_file = read_file('test_data/consensus.txt')

data = FASTA_sort(FASTA_file)
sequences = [fasta for key, fasta in data.items()]

def profile_matrix(sequences):
    meta_count = [''.join([seqeunce[index] for seqeunce in sequences]) for index in range(8)]
    count = {base: [position.count(base) for position in meta_count] for base in NUCLEOTIDES}

        

        

    return count

def other_profile_matrix(sequences):
    count = {base: [0,0,0,0,0,0,0,0] for base in NUCLEOTIDES}
    for sequence in sequences:
        for index, base in enumerate(sequence):
            count[base][index] += 1




    for base in NUCLEOTIDES:
        stg = ' '.join(str(number) for number in count[base])
        print(f'{base}: {stg}')


from collections import Counter

def f(sequences):
    #loops through every position
    count = {}
    #creates an array where the ith element is a string composed of the ith character in each sequence
    positions = [''.join([seqeunce[index] for seqeunce in sequences]) for index in range(len(sequences[0]))]
    #sets the base to an array where the ith element is the number of times that base appears in the ith string of the positions array
    for base in NUCLEOTIDES:
        count[base] = [position.count(base) for position in positions]

    #grabs the most common character in each element of the positions array
    #concats this to the consensus string
    consensus = ''
    for position in positions:
        consensus += max(position, key=position.count)
    
    #formatting for ROSALIND submission
    print(consensus)
    for base in NUCLEOTIDES:
        print(f'{base}: {' '.join(str(number) for number in count[base])}')

f(sequences)


