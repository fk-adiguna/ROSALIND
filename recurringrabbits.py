def rabbit_pairs(months, pairs_in_litter):
    if months == 1 or months == 2:
        return 1
    else:
        return rabbit_pairs(months - 1, pairs_in_litter) + pairs_in_litter * rabbit_pairs(months - 2, pairs_in_litter)
print(rabbit_pairs(34, 5))