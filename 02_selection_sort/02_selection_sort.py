def findSmallest(arr):
	small_index = 0
	small_content = arr[0]
	for i in range(1,len(arr)):
		if arr[i]<small_content:
			small_index = i
			small_content = arr[i] # used for comparison
	return small_index

def selection_sort(arr):
	new_arr = []
	for i in range(len(arr)):
		new_arr.append(arr.pop(findSmallest(arr)))
	return new_arr

arr = [4,5,13,1,98]
print(selection_sort(arr))