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
    sequence = ''.join([random.choice(NUCLEOTIDES) for i in range(length + 1)])
    return sequence

def get_most_recent_file():
    global most_recent_time
    global most_recent_file
    for entry in os.scandir(TEST_CASES_PATH):
        print('entry name: ', entry.name, '\nlast modified time: ', entry.stat().st_mtime_ns)
        if not entry.is_file(): return
        modified_time = entry.stat().st_mtime_ns
        if modified_time > most_recent_time:
            most_recent_time = modified_time
            most_recent_file = entry.name
            return entry
        