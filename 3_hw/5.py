# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Обходим в глубину, используя stack. Основная идея заключается в том, что в stack е хранится кортеж с элементом
# и сторокой, показывающей путь из вершины до данного элемента. Сложность алгоритма O ( n )
def binaryTreePaths(root):
    stack = [(root, '')]
    result = []   # список с путями до всех элементов

    while stack:
        cur_node, path = stack.pop()
        path += '->{}'.format(cur_node.val)

        if cur_node.left == None and cur_node.right == None:  # Проверка на листик
            result.append(path[2:])      # не учитываем первую стрелочку в строке
                
        if cur_node.left:
            stack.append((cur_node.left, path))
        
        if cur_node.right:
            stack.append((cur_node.right, path))
    return result