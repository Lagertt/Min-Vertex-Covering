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

def generate_random_graph(n):
    # Генерация случайного графа с n вершинами
    graph = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Включаем ребро с вероятностью 0.5 (можно настроить по желанию)
            if random.choice([True, False]):
                graph.append((i, j))
    return n, graph

#переборный алгоритм
def find_vertex_cover(n, graph):
    min_vertex_cover_size = float('inf')
    min_vertex_cover = []

    start_time1 = time.process_time()  # Засекаем процессорное время начала выполнения

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

    end_time1 = time.process_time()  # Засекаем процессорное время окончания выполнения
    execution_time = end_time1 - start_time1

    return min_vertex_cover_size, min_vertex_cover, execution_time

# Приближенный алгоритм
def approxAlg(n, graph):
    start_time2 = time.process_time()  # Засекаем процессорное время начала выполнения
    result = []  # список для хранения вершинного покрытия
    graph_matrix = [[0] * n for _ in range(n)]  # Создаем нулевую матрицу смежности

    for edge in graph:
        graph_matrix[edge[0] - 1][edge[1] - 1] = 1
        graph_matrix[edge[1] - 1][edge[0] - 1] = 1

    while any(any(x == 1 for x in row) for row in graph_matrix):  # пока в графе есть непокрытые ребра
        edge_found = False
        # Шаг 1: Выбрать произвольное ребро
        for i in range(n):
            for j in range(n):
                if graph_matrix[i][j] == 1:
                    edge_found = True
                    # Шаг 2: Добавить к результату оба конца этого ребра
                    result.append(i + 1)
                    result.append(j + 1)
                    # Шаг 3: Удалить все ребра, инцидентные этим вершинам
                    for k in range(n):
                        graph_matrix[i][k] = 0
                        graph_matrix[k][i] = 0
                        graph_matrix[j][k] = 0
                        graph_matrix[k][j] = 0
                    break  # Перейти к следующей итерации
        if not edge_found:
            break  # Если не найдено ребро, выходим из цикла

    end_time2 = time.process_time()  # Засекаем процессорное время окончания выполнения
    execution_time_approx = end_time2 - start_time2
    return len(set(result)), list(set(result)), execution_time_approx # возвращаем результат

# Жадный алгоритм
def greedyAlg(n, graph):
    start_time3 = time.process_time()  # Засекаем процессорное время начала выполнения
    result = []  # список для хранения вершинного покрытия
    graph_matrix = [[0] * n for _ in range(n)]  # Создаем нулевую матрицу смежности

    for edge in graph:
        graph_matrix[edge[0] - 1][edge[1] - 1] = 1
        graph_matrix[edge[1] - 1][edge[0] - 1] = 1

    while any(any(x == 1 for x in row) for row in graph_matrix):  # пока в графе есть непокрытые ребра
        max_degree = 0  # переменная для хранения максимальной степени вершины
        max_vertex = None  # переменная для хранения вершины с максимальной степенью

        for i in range(n):  # проходим по всем вершинам графа
            degree = 0  # переменная для хранения степени текущей вершины
            for j in range(n):  # проходим по всем вершинам, инцидентным текущей
                if graph_matrix[i][j] == 1:  # если между текущими вершинами есть ребро
                    degree += 1  # увеличиваем степень текущей вершины на 1
            if degree > max_degree:  # если степень текущей вершины больше максимальной
                max_degree = degree  # обновляем значение максимальной степени
                max_vertex = i  # обновляем значение вершины с максимальной степенью

        if max_vertex is None:  # если не удалось найти вершину с максимальной степенью
            end_time3 = time.process_time()  # Засекаем процессорное время окончания выполнения
            execution_time_greedy = end_time3\
                             - start_time3
            return len(result), result, execution_time_greedy # возвращаем текущий результат

        result.append(max_vertex + 1)  # добавляем вершину с максимальной степенью к результату

        for i in range(n):  # проходим по всем вершинам, инцидентным выбранной вершине
            if graph_matrix[max_vertex][i] == 1:  # если есть ребро между выбранной и текущей вершиной
                graph_matrix[max_vertex][i] = 0  # удаляем это ребро из графа
                graph_matrix[i][max_vertex] = 0  # удаляем это ребро из графа (граф неориентированный)

    end_time4 = time.process_time()  # Засекаем процессорное время окончания выполнения
    execution_time_greedy = end_time4 - start_time3
    return len(result), result, execution_time_greedy # возвращаем результат

if __name__ == "__main__":
    choice = input("Источник ввода (1.file/2.random): ").lower()

    if choice == '1':
        filename = input("Введите имя файла с матрицей смежности: ")
        n, graph = read_graph_from_file(filename)
    elif choice == '2':
        n = int(input("Введите количество вершин в графе: "))
        n, graph = generate_random_graph(n)

    # Результаты метода полного перебора
    result_size, result_vertex_cover, execution_time = find_vertex_cover(n, graph)
    print("\nМетод полного перебора:")
    print("Размер вершинного покрытия:", result_size)
    print("Вершины вершинного покрытия:", result_vertex_cover)
    print("Время выполнения:", execution_time, "секунд")

    # Результаты приближенного алгоритма
    result_size_approx, result_vertex_cover_approx, execution_time_approx = approxAlg(n, graph.copy())
    print("\nПриближенный алгоритм:")
    print("Размер вершинного покрытия:", result_size_approx)
    print("Вершины вершинного покрытия:", result_vertex_cover_approx)
    print("Время выполнения:", execution_time_approx, "секунд")

    # Результаты жадного алгоритма
    result_size_greedy, result_vertex_cover_greedy, execution_time_greedy = greedyAlg(n, graph.copy())
    print("\nЖадный алгоритм:")
    print("Размер вершинного покрытия:", result_size_greedy)
    print("Вершины вершинного покрытия:", result_vertex_cover_greedy)
    print("Время выполнения:", execution_time_greedy, "секунд")
