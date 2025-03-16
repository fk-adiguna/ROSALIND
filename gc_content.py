from dna_toolkit import *

FASTA_file = read_file('test_data/gc_content.txt')

def highest_gc(f : dict):
    dictionary = FASTA_sort(f)
    highest_gc_content : float = 0.00
    highest_gc_tag = ''
    for tag, sequence in dictionary.items():
        gc = gc_content(sequence)
        if gc > highest_gc_content:
            highest_gc_content = gc
            highest_gc_tag = tag

    print(highest_gc_tag[1:])
    print(highest_gc_content)

highest_gc(FASTA_file)


