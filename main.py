import random
import time

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        matrix = [list(map(int, line.strip().split())) for line in lines[1:]]

    # Преобразуем матрицу смежности в список рёбер
    graph = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1 or matrix[j][i] == 1:
                graph.append((i + 1, j + 1))

    return n, graph

def input_graph_from_keyboard():
    n = int(input("Введите количество вершин в графе: "))
    print("Введите матрицу смежности:")
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # Преобразуем матрицу смежности в список рёбер
    graph = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1 or matrix[j][i] == 1:
                graph.append((i + 1, j + 1))

    return n, graph

def generate_random_graph(n):
    # Генерация случайного графа с n вершинами
    graph = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Включаем ребро с вероятностью 0.5 (можно настроить по желанию)
            if random.choice([True, False]):
                graph.append((i, j))
    return n, graph

def find_vertex_cover(n, graph):
    min_vertex_cover_size = float('inf')
    min_vertex_cover = []

    start_time = time.time()  # Засекаем время начала выполнения

    for i in range(2**n):
        current_vertex_cover = []
        for j in range(n):
            if (i >> j) & 1:
                current_vertex_cover.append(j + 1)

        is_vertex_cover = True
        for edge in graph:
            if edge[0] not in current_vertex_cover and edge[1] not in current_vertex_cover:
                is_vertex_cover = False
                break

        if is_vertex_cover and len(current_vertex_cover) < min_vertex_cover_size:
            min_vertex_cover_size = len(current_vertex_cover)
            min_vertex_cover = current_vertex_cover

    end_time = time.time()  # Засекаем время окончания выполнения
    execution_time = end_time - start_time

    return min_vertex_cover_size, min_vertex_cover, execution_time

if __name__ == "__main__":
    choice = input("Выберите источник ввода (1.file/2.keyboard/3.random): ").lower()

    if choice == '1':
        filename = input("Введите имя файла с матрицей смежности: ")
        n, graph = read_graph_from_file(filename)
    elif choice == '2':
        n, graph = input_graph_from_keyboard()
    elif choice == '3':
        n = int(input("Введите количество вершин в графе: "))
        n, graph = generate_random_graph(n)
    else:
        print("Некорректный выбор.")
        exit()

    result_size, result_vertex_cover, execution_time = find_vertex_cover(n, graph)

    print("Размер вершинного покрытия:", result_size)
    print("Вершины вершинного покрытия:", result_vertex_cover)
    print("Время выполнения:", execution_time, "секунд")
