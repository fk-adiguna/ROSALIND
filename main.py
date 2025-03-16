def motif(subsequence, sequence):
    print(*[index + 1 for index in range(len(sequence)) if sequence[index:index + len(subsequence)] == subsequence])