'''Сначала пишу функцию сортировки списка (как в лекции). Затем сортирую список, нахожу минимальную 
разницу с помощью одного цикла, затем в новый список добавляю списки из элементов с минимальной разницей с помощью
одного цикла. Сложность программы О(n*log n + n + n = n*log n'''


def merge(list1, list2):
    new_list = []
    i, j = 0, 0
    while i < len(list1) or j < len(list2):
        if i == len(list1):
            new_list.append(list2[j])
            j += 1
        elif j == len(list2):
            new_list.append(list1[i])
            i += 1
        else:
            if list1[i] < list2[j]:
                new_list.append(list1[i])
                i += 1
            else:
                new_list.append(list2[j])
                j += 1
    return new_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    part1 = arr[:len(arr)//2]
    part2 = arr[len(arr)//2:]
    return merge(merge_sort(part1), merge_sort(part2))


def minimumAbsDifference(arr):
    arr = merge_sort(arr)  # Сортировка списка
    maxx = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] < maxx:
            maxx = arr[i] - arr[i-1]  # Нахождение минимальной разницы
    result = []  # Создание пустого списка для добавления подходящих пар
    for j in range(1, len(arr)):
        if arr[j] - arr[j-1] == maxx:
            result.append([arr[j-1], arr[j]])  # Добавление подходящих пар
    return result
