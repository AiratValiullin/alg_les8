# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random

def graph(n):

    lst = []
    for i in range(n):
        a = random.sample(range(0, n), random.randint(2, n))
        if i in a:
            a.pop(a.index(i))
        lst.append(a)

    return lst

c = graph(int(input('Введите количество вершин ')))
print(*c, sep='\n')

def dfs(graph, start):

    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        for nei in graph[current]:
            if not nei in visited:
                stack.append(nei)
        visited.append(current)
    return visited

dfs(c, 0)
print(dfs)