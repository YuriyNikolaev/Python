# selection_sort.py
#
def findSmallest(arr):
	"""Поиск наименьшего элемента массива """
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	""" Функция сортировки выбором. Сортирует массив """
	newArr = []
	# находит наименьший элемент в массиве
	# и добавляет его в новый массив
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5, 3, 6, 2, 10]))
#print selectionSort([5, 3, 6, 2, 10])
