# Создаю функцию, которая генерирует список по инструкции, данной в условии задачи, и возвращает 
# его максимальный элемент. Сначала создается  массив, состоящий из нулей (Я думаю, что заполнять массив
# можно любыми элементами, поскольку главная цель в том, чтобы индекс массива существовал при обращении к нему, мы все равно изменим 
# сам элемент. В таком случае необходимо прописать, что элемент под индексом 0 всегда равен 0), который в дальнейшем 
# заполняется в соответствии с выполнением условий.
# Сложность алгоритма O ( n )

def getMaximumGenerated(n: int) -> int:  
    nums = [0] * (n + 1)  # Длина списка по условию n + 1
    nums[1] = 1
    for i in range(1, len(nums) // 2):   # Заполнение списка
        if 2 <= 2 * i <= n:
            nums[2 * i] = nums[i]
        if 2 <= 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]
    return max(nums)    # Возвращает максимальный элемент в списке