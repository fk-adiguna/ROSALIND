import random
import os

NUCLEOTIDES = ['A', 'C', 'G', 'T']
COMPLEMENT_NUCLEOTIDES = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}

TEST_CASES_PATH = 'test_cases'
most_recent_file = None
most_recent_time = 0


# Checks sequence to make sure it is a DNA string
def validate_sequence(dna_sequence):
    standard_sequence = dna_sequence.upper()
    for nucleotide in standard_sequence:
        if nucleotide not in NUCLEOTIDES:
            return False
    return standard_sequence

def generate_random_dna_sequence(length):
    return ''.join([random.choice(NUCLEOTIDES) for i in range(length + 1)])

random_dna_sequence = validate_sequence(generate_random_dna_sequence(random.randint(10, 100)))

def get_most_recent_test_file(path):
    global most_recent_time
    global most_recent_file
    for entry in os.scandir(path):
        if not entry.is_file(): return
        modified_time = entry.stat().st_mtime_ns
        if modified_time > most_recent_time:
            most_recent_time = modified_time
            most_recent_file = entry.name
            
    return most_recent_file

def read_file(pathway : str):

    with open(pathway, 'r') as file:
        return [line.strip() for line in file.readlines()]


def test_function(func):
    answer_file = open('answer.txt', 'w')
    answer = func(open(f'test_cases/{get_most_recent_test_file(TEST_CASES_PATH)}', 'r').readline().strip())
    
    answer_file.write(answer)

def gc_content(sequence: str ):
    return (sequence.count('C') + sequence.count('G')) * 100/len(sequence)

def subsection_gc_content(sequence : str, length : int = 20):
    subsection_gc = []

    for nucleotide_index in range(0, len(sequence), length):
        gc = gc_content(sequence[nucleotide_index : nucleotide_index + length])
        subsection_gc.append(f'{gc}%')

    return subsection_gc

def reverse_complement(sequence):
    sequence_complement = [COMPLEMENT_NUCLEOTIDES[nucleotide] for nucleotide in sequence]
    sequence_complement.reverse()
    return ''.join(sequence_complement)

def pythonic_reverse_complement(sequence):
    return sequence.translate(str.maketrans('ATCG', 'TAGC'))[::-1]

def count_dna_nucleotides(sequence : str = random_dna_sequence, order : str = 'ACGT'):
    return ' '.join([str(sequence.count(base)) for base in order])

def transcribe(sequence):
    return ''.join([nucleotide.replace('T', 'U') for nucleotide in sequence.upper()])

def better_transcribe(sequence):
    return sequence.upper().translate(str.maketrans('T', 'U'))