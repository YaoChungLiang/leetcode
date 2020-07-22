def Binary_search(arr,l,r,n):
	if n>arr[-1] or n<arr[0]:
		return -1
	if r >= l:
		mid = l + (r-l)/2
		if arr[mid] == n:
			return mid
		elif arr[mid] > n:
			return Binary_search(arr, 0 , mid-1, n)
		else:
			return Binary_search(arr, mid+1, r , n)
	else :
		return -1
		
	


if __name__ == "__main__":
	arr = [2,6,9,10,12]
	n = 0
	res_index =  Binary_search(arr,0,len(arr), n)
	if res_index != -1:
		print("result index is {}".format(res_index))
	else:
		print("No such value in the array")
