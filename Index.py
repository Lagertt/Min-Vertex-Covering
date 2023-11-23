#         	Задача о вершинном покрытии минимальной мощности.
# Дано: число вершин в графе (n) и сам граф (неориентированный) в виде матрицы смежности.
# Получить: количество вершин в найденном вершинном покрытии, а также сам список вершин.

# Жадный алгоритм
def greedyAlg(n, graph):
  result = [] # список для хранения вершинного покрытия
  while any(any(x == 1 for x in row) for row in graph): # пока в графе есть непокрытые ребра
    max_degree = 0 # переменная для хранения максимальной степени вершины
    max_vertex = None # переменная для хранения вершины с максимальной степенью

    for i in range(n): # проходим по всем вершинам графа
      degree = 0 # переменная для хранения степени текущей вершины
      for j in range(n): # проходим по всем вершинам, инцидентным текущей
        if graph[i][j] == 1: # если между текущими вершинами есть ребро
          degree += 1 # увеличиваем степень текущей вершины на 1
      if degree > max_degree: # если степень текущей вершины больше максимальной
        max_degree = degree # обновляем значение максимальной степени
        max_vertex = i # обновляем значение вершины с максимальной степенью

    if max_vertex is None: # если не удалось найти вершину с максимальной степенью
      return result # возвращаем текущий результат
    
    result.append(max_vertex) # добавляем вершину с максимальной степенью к результату

    for i in range(n): # проходим по всем вершинам, инцидентным выбранной вершине
      if graph[max_vertex][i] == 1: # если есть ребро между выбранной и текущей вершиной
        graph[max_vertex][i] = 0 # удаляем это ребро из графа
        graph[i][max_vertex] = 0 # удаляем это ребро из графа (граф неориентированный)

  return len(result), result # возвращаем результат

#Приближенный алгоритм
def approxVertexCover(n, graph):
    result = []  # список для хранения вершинного покрытия
    while any(any(x == 1 for x in row) for row in graph):  # пока в графе есть непокрытые ребра
        edge_found = False
        # Шаг 1: Выбрать произвольное ребро
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    edge_found = True
                    # Шаг 2: Добавить к результату оба конца этого ребра
                    result.append(i)
                    result.append(j)
                    # Шаг 3: Удалить все ребра, инцидентные этим вершинам
                    for k in range(n):
                        graph[i][k] = 0
                        graph[k][i] = 0
                        graph[j][k] = 0
                        graph[k][j] = 0
                    break  # Перейти к следующей итерации
        if not edge_found:
            break  # Если не найдено ребро, выходим из цикла
return len(set(result)), list(set(result))  # возвращаем результат


n = [5, 5, 6, 8, 10] # количество вершин в графе

# матрица смежности графа
graphs = [
  [[0, 1, 1, 0, 0], [1, 0, 1, 1, 0], [1, 1, 0, 1, 1], [0, 1, 1, 0, 1], [0, 0, 1, 1, 0]],
  [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0]],
  [[0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 0, 1, 1, 0]],
  [[0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1], [0, 0 ,1 ,1 ,0 ,0 ,1 ,0], [0 ,0 ,0 ,1 ,1 ,1 ,0 ,1], [0 ,0 ,0 ,0 ,1 ,0 ,1 ,0]],
  [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 0], [0, 0 ,1 ,1 ,0 ,0 ,1 ,0 ,1 ,1], [0 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1], [0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1], [0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1], [0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0]]
         ]

for index, graph in enumerate(graphs):
  result = greedyAlg(n[index], graph) # вызываем функцию для поиска вершинного покрытия
  print(result) # выводим результат
