
import numpy as np
import parser

#arr = \
#[ 
#	[3, 0, 0, 0],
#	[7, 4, 0, 0],
#	[2, 4, 6, 0],
#	[8, 5, 9, 3] 
#
#]
#
#new_arr = \
#[
#	[0, 0, 0, 0],
#	[0, 0, 0, 0],
#	[0, 0, 0, 0],
#	[0, 0, 0, 0],
#]

arr = parser.parse_text("test3.txt")
new_arr = []
for row in arr:
	new_r = []
	for element in range(len(arr[0])):
		new_r.append(0)
	new_arr.append(new_r)

print arr
print new_arr



for row in range(len(arr)-1, -1, -1):
	for col in range(len(arr[0])):
		# print arr[row][col]
		if row-1 < -1:
			break
		# hardcoded beware of 3
		if col + 1 == len(arr[0]):
			break
		if arr[row][col] == 0:
			break
		sum1 = 0
		sum2 = 0
		#TODO beware hardcode
		if row == len(arr)-1:
			sum1 = arr[row][col] + arr[row-1][col]
			sum2 = arr[row][col+1] + arr[row-1][col]
		else:
			sum1 = new_arr[row][col] + arr[row-1][col]
			sum2 = new_arr[row][col+1] + arr[row-1][col]

		print "-----------"
		print str(sum1) + " | " + str(sum2)
		print "-----------"


		if sum1 > sum2:
			new_arr[row-1][col] = sum1
		else:
			new_arr[row-1][col] = sum2
	print "VVVVVVVVVVVVVVVVVVVVVVVV"
	print new_arr
	print "VVVVVVVVVVVVVVVVVVVVVVVV"
	#print(new_arr[1])
	#print(arr)



# print arr
print new_arr[0]
max = 0
for x in new_arr[0]:
	if x > max:
		max = x 
print max
# print arr[0][0]
# print arr[0][1] # right
# print arr[1][0] # down

# print len(arr) # 4 








