import numpy as np


def parse_text(filename):
	arr = []

	with open(filename, 'r') as f:
		for line in f:
			temp_str = line.rstrip()
			temp_arr = temp_str.split(" ")
			# print temp_arr
			# TODO: readup on map()
			temp_arr = map(int, temp_arr)
			arr.append(temp_arr)

	last_row = len(arr) - 1
	elements_in_last = len(arr[last_row])
	# print elements_in_last

	for r in arr:
		# print len(r)
		add_zero = elements_in_last - len(r)
		for e in range(add_zero):
			r.append(0)

	# print arr
	return arr


if __name__ == "__main__":
	parse_text("test.txt")
