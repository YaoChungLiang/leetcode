import copy


def bubble_sort(arr):
	cnt = 0
	n = len(arr)
	for i in range(n):
		for j in range(0,n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
			#print(arr)
			cnt += 1
	#return arr,cnt



def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)/2
		L = arr[:mid]
		R = arr[mid:]
		merge_sort(L)
		merge_sort(R)
		i = j = k = 0
		
		while i < len(L) and j < len(R):
			if L[i] > R[j]:
				arr[k] = R[j]
				j += 1
			else:
				arr[k] = L[i]
				i += 1
			k += 1
		
		while i < len(L):
			arr[k] = L[i]
			k += 1
			i += 1
		while j < len(R):
			arr[k] = R[j]
			k += 1
			j += 1
			print(arr)
			

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and arr[j] > key:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key


def partition(arr, start, end):
	i = start - 1
	pivot = arr[end]
	for j in range(start, end):
		if arr[j] < pivot:
			i += 1
			arr[i] , arr[j] = arr[j] , arr[i]
	arr[i+1], arr[end] = arr[end], arr[i+1]
	return (i+1)


def quick_sort(arr,start, end):
	if start < end:
		partition_index = partition(arr,start, end)
		quick_sort(arr, start, partition_index-1)
		quick_sort(arr, partition_index+1, end)



def selection_sort(arr):
	
	for i in range(len(arr)):
		temp_index = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[temp_index]:
				temp_index = j
		arr[i], arr[temp_index] = arr[temp_index], arr[i]


def heapify(arr,n,i):
	largest = i  # maximun as root
	l = 2*i+1
	r = 2*i+2
	
	if l<n and arr[l] > arr[i]:
		largest = l
	if r<n and arr[largest] < arr[r]:
		largest = r

	if largest != i :
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
		print(arr)


def heap_sort(arr):
	n = len(arr)
	# build a maxheap
	for i in range(n,-1,-1):
		heapify(arr,n,i)
	# extract heap one by one
	for i in range(n-1,0,-1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr,i,0)


if  __name__ == '__main__':
	arr = [12,9,6,2,10]
	temp_arr = copy.deepcopy(arr)
	#######          bubble sort          ###################
	bubble_sort(temp_arr)
	print(temp_arr)
	#res_arr, cnt = bubble_sort(arr)
	#print("bubble_sort {} times".format(cnt))

	######           merge sort           ##################
	temp_arr = copy.deepcopy(arr)
	merge_sort(temp_arr)
	print(temp_arr)
	
	######           insertion sort       ##################

	temp_arr = copy.deepcopy(arr)
	insertion_sort(temp_arr)
	print(temp_arr)
	
	######           quick sort           ################
	
	temp_arr = copy.deepcopy(arr)
	print(temp_arr)
	n = len(temp_arr)
	quick_sort(temp_arr,0,n-1)
	print(temp_arr)

	######           selection sort       #################
	temp_arr = copy.deepcopy(arr)
	selection_sort(temp_arr)
	print(temp_arr)
	

	######            heap sort           #################
	temp_arr = copy.deepcopy(arr)
	heap_sort(temp_arr)
	print(temp_arr)


