float_to_int = lambda e: [[float(x), int(x)][int(x) == float(x)] for x in e]


def BubbleSorter(elements: list) -> list:
	for i in range(0, len(elements)-1):
		swapped = False
		for j in range(0, len(elements)-i-1):
			if elements[j] > elements[j+1]:
				elements[j], elements[j+1] = elements[j+1], elements[j]
				swapped = True
		if not swapped:
			break
	return elements


def InsertionSorter(elements: list) -> list:
	if len(elements) > 1:
		for i in range(1, len(elements)):
			n = elements[i]
			j = i-1
			while j>=0 and n<elements[j]:
				elements[j+1] = elements[j]
				j -= 1
			elements[j+1] = n
	return elements


def SelectionSorter(elements: list) -> list:
	for i in range(0, len(elements) - 1):
		min_i = i
		for j in range(i + 1, len(elements)):
			if elements[j] < elements[min_i]: min_i = j
		elements[i], elements[min_i] = elements[min_i], elements[i]
	return elements


def MergeSorter(elements: list) -> list:
	if len(elements) > 1:
		arr1 = MergeSorter(elements[:int(len(elements)//2)])
		arr2 = MergeSorter(elements[int(len(elements)//2):])

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


def QuickSorter(elements: list) -> list:
	if len(elements) > 1:
		pivot, i = elements[len(elements) - 1], -1
		for j in range(0, len(elements)):
			if elements[j] <= pivot:
				i += 1
				elements[i], elements[j] = elements[j], elements[i]

		arr1 = QuickSorter(elements[:i])
		arr2 = QuickSorter(elements[i + 1:])

		elements = arr1 + [pivot] + arr2

	return elements


def main():
	_start = True
	while _start:
		try:
			print("Sorter Algorithm\n")
			sort = int(input("\nChoose what Sorting Algorithm you want to use:\n\t1 - Bubble Sort\n\t2 - Insertion Sort\n\t3 - Selection Sort\n\t4 - Merge Sort\n\t5 - Quick Sort\n\n> ").strip())
		except ValueError:
			print("Choose only those in choices!")
		else:
			_sorting = True
			while _sorting:
				_sorting_algorithms = {1:BubbleSorter, 2:InsertionSorter, 3:SelectionSorter, 4:MergeSorter, 5:QuickSorter}
				print(_sorting_algorithms[sort](float_to_int(input("Input list of numbers (separated by spaces):\n\t> ").strip().split(" "))))
				while True:
					try:
						_again = int(input("Try Again?\n\t1 - Exit\n\t2 - Same Sorting Algorithm\n\t3 - Change Sorting Algorithm\n\n> "))
					except ValueError:
						print("Choose only those in choices!")
					else:
						if _again == 1:
							_start = False
							_sorting = False
						elif _again == 3:
							_sorting = False
						break


if __name__ == "__main__":
	main()