# Сложность алгоритма О(n ** 2)

def findLongestChain(pairs) -> int:
        pairs.sort()
        dp = [1] * len(pairs) # Будет содержать инф. о текущей длине цепочки на элементе

        for i in range(len(pairs)):               # Пример
            for j in range(i):                    # pairs = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10]]
                if pairs[j][1] < pairs[i][0]:     # dp [1, 1, 1, 1, 1, 1]
                    dp[i] = max(dp[i], dp[j] + 1) # dp [1, 2, 1, 1, 1, 1]
        return max(dp)                            # dp [1, 2, 2, 1, 1, 1]
                                                  # dp [1, 2, 2, 3, 1, 1]
                                                  # dp [1, 2, 2, 3, 3, 1]
                                                  # dp [1, 2, 2, 3, 3, 4]
