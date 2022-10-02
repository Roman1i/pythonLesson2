import random

def fill_list():
    print('Добавтье элемент в список или введите "stop"')

    n = ""
    nums = []

    while n != "stop":
        if n.isdigit():
            nums.append(int(n))
        n = input()
    return nums

def shuffle(list_):
    n = len(list_)
    newList = []
    for i in range(n):
        tmp = list_[random.randint(0, n - i - 1)]
        newList.append(tmp)
        list_.remove(tmp)
    return newList

print(shuffle(fill_list()))





