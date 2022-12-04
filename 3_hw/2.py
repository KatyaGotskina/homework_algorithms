# Использую stack для обхода в глубину, прохожу все острова и и проверяю их на соседство с границей сетки,
# поскольку только при этом они не являются окруженными водой. 
# При некорректных координатах соседних клеток у острова устанавливаю флагу значение False, 
# Чтобы не учитывать остров при ответе. Сложность алгоритма O ( n ** 3 )

def numEnclaves(grid) -> int:
    counter = 0  # Количество островов, неконтактирующих с границей 
    flag = True  # Изначально флаг True 
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid [i][j] == 0 and  (i, j) not in visited:
                visited.add((i, j))
                stack = [(i, j)]
                while stack:
                    row, col = stack.pop()
                    for z, f in (row - 1,col), (row + 1, col), (row, col - 1), (row, col + 1):
                
                        if 0 <= z < len(grid) and 0 <= f < len(grid[0]) and grid[z][f] == 0 and (z,f) not in visited:
                            visited.add((z,f))
                            stack.append((z,f))
                        elif not (0 <= z < len(grid) and 0 <= f < len(grid[0])):
                            flag = False # не учитываем остров если координаты вокруг хотя бы 1 клетки острова
                            #выходят за рамки поля                        
                if flag:
                    counter += 1 # Увеличиваем counter, поскольку еще один остров нам подходит 
                flag = True  # Обновляем флаг 
    return counter
