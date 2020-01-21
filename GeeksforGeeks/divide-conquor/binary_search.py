from math import ceil

def binary_search(low, high, lis, item):
	mid = ceil((low+high)/2)
	if lis[mid] == item:
		return mid
	elif lis[mid] > item:
		print("search in ",lis[:mid])
		return binary_search(low, mid-1, lis, item)
	else:
		print("search in ",lis[mid+1:])
		return binary_search(mid+1, high, lis, item)

if __name__ == '__main__':
	lis = [1,9,4,7,3,15,21]
	sorted_lis = sorted(lis)
	item_to_search = 21
	low = 0
	high = len(lis) - 1
	print("searching", item_to_search, "in", sorted_lis)
	index = binary_search(low, high, sorted_lis, item_to_search)
	print("item found at index", index)