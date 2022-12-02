# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Использую очередь для обхода в ширину.Изменение глубины рассматриваемого объекта означает то, что мы
# уже получили данные о предыдущем уровне объектов, поэтому я добавляю среднее арифметическое в итоговый список 
# и обновляю переменные, для получения данных новой глубины. Сложность алгоритма O ( n )
def averageOfLevels(root):
    q = [(root, 0)]
    summ, depth = root.val, 0    # сумма значений элементов одной глубины, глубина 
    counter, result = 1, []      # Количество элементов одной глубины, итоговый список значений

    while q:
        cur_vertex, new_depth = q.pop(0)
        if new_depth > depth:    # Если глубина поменялась, то обновляем переменные и глубину
            depth = new_depth
            result.append(summ / counter)   # Добавляем среднее арифметическое в result 
            summ, counter = 0, 0
        summ += cur_vertex.val

        counter += 1
        if cur_vertex.left:
            q.append((cur_vertex.left, depth+1))

        if cur_vertex.right:
            q.append((cur_vertex.right, depth+1))

    result.append(summ / counter)   # Действие для последней итерации, поскольку после нее значение глубины не обновляется
    return result
