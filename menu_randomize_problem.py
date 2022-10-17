from itertools import permutations


def permute_options():
    maximum = 0
    for subset in permutations(combination_options, menu_options):
        dist = 0
        for i in range(menu_options):
            if i + 1 < menu_options:
                dist = dist + graph.get((subset[i], subset[i + 1]), graph.get((subset[i + 1], subset[i]), 0))
            else:
                dist = dist + graph.get((subset[i], subset[0]), graph.get((subset[0], subset[i]), 0))
        if dist > maximum:
            maximum = dist
            max_combinations = subset[:]


def combine_options():
    combination_options = []
    for i in graph.keys():
        if i[0] not in combination_options:
            combination_options.append(i[0])
        if i[1] not in combination_options:
            combination_options.append(i[1])
    combination_options.sort()


if __name__ == '__main__':
    global max_combinations
    global combination_options

    menu_options = int(input())
    options_differences = int((menu_options * (menu_options - 1)) / 2)
    graph = {}
    for _ in range(options_differences):
        x, y, value = input().split()
        value = int(value)
        graph[(x, y)] = value
    combine_options()
    permute_options()
    for i in max_combinations:
        print(i, end=" ")
