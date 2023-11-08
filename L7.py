import random

size1 = int(input("Введите размер матрицы M1: "))
M1 = []

for i in range(size1):
    row = []
    for j in range(size1):
        row.append(0)
    M1.append(row)

for i in range(size1):
    for j in range(i + 1, size1):
        M1[i][j] = M1[j][i] = random.randint(0, 1)

lists = [[] for _ in range(size1)]
for i in range(size1):
    for j in range(size1):
        if M1[i][j] == 1:
            lists[i].append(j)


def epth_first_search(G):
    def DFS(v):
        NUM[v] = True
        print(v, end=' ')

        for i in range(size_G):
            if G[v][i] == 1 and not NUM[i]:
                DFS(i)

    size_G = len(G)
    NUM = [False] * size_G

    if not NUM[0]:
        DFS(0)

def depth_first_search_iterative(adj_matrix):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices

    stack = [0]
    visited[0] = True
    print(0, end=' ')

    while stack:
        current_vertex = stack[-1]
        found = False

        for i in range(num_vertices):
            if adj_matrix[current_vertex][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = True
                print(i, end=' ')
                found = True
                break

        if not found:
            stack.pop()


def depth_first_search(adj_list):
    def DFS(vertex):
        visited[vertex] = True
        print(vertex, end=' ')

        for neighbor in adj_list[vertex]:
            if not visited[neighbor]:
                DFS(neighbor)

    num_vertices = len(adj_list)
    visited = [False] * num_vertices

    if not visited[0]:
        DFS(0)


print("Матрица смежности для M1:")
for row in M1:
    print(row)

print("\nСписок смежности для M1: ")
for i, verticles in enumerate(lists):
    print(f"Вершина {i}: {verticles}")

print("Результат обхода в глубину:")
epth_first_search(M1)

print("\nРезультат обхода в глубину для списка смежности:")
depth_first_search(lists)

print("\nРезультат обхода в глубину (без рекурсии):")
depth_first_search_iterative(M1)
