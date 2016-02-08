def sum_inplace(numbers):
    pos_total = 0
    neg_total = 0
    for n in numbers:
        if n >= 0:
            pos_total += n
        else:
            neg_total += n
    print 'negative and positive sums are:', neg_total, pos_total
