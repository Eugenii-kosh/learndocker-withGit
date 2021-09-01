import sys

llist = []
lastD = 0

with open('./logs/logs.txt', 'r', encoding='utf-8') as file:
    for f in file:
        if '\n' in f:
            f = f[0:-1]
        llist.append(f)
    file.close

if len(llist) == 0:
    pass
    with open('./logs/logs.txt', 'a', encoding='utf-8') as file:
        for i in range(1, 6):
            file.write(str(i) + '\n')
        file.close
        print(llist)
else:
    with open('./logs/logs.txt', 'a', encoding='utf-8') as file:
        for i in range(int(llist[-1]) + 1, int(llist[-1]) + 6):
            file.write(str(i) + '\n')
        file.close
        print(llist)
