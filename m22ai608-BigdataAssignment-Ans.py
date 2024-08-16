import random   #Returns a random number 
import sys      # provides the name of the existing python modules
import time     


def kthOrderStatistic(k, size, arr):
	if k < 0 or k >= size:     #if size less than 0 or greater than length of array it will return -1
		return -1

	def custom_partition(low, high):   #low,right indicates values are custom_partitioning according ASC & DSC order
		random_piv_ind = random.randint(low, high)  # quick_selecting Random num
		selcted_pivot_val = arr[random_piv_ind]  # random_piv_ind accessing elements from selcted_pivot_val in Array and used for custom_partitioning.
		arr[random_piv_ind], arr[high] = arr[high], arr[random_piv_ind] 
		store_index = low #initial position where elements smaller than the pivot value will be placed.
		for i in range(low, high):
			if arr[i] < selcted_pivot_val:
				arr[i], arr[store_index] = arr[store_index], arr[i]  #This line swaps the element at index i with the element at the current store_index.
				store_index += 1  #This increments the store_index by 1 to indicate that a smaller element has been placed at its position.
		arr[store_index], arr[high] = arr[high], arr[store_index]  #swaps the pivot element ( high) with the element at the final store_index
		return store_index

	def quick_select(low, high, k_small):   #k:the target position of the kth order statistic.
		print('values.....', low, high, k_small)
		print(arr)
		if low == high: 
			return arr[low]   # If the range has reduced to a single element, the function returns that element.
		random_piv_ind = custom_partition(low, high)  #partition the array arr based on a randomly selected pivot element.
		if k_small == random_piv_ind: 
			return arr[k_small]  #pivot element is the kth order statistic. Here it will return k index.
		elif k_small < random_piv_ind:
			return quick_select(low, random_piv_ind - 1, k_small)  #kth order statistic lies within the left partition and range from low to random_piv_ind - 1 to find the kth order statistic in the left partition. 
		else:
			return quick_select(random_piv_ind + 1, high, k_small) # kth order statistic lies within the right partition and  range from random_piv_ind + 1 to high to find the kth order statistic in the right partition.
	return quick_select(0, size - 1, k)  # it initiates the initial recursive call to quick_select with the entire array range.


if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("Usage: python M22AI608.py K size arr[1] arr[2] ... arr[size]")
		sys.exit(1)

	k = int(sys.argv[1]) #k- order
	size = int(sys.argv[2]) # size of array
	args = sys.argv[3:] # collecing values except k and size
	arr = [int(arg) for arg in args]  # stores in array format

	ptime = time.process_time()  #records execution time
	print('process time', ptime)
	result = kthOrderStatistic(k, size, arr) 

	print("Kth Order Statistic:", result) #prints the obtained kth order statistic.


							###### REPORT ######
#1st 
##python .\m22ai608-BigdataAssignment-Ans.py 2 7 1 4 6 2 8 5 6

# process time 0.046875
# values..... 0 6 2
# [1, 4, 6, 2, 8, 5, 6]
# values..... 2 6 2
# [1, 2, 6, 6, 8, 5, 4]
# Kth Order Statistic: 4

#2nd
##python .\m22ai608-BigdataAssignment-Ans.py 5 7 1 4 6 2 8 5 6

# process time 0.046875
# values..... 0 6 2
# [1, 4, 6, 2, 8, 5, 6]
# values..... 0 6 5
# [1, 4, 6, 2, 8, 5, 6]
# values..... 1 6 5
# [1, 4, 6, 2, 8, 5, 6]
# values..... 5 6 5
# [1, 4, 2, 5, 6, 6, 8]
# values..... 5 5 5
# [1, 4, 2, 5, 6, 6, 8]
# Kth Order Statistic: 6

#3rd
##python .\m22ai608-BigdataAssignment-Ans.py 2 10 5 6 8 5 8 4 7 1 5 9

# process time 0.046875
# values..... 0 9 2
# [5, 6, 8, 5, 8, 4, 7, 1, 5, 9]
# values..... 0 8 2
# [5, 6, 8, 5, 8, 4, 7, 1, 5, 9]
# values..... 0 4 2
# [5, 5, 5, 4, 1, 6, 7, 8, 8, 9]
# Kth Order Statistic: 5