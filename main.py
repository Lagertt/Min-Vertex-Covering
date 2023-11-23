import random 
from time import time
import copy

#         	Задача о вершинном покрытии минимальной мощности.
# Дано: число вершин в графе (n) и сам граф (неориентированный) в виде матрицы смежности.
# Получить: количество вершин в найденном вершинном покрытии, а также сам список вершин.

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        graph = [list(map(int, line.strip().split())) for line in lines[1:]]

    return n, graph

def generateGraph(n):
  graph = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if (i != j):
        if (i < j):
          graph[i][j] = int(random.choice([1, 0]))
        else:
          graph[i][j] = graph[j][i]
    
  return graph

# Полный перебор
def fullSearchAlg(n, graph):
  def is_vertex_cover(graph, vertices):
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 1 and i not in vertices and j not in vertices:
          return False
    return True

  result = []
  min_size = n

  for i in range(2 ** n):
    vertex_set = []
    for j in range(n):
      if i & (1 << j):
        vertex_set.append(j)

    if is_vertex_cover(graph, vertex_set) and len(vertex_set) < min_size:
      result = vertex_set
      min_size = len(vertex_set)

  return len(result), result 

# Жадный алгоритм
def greedyAlg(n, graph):
  result = []
  while any(any(x == 1 for x in row) for row in graph): 
    max_degree = 0 
    max_vertex = None 

    for i in range(n): 
      degree = 0 
      for j in range(n): 
        if graph[i][j] == 1: 
          degree += 1 
      if degree > max_degree: 
        max_degree = degree 
        max_vertex = i

    if max_vertex is None: 
      return result 
    
    result.append(max_vertex) 

    for i in range(n):
      if graph[max_vertex][i] == 1: 
        graph[max_vertex][i] = 0
        graph[i][max_vertex] = 0

  return len(result), result 

#Приближенный алгоритм
def approxAlg(n, graph):  
  result = set()  # Множество вершин покрытия
    
  while any(any(x == 1 for x in row) for row in graph):
    u, v = random.sample(range(n), 2)

    result.add(u)
    result.add(v)

    for i in range(n):
      if graph[u][i] == 1:
        graph[u][i] = 0
        graph[i][u] = 0
      if graph[v][i] == 1:
        graph[v][i] = 0
        graph[i][v] = 0

  return len(result), list(result)


if __name__ == "__main__":
    choice = input("Источник ввода (1.file/2.random): ").lower()

    if choice == '1':
        filename = input("Введите имя файла с матрицей смежности: ")
        n, graph = read_graph_from_file(filename)
        print(graph)
    elif choice == '2':
        n = int(input("Введите количество вершин в графе: "))
        graph = generateGraph(n)

    # Результаты метода полного перебора
    start_time = time()  # Засекаем процессорное время начала выполнения
    result_size, result_vertex_cover = fullSearchAlg(n, copy.deepcopy(graph))
    end_time = time()  # Засекаем процессорное время окончания выполнения
    print("\nМетод полного перебора:")
    print("Размер вершинного покрытия:", result_size)
    print("Вершины вершинного покрытия:", result_vertex_cover)
    print("Время выполнения:", end_time - start_time, "секунд")

    # Результаты приближенного алгоритма
    start_time = time()  # Засекаем процессорное время начала выполнения
    result_size_approx, result_vertex_cover_approx = approxAlg(n, copy.deepcopy(graph))
    end_time = time()  # Засекаем процессорное время окончания выполнения
    print("\nПриближенный алгоритм:")
    print("Размер вершинного покрытия:", result_size_approx)
    print("Вершины вершинного покрытия:", result_vertex_cover_approx)
    print("Время выполнения:", end_time - start_time, "секунд")

    # Результаты жадного алгоритма
    start_time = time()  # Засекаем процессорное время начала выполнения
    result_size_greedy, result_vertex_cover_greedy = greedyAlg(n, copy.deepcopy(graph))
    end_time = time()  # Засекаем процессорное время окончания выполнения
    print("\nЖадный алгоритм:")
    print("Размер вершинного покрытия:", result_size_greedy)
    print("Вершины вершинного покрытия:", result_vertex_cover_greedy)
    print("Время выполнения:", end_time - start_time, "секунд")
