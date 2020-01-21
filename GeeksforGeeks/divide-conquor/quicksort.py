def quickSort(lis,first,last):
	if first < last:
		splitpoint = partition(lis,first,last)
		quickSort(lis, first, splitpoint-1)
		quickSort(lis, splitpoint+1, last)

def partition(lis,first,last):
	pivotvalue = lis[first]
	leftmark = first+1
	rightmark = last

	done = False
	while not done:
		while leftmark <= rightmark and lis[leftmark] <= pivotvalue:
			leftmark += 1

		while leftmark <= rightmark and lis[rightmark] >= pivotvalue:
			rightmark -= 1

		if leftmark > rightmark:
			done = True
		else:
			lis[leftmark], lis[rightmark] = lis[rightmark], lis[leftmark]

	lis[first], lis[rightmark] = lis[rightmark], lis[first]
	return rightmark

lis = [54,26,93,17,77,31,44,55,20]
first, last = 0, len(lis) - 1
quickSort(lis, first, last)
print(lis)
