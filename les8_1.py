# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n = 19 # количество вершин
lst1 = []
k = 0

for i in range(n):
    lst = []
    for j in range(n):
        if j == k:
            lst.append(0)
        else:
            lst.append(1)
    k += 1
    lst1.append(lst)
print(*lst1, sep='\n' )

sum = 0
for i in lst1:
    for j in i:
        sum += j
print(f' Количество ребер (рукопожатий) = {int(sum/2)}')
