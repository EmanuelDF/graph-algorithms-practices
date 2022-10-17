from itertools import permutations, product


class Stack:
    def __init__(self):
        self.stack = []
        self.stack.append("Dummy")

    def read(self, stack_list):
        temp = stack_list.split()
        for i in temp:
            self.stack.append(i)

    def decide(self, args_list):
        parent = 1
        height = 0
        for i in args_list:
            if (self.stack[2 * parent]) == i:
                parent = 2 * parent
            else:
                parent = 2 * parent + 1
            height += 1
        return self.stack[parent + 2 ** height]


def search_first_amplitude(recognition_graph, vertices_traversed, query, vertices):
    visited_subgraph = []
    vertices_traversed.append(vertices)
    query.append(vertices)
    visited_subgraph.append(vertices)

    while query:
        j = query.pop(0)
        adjacent = recognition_graph[j]
        adjacent_nodes = []
        for m in adjacent:
            adjacent_nodes.append(m[0][0])
        for neighbor in adjacent_nodes:
            if neighbor not in vertices_traversed:
                vertices_traversed.append(neighbor)
                query.append(neighbor)
                visited_subgraph.append(neighbor)

    return visited_subgraph


def read_recognition_graph(recognition_vertices_quantity):
    recognition_graph = {}
    for _ in range(recognition_vertices_quantity):
        line = input().split()
        temp_list = [i.split(sep=",") for i in line[1:]]
        adjacency_list = [[i[0], int(i[1])] for i in temp_list]
        recognition_graph[line[0]] = adjacency_list
    return recognition_graph


def read_logistic_graph(logistics_vertices_quantity):
    logistic_graph = {}
    for _ in range(logistics_vertices_quantity):
        line = input().split()
        temp_list = [i.split(sep=",") for i in line[1:]]
        adjacency_dictionary = {}
        for i in temp_list:
            adjacency_dictionary[i[0]] = int(i[1])
        logistic_graph[line[0]] = adjacency_dictionary
    return logistic_graph


def read_coordinates(recognition_vertices_quantity):
    map_coordinate = {}
    for _ in range(recognition_vertices_quantity):
        line = input().split()
        temp_list = [i.split(sep=",") for i in line[1:]]
        xyz_list = [[int(i[0]), int(i[1]), int(i[2])] for i in temp_list]
        map_coordinate[line[0]] = xyz_list[0]
    return map_coordinate


def measure_cartesian_distance(point_a, point_b):
    return ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2 + (point_a[2] - point_b[2]) ** 2) ** 0.5


def execute_recognition(coordinate_map, recognition_graph):
    vertices_traversed_list = []
    total_vertices_list = []
    subgraph_list = []
    new_path_list = []
    sweep_graph(recognition_graph, subgraph_list, total_vertices_list, vertices_traversed_list)

    # Calculates Euclidean Distance
    subgraph_quantity = len(subgraph_list)
    if subgraph_quantity > 1:
        for j in range(len(subgraph_list)):
            r = product(subgraph_list[j], subgraph_list[j - 1])
            s = list(r)
            minimum = 99999999999
            vertices = None
            for t in s:
                d = measure_cartesian_distance(coordinate_map[t[0]], coordinate_map[t[1]])
                if d <= minimum:
                    minimum = d
                    vertices = [t[0], t[1]]
            vertices.sort()
            if vertices not in new_path_list:
                new_path_list.append(vertices)
        new_path_list.sort()
        for path in new_path_list:
            print("%s-%s" % (path[0], path[1]))
    else:
        print("No new paths needed.")


def sweep_graph(recognition_graph, subgraph_list, vertices_list, vertices_traversed_list):
    for j in recognition_graph:
        vertices_list.append(j)
    for j in vertices_list:
        if j not in vertices_traversed_list:
            q = []
            subgraph_list.append(search_first_amplitude(recognition_graph, vertices_traversed_list, q, j))


def execute_logistic(logistic_graph):
    minimum = 999999999999
    path = list(logistic_graph.keys())
    vertices = len(path)
    permutations_list = list(permutations(path[1:]))
    paths = []
    for i in permutations_list:
        temp = list(i)
        temp.append(path[0])
        paths.append(temp)
    for i in paths:
        length = 0
        for j in range(vertices):
            length += logistic_graph[i[j]].get(i[(j + 1) % vertices], 999999)
        if length < minimum:
            minimum = length
    if minimum <= 999999:
        print(minimum)
    else:
        print("Impossible!")


def execute_attack():
    tree = Stack()
    line = input()
    tree.read(line)
    line = input()
    while "end" not in line:
        param = line.split()
        gun = tree.decide(param)
        print(gun)
        line = input()


if __name__ == '__main__':
    mission = input()
    if mission == "R":
        vertices_quantity = int(input())
        map_coordinates = read_coordinates(vertices_quantity)
        graph = read_recognition_graph(vertices_quantity)
        execute_recognition(map_coordinates, graph)
    elif mission == "L":
        vertices_quantity = int(input())
        graph = read_logistic_graph(vertices_quantity)
        execute_logistic(graph)
    elif mission == "A":
        execute_attack()
    else:
        print("Inform the mission type:")

# Inputs

# R
# 4
# A 999,10,8
# B 1005,50,-20
# C 955,-25,15
# D 1019,-20,-7
# A B,1
# B
# C D,1
# D

# L
# 3
# A B,3 C,4
# B A,3 C,5
# C A,4 B,5

# A
# ? caça helicóptero blindado não blindado não míssil laser canhão metralhadora
# caça blindado
# caça não
# helicóptero blindado
# helicóptero não
# fim
