'''Алгоритм основывается на переборе значений и счете количества совпадений. Сложность О(n)'''


def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0  # счетчик
    # строку с драгоценными камнями переводим в список для удобной работы. Сложность этой операции О(n)
    jewels_types = list(jewels)
    for stone in stones:
        if stone in jewels_types:  # Проверяем наличие камней в списке
            count += 1
    return count
