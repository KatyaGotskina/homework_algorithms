# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Проходим по связанному списку и записываем все значения в строковом виде в переменную. Затем переводим в 
# десятичный вид. Сложность алгоритма O ( n )
def getDecimalValue(head) -> int:
    s = ''
    while head:
        s += str(head.val)
        head = head.next
    return int(s, 2)