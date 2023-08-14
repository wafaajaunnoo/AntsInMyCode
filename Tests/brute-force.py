import numpy as np
import itertools

def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def brute_force_tsp(cities):
    n_cities = len(cities)
    all_permutations = itertools.permutations(range(n_cities))
    min_path_length = np.inf
    best_path = None

    for perm in all_permutations:
        current_path_length = 0

        for i in range(n_cities - 1):
            current_path_length += distance(cities[perm[i]], cities[perm[i+1]])

        current_path_length += distance(cities[perm[-1]], cities[perm[0]])

        if current_path_length < min_path_length:
            min_path_length = current_path_length
            best_path = perm

    return [city + 1 for city in best_path], min_path_length

if __name__ == "__main__":
    np.random.seed(42)
    cities = np.random.rand(50, 3)

    best_path, best_path_length = brute_force_tsp(cities)

    print("Cheapest path:", best_path)
    print("Cheapest path length:", best_path_length)
