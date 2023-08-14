import numpy as np

# Calculate the cost of a tour
def calculate_tour_cost(tour, cities, pheromone):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i+1]]) + pheromone[tour[i], tour[i+1]]
    cost += distance(cities[tour[-1]], cities[tour[0]])
    return cost

# Recursive function to perform Branch and Bound
def branch_and_bound(cities, pheromone, time_windows, current_time, current_city, visited):
    if all(visited):
        return [0], 0
    
    min_cost = np.inf
    min_tour = []
    
    for next_city in range(len(cities)):
        if not visited[next_city] and is_valid_time_window(visited, current_time, current_city, next_city):
            visited[next_city] = True
            new_time = max(current_time + cost(cities[current_city], cities[next_city]), time_windows[next_city][0])
            new_tour, new_cost = branch_and_bound(cities, pheromone, time_windows, new_time, next_city, visited.copy())
            new_cost += cost(cities[current_city], cities[next_city])
            
            if new_cost < min_cost:
                min_cost = new_cost
                min_tour = [current_city] + new_tour
                
            visited[next_city] = False
    
    return min_tour, min_cost

if __name__ == "__main__":
    np.random.seed(42)
    cities = np.random.rand(17, 3)
    time_windows = np.random.randint(low=9*60, high=17*60-30, size=(len(cities), 2))
    pheromone = np.ones((len(cities), len(cities))) * 0.1

    starting_city = 0
    visited = [False] * len(cities)
    visited[starting_city] = True

    best_tour, best_cost = branch_and_bound(cities, pheromone, time_windows, 9*60, starting_city, visited)

    print("Best tour:", best_tour)
    print("Best tour cost:", best_cost)
