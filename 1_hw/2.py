'''Алгоритмом является последовательное выполнение операций изменения переменных. Сложность О(n)'''


def numberOfMatches(teams: int) -> int:
    matches = 0  # Cчетчик количества сыгранных матчей
    while teams != 1:
        if teams % 2 == 0:
            teams //= 2  # Объединение команд
            matches += teams
        else:
            teams = ((teams - 1) // 2) + 1  # Объединение команд
            matches += teams - 1
    return matches
