from itertools import permutations


def validate_possibilities(neighbor_cities, i, subset):
    global points, minimum_points
    if is_equivalent_distance(neighbor_cities, possibilities):
        if i < minimum_points:
            minimum_points = i
            points = subset
    neighbor_cities = []
    return neighbor_cities


def is_equivalent_distance(city_a, city_b):
    length_a = len(city_a)
    length_b = len(city_b)
    if length_a == length_b:
        for i in range(length_a):
            if city_a[i] != city_b[i]:
                return False
        return True
    return False


def add_possibilities(possibilities):
    for i in adjacencies.keys():
        if i[0] not in possibilities:
            possibilities.append(i[0])
        if i[1] not in possibilities:
            possibilities.append(i[1])
    possibilities.sort()


def permute_possibilities():
    neighbor_cities = []
    for i in range(0, len(adjacencies)):
        for subset in permutations(possibilities, i):
            for j in subset:
                if j not in neighbor_cities:
                    neighbor_cities.append(j)
                for k in possibilities:
                    x = adjacencies.get((j, k), False)
                    if x:
                        if k not in neighbor_cities:
                            neighbor_cities.append(k)
                    x = adjacencies.get((k, j), False)
                    if x:
                        if k not in neighbor_cities:
                            neighbor_cities.append(k)
            neighbor_cities.sort()
            neighbor_cities = validate_possibilities(neighbor_cities, i, subset)


if __name__ == '__main__':
    adjacencies = {}
    points = []
    possibilities = []
    city_a, city_b, dist = input().split()
    dist = int(dist)
    while dist > 0:
        adjacencies[(city_a, city_b)] = dist
        city_a, city_b, dist = input().split()
        dist = int(dist)
    add_possibilities(possibilities)
    minimum_points = len(possibilities)
    permute_possibilities()
    print(minimum_points)
    for i in points:
        print(i)
