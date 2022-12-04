# Использую stack для обхода в глубину, прохожу все острова и узнаю их площадь.
# При некорректных координатах соседних клеток у острова устанавливаю флагу значение False, 
# Чтобы не учитывать остров при ответе. Сложность алгоритма O ( n ** 3 )


def numEnclaves(grid) -> int:
    counter, area = 0, 0   # колво клеток, с которых нельзя выйти за границу и количество клеток в острове 
    flag = True    # Изначально флаг True
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid [i][j] == 1 and  (i, j) not in visited:
                visited.add((i, j))
                stack = [(i, j)]
                while stack:
                    area += 1
                    row, col = stack.pop()
                    for z, f in (row - 1,col), (row + 1, col), (row, col - 1), (row, col + 1):
                
                        if 0 <= z < len(grid) and 0 <= f < len(grid[0]) and grid[z][f] == 1 and (z,f) not in visited:
                            visited.add((z,f))
                            stack.append((z,f))
                        elif not (0 <= z < len(grid) and 0 <= f < len(grid[0])):
                            flag = False # не учитываем остров если координаты вокруг хотя бы 1 клетки острова
                            #выходят за рамки поля
                        
                if flag:
                    counter += area # Добавляем к counter количество клеток в только что рассмотренном острове 
                area = 0   
                flag = True
    return counter

