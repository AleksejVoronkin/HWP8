data = [i.split() for i in open("t.txt", "r", encoding = 'utf-8')]
print(data)
famil = input('искомая Фамилия: ')
with open('t.txt', 'a') as f:
    for i in data:
        if i != famil:
            del [i]
print(data)


