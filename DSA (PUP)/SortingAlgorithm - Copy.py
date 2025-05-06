"""Sorting Algorithm program --by Dela Rosa, Leant Nathaniel I."""

#Defining functions for Bubble Sorting

def BubbleSort(elements: list) -> list:
	for i in range(0, len(elements)-1):
		swapped = False
		for j in range(0, len(elements)-i-1):
			if elements[j] > elements[j+1]:
				elements[j], elements[j+1] = elements[j+1], elements[j]
				swapped = True
		if not swapped:
			break
	return elements


def InsertionSort(elements: list) -> list:
	if len(elements) > 1:
		for i in range(1, len(elements)):
			n = elements[i]
			j = i-1
			while j>=0 and n<elements[j]:
				elements[j+1] = elements[j]
				j -= 1
			elements[j+1] = n
	return elements


def SelectionSort(elements: list) -> list:
	for i in range(0, len(elements) - 1):
		min_i = i
		for j in range(i + 1, len(elements)):
			if elements[j] < elements[min_i]: min_i = j
		elements[i], elements[min_i] = elements[min_i], elements[i]
	return elements


def MergeSort(elements: list) -> list:
	if len(elements) > 1:
		arr1 = MergeSort(elements[:int(len(elements)//2)])
		arr2 = MergeSort(elements[int(len(elements)//2):])

		i, j, elements = 0, 0, []
		while i != len(arr1) and j != len(arr2):
			if arr1[i] <= arr2[j]:
				elements.append(arr1[i])
				i += 1
			else:
				elements.append(arr2[j])
				j += 1
		else:
			if len(arr1) == i:
				elements.extend(arr2[j:])
			else:
				elements.extend(arr1[i:])

	return elements


def QuickSort(elements: list) -> list:
	if len(elements) > 1:
		pivot, i = elements[len(elements) - 1], -1
		for j in range(0, len(elements)):
			if elements[j] <= pivot:
				i += 1
				elements[i], elements[j] = elements[j], elements[i]

		arr1 = QuickSort(elements[:i])
		arr2 = QuickSort(elements[i + 1:])

		elements = arr1 + [pivot] + arr2

	return elements

def SortProgram():
	begin = True
	print("\n~ Sorting Algorithm ~\n")
	while begin:
		try:
			sort = int(input("Select which Sorting Algorithm you want to apply in your array:\n  1- Bubble Sort\n  "
							 "2- Insertion Sort\n  3- Selection Sort\n  4- Merge Sort\n  5- Quick Sort\n> ").strip())
			if sort == 1:
				print("\n ** BUBBLE SORT **\n")
			elif sort == 2:
				print("\n ** INSERTION SORT**\n")
			elif sort == 3:
				print("\n ** SELECTION SORT **\n")
			elif sort == 4:
				print("\n ** MERGE SORT **\n")
			elif sort == 5:
				print("\n ** QUICK SORT **\n")

		except ValueError:
			print(" Please select only among the choices...\n")
		else:
			sorting = True
			while sorting:
				algorithms = {1:BubbleSort, 2:InsertionSort, 3:SelectionSort, 4:MergeSort, 5:QuickSort}
				arr = input("Input Five numbers to sort (separated by spaces):\n  > ")
				try:
					arr = [float(x) for x in arr.strip().split()]

					if len(arr) != 5:
						print("INPUT ERROR: Input exact 5 numbers...\n")
					else:
						print(" ",algorithms[sort](arr),"\n")

						while True:
							try:
								retry = int(input("Try Again?\n  1- Exit\n  2- Same Sorting Algorithm\n  "
												  "3- Change Sorting Algorithm\n\n> "))
							except ValueError:
								print(" Please select only among the choices...\n")
							else:
								if retry == 1:
									begin = False
									sorting = False
								elif retry == 3:
									sorting = False
								break

				except ValueError:
					print("INPUT ERROR: Enter numbers only...\n\n")

SortProgram()