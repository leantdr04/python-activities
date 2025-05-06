"""Sorting Algorithm program --by Dela Rosa, Leant Nathaniel I."""
#----------BUBBLE SORT-------------------
# Defining Bubble Sort function
def BubbleSort(elements: list):
	for i in range(0, len(elements)-1):                  #elements in array is sorted per loop
		print("Iteration #", i + 1)                            #Displays Number of Iteration per loop
		swapped = False
		for j in range(0, len(elements)-i-1):
			if elements[j] > elements[j+1]:                            #Tells the program to swap position if
				elements[j], elements[j+1] = elements[j+1], elements[j]  #current index is greater than next element
				swapped = True
			print(arr)                          #Display arrays per loop to show first iteration up to Final output
		if not swapped:                           #Condition statement when swapping did not occur.
			break
		print()
	return elements

print("\n ~ Bubble Sorting Algorithm ~\n")
arr = input("Input Five numbers to sort (separated by spaces):\n  > ")    #User inputs 5 values
try:
	arr = [float(x) for x in arr.strip().split()]                    #Converts 'array' variable from string to list
	if len(arr) != 5:                                                #Tells program to accept 5 values only
		print("INPUT ERROR: Input exact 5 numbers...\n")            #Displays Error when input values exceed 5 values
	else:
		print("Your array: ",arr)
		print("\n** Sorted Array:",BubbleSort(arr))             #Initiates BubbleSort() function and prints final output
except ValueError:                                              #Displays Error when user inputs non-integers
	print("INPUT ERROR: Enter numbers only...\n\n")

#---------INSERTION SORT-----------------
# Defining Insertion Sort function
def InsertionSort(elements: list):
	if len(elements) > 1:
		for i in range(1, len(elements)):    #Loop starts at second element
			n = elements[i]                     #element at current index position will be in variable 'n'
			j = i-1                         #variable 'j' as the element before current element
			while j>=0 and n<elements[j]:
				elements[j+1] = elements[j]
				j -= 1                          #The element that was replaced in position will lower in position
			elements[j+1] = n             # Element at 'j + 1' will be current element in variable 'n'
			print(arr)                  #Displays the arrays per loop

print("\n ~ Insertion Sorting Algorithm ~\n")
arr = input("Input Five numbers to sort (separated by spaces):\n  > ")
try:                                                         #Same blocks of code for User Input process
	arr = [float(x) for x in arr.strip().split()]
	if len(arr) != 5:
		print("INPUT ERROR: Input exact 5 numbers...\n")
	else:
		print("Your array: ",arr)
		print("\n** Sorted Array:",InsertionSort(arr))       #Initiates InsertionSort() and prints final output
except ValueError:
	print("INPUT ERROR: Enter numbers only...\n\n")

#---------SELECTION SORT-----------------
# Defining Selection Sort function
def SelectionSort(elements: list):
	for i in range(0, len(elements) - 1):               #Loop starts at first element
		min_i = i                                            #Variable defined as 'min_i' assumed to be lowest number in array
		for j in range(i + 1, len(elements)):
			if elements[j] < elements[min_i]: min_i = j              #element in 'j' overwrites lowest number when element in j is lesser than element in min_i
		elements[i], elements[min_i] = elements[min_i], elements[i]   #Element in i replaces position to element in min_i and lowest number replace element in position i
		print(arr)                                       #Displays the arrays per iteration
	return elements

print("\n ~ Selection Sorting Algorithm ~\n")
arr = input("Input Five numbers to sort (separated by spaces):\n  > ")
try:                                                        #Same blocks of code for User Input process
	arr = [float(x) for x in arr.strip().split()]
	if len(arr) != 5:
		print("INPUT ERROR: Input exact 5 numbers...\n")
	else:
		print("Your array: ",arr)
		print("\n** Sorted Array:",SelectionSort(arr))      #Initiates SelectionSort() and prints final output
except ValueError:
	print("INPUT ERROR: Enter numbers only...\n\n")

#---------MERGE SORT-----------------
# Defining Merge Sort function
def MergeSort(elements: list):
	if len(elements) > 1:
		arr1 = MergeSort(elements[:int(len(elements)//2)])
		arr2 = MergeSort(elements[int(len(elements)//2):])
		print(arr1,"\t\t",arr2)
		i, j, elements = 0, 0, []
		while i != len(arr1) and j != len(arr2):  # while loop stops when either one of arrays has no elements to be placed in variable 'elements'
			if arr1[i] <= arr2[j]:
				elements.append(arr1[i])  # append() function to use for adding specified element to arr1
				i += 1
			else:
				elements.append(arr2[j])  # append() function to use for adding specified element to arr2
				j += 1
		else:
			if len(arr1) == i:
				elements.extend(arr2[j:])  # extend() function to merge remaining elements to variable 'elements'
			else:
				elements.extend(arr1[i:])
	return elements

print("\n ~ Merge Sorting Algorithm ~\n")
arr = input("Input Five numbers to sort (separated by spaces):\n  > ")
try:                                                       #Same blocks of code for User Input process
	arr = [float(x) for x in arr.strip().split()]
	if len(arr) != 5:
		print("INPUT ERROR: Input exact 5 numbers...\n")
	else:
		print("Your array: ",arr)
		print("First array: Second Array:")              #Initiates MergeSort() and displays the First and Second-
		print("\n** Sorted Array:",MergeSort(arr))       #array to be merged and sorted as Final output
except ValueError:
	print("INPUT ERROR: Enter numbers only...\n\n")

#---------QUICK SORT-----------------
# Defining Quick Sort function
def QuickSort(elements: list):
	if len(elements) > 1:
		pivot, i = elements[len(elements) - 1], -1             #Identifies the value of pivot and 'i'
		for j in range(0, len(elements)):
			if elements[j] <= pivot:                     #When value of element in 'j' is less than or equal to value of pivot,
				i += 1                                              #value of variable 'i' adds to 1
				elements[i], elements[j] = elements[j], elements[i]  # Elements in index j and i will swap

		arr1 = QuickSort(elements[:i])                          #Lower numbers than pivot will be in left of array
		arr2 = QuickSort(elements[i + 1:])                          #Higher numbers than pivot will be i right side of array

		elements = arr1 + [pivot] + arr2            #Defines the variable 'element' with sorted array containing arr1, pivot, and arr2, respectively.
		print(f"\t{arr1} \t\t {[pivot]} \t\t {arr2}")     # Displays elements during iterations and partitioning
	return elements

print("\n ~ Quick Sorting Algorithm ~\n")
arr = input("Input Five numbers to sort (separated by spaces):\n  > ")
try:                                                     #Same blocks of code for User Input process
	arr = [float(x) for x in arr.strip().split()]
	if len(arr) != 5:
		print("INPUT ERROR: Input exact 5 numbers...\n")
	else:
		print("Your array: ",arr)
		print("First array:  Pivot:  Second Array:")
		print("\n** Sorted Array:",QuickSort(arr))      # Initiates SelectionSort() and displays sorted array
															#containing arr1, pivot, and arr2, respectively.
except ValueError:
	print("INPUT ERROR: Enter numbers only...\n\n")