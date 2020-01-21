def mergeSort(lis):
	if len(lis) > 1:
		print("Splitting  ", lis)
		mid = len(lis) // 2
		lefthalf = lis[:mid]
		righthalf = lis[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		print ("Merging    ", lis)
		i, j, k = 0, 0, 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				lis[k]=lefthalf[i]
				i += 1
			else:
				lis[k]=righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf):
			lis[k]=lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf):
			lis[k]=righthalf[j]
			j += 1
			k += 1

	else:
		print("can't split",lis)

if __name__ == '__main__':
	lis = [54,26,93,17,77,31,44,55,20]
	mergeSort(lis)
	print("\nfinal answer", lis)
