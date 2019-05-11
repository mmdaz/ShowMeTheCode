import itertools
# import statistics



def process_purchases(purchases):
	# creates two copies of this list and pass it to variables.
	min_, max_ = itertools.tee(purchases, 2)
	return min(min_), max(max_)

test_list = [1, 2, 3, 4]
print(process_purchases(test_list))


def test_corotin():
	a = 0
	while True:
		a += 1
		yield a

for a in test_corotin():
	print(a)