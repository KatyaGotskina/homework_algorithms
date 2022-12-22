# Сложность алгоритма O(n ** 2)

def minDistance(s1: str, s2: str) -> int:
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)] # за столбцы отвечает s2
    # Пример:
    for i in range(len(dp)):     #   '' c a t
        dp[i][0] = i             # '' 0 1 2 3
    for j in range(len(dp[0])):  # h  1 0 0 0
        dp[0][j] = j             # i  2 0 0 0

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if s1[i] == s2[j]: # Если буквы одинаковые, считаем, что их нет
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1 # Пример:  
    return dp[-1][-1]                                          # Что быстрее: 'cat' -> '' или 'ca' -> 'h'?
