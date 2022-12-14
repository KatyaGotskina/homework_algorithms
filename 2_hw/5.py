# Решаю задачу с помощью динамического программирования. Создаю список, каждый элемент которого будет
# соответствовать количеству периодов плавного спуска акций, включающих элемент из изначального списка с таким же индексом.
#Сложность алгоритма O( n )

def getDescentPeriods(prices):
    dp = [1] * len(prices)   # изначальный список состоит из единиц, потому что списки, включающие только одно число,
                             # тоже являются периодами плавного спуска акций. ( Я про [1], [2], [3] в полученном prices [1, 3, 2])
    for i in range(1, len(dp)):
        if prices[i] - prices[i-1] == -1:
       		dp[i] += dp[i-1] 
    return sum(dp)     # ответом является сумма из получившегося списка, потому что каждый элемент созданного списка отвечает
                       # за количество периодов плавного спуска акций, включающих уникальный элемент из изначального списка, так что все 
                       # последовательности уникальны 

