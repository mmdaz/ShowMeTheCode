import itertools
import statistics



def process_purchases(purchases):
	min_, max_, avg = itertools.tee(purchases, 3)
	return min(min_), max(max_), statistics.median(avg)

test_list = [1, 2, 3, 4]
print(process_purchases(test_list))
