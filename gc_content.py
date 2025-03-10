from dna_toolkit import *

def gc_content(sequence: str ):
    return str((sequence.count('C') + sequence.count('G')) * 100/len(sequence))


