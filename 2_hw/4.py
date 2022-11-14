#  Перебираю пары и запоминаю наибльшее значение пары. Сложность алгоритма O (n**2)

def maxScoreSightseeingPair(values) -> int:
    maximum = 0 # Максимальная оценка пары 

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            maximum = max(maximum, values[i] + values[j] + i - j)

    return maximum
