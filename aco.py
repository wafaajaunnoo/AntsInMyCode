"""
  --importing libraries:
  np: for numerical computation
  random: to geenrate random numbers
  plt: to create visualizations
  Axes3D: for 3D plotting of the scenario
"""
import numpy as np # library for numerical computations
import random # to generate random numbers
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
  utility functions (will act as utility-based agents) to claculate distances & costs, and to validate time windows
  distance: calculates euclidean distance between 2 points (cities)
  cost: adds distance between 2 points to calculate cost.
        als generates a random value between 0 and 100 to simulate pheromone influence.
  is_valid_time_window: checks if current time of visiting ant is within
                        the time window specified for the city being visited.
                        return "true" if time window is valid, else "false"
"""

def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def cost(point1, point2):
    return distance(point1, point2) + 100 * np.random.rand()

def is_valid_time_window(visited, current_city, time_windows):
    current_time = visited[current_city][1]
    return time_windows[current_city][0] <= current_time <= time_windows[current_city][1]

"""
  func utility_based_agent with 5 parameters:
  1. 'cities': city coordinates, represented as (x,y)
  2. 'pheromone': matrix to represent pheromone levels between cities (pheremone[i,j] represents PL between cities 'i' and 'j')
  3. 'alpha': controls importance of pheromone level in decision making
  4. 'beta': controls importance of cost in decision-making
  5. 'time_windows': dictionary where each key represents a city index. Tuple (start_time, end_time) represents time window for a city
"""
def utility_based_agent(cities, pheromone, alpha, beta, time_windows):
    '''
      'visited': a list of lists- each sublist represents a city and stores:
      i) values true & false to check if a city is visited
      ii) arrival time at that city
    '''
    visited = [[False, 0] for _ in range(len(cities))]
    current_point = np.random.randint(len(cities)) # initializes agent's current city randomly
    visited[current_point][0] = True
    path = [current_point + 1]  # a list to store visited cities. Add 1 to the city number so city num starts at 1 and not 0
    path_length = 0 # initializes length of path

    '''
    main loop.
    - 'unvisited': list of unvisited cities
    - 'probabilities': array to store probability of selecting each unvisited city as next destination
    - Probability value is calculated based on pheromone levels, cost and time window constraints.
    '''
    while False in [v[0] for v in visited]:
        unvisited = np.where(np.logical_not([v[0] for v in visited]))[0]
        probabilities = np.zeros(len(unvisited))

        for i, unvisited_point in enumerate(unvisited):
            penalties = 0
            if cities[current_point][1] > cities[unvisited_point][1]:
                penalties += 100
            if cities[current_point][1] < cities[unvisited_point][1]:
                penalties -= 100
            if penalties < 0:
                penalties = 0

            if is_valid_time_window(visited, unvisited_point, time_windows):
                probabilities[i] = pheromone[current_point, unvisited_point]**alpha / cost(cities[current_point], cities[unvisited_point])**beta + penalties

        if np.sum(probabilities) == 0:
            #if no valid time window exists, allow visiting any city 
            probabilities = np.ones(len(unvisited))

        probabilities /= np.sum(probabilities)

        next_point = np.random.choice(unvisited, p=probabilities)
        arrival_time = max(visited[current_point][1] + cost(cities[current_point], cities[next_point]), time_windows[next_point][0])
        path.append(next_point + 1)  #add 1 to the city number to adjust for starting from 1
        path_length += cost(cities[current_point], cities[next_point])
        visited[next_point][0] = True
        visited[next_point][1] = arrival_time
        current_point = next_point

    return path, path_length

    '''
    - uses the principles of ACO to iteratively update pheromone levels on paths between cities
    - employs utility-based agents/ants that make probabilistic decisions while considering all constraints
    - constructs paths based pn probabilistic decision-making.
    '''
def ant_colony_optimization(cities, n_ants, n_iterations, alpha, beta, evaporation_rate, Q, time_windows):
    n_cities = len(cities)
    pheromone = np.ones((n_cities, n_cities))
    best_path = None
    best_path_length = np.inf

    for iteration in range(n_iterations):
        paths = []
        path_lengths = []

        for ant in range(n_ants):
            path, path_length = utility_based_agent(cities, pheromone, alpha, beta, time_windows)
            paths.append(path)
            path_lengths.append(path_length)

            if path_length < best_path_length:
                best_path = path
                best_path_length = path_length

        pheromone *= evaporation_rate

        for path, path_length in zip(paths, path_lengths):
            for i in range(n_cities - 1):
                pheromone[path[i] - 1, path[i + 1] - 1] += Q / path_length  # subtract 1 to adjust for starting from 1
            pheromone[path[-1] - 1, path[0] - 1] += Q / path_length  # subtract 1 to adjust for starting from 1

        #updating pheromone levels dynamically  based on best path length found so far
        if iteration % 10 == 0:  # evaporation rate is adjusted every 10 seconds
            best_path_length_so_far = min(path_lengths)
            evaporation_rate = 0.5 * (1 - (best_path_length_so_far / best_path_length))  # Example adjustment formula

        #print(f"Iteration {iteration+1} - Pheromone Matrix:")
        #print(pheromone) -- gives output for the pheromone level at each

    #ensure the best path ends with the same city as the first visited city
    best_path.append(best_path[0])

    return best_path, best_path_length

if __name__ == "__main__":
    np.random.seed(42)
    cities = np.random.rand(17, 3)

    #generate random time windows for each city (start time, end time)
    time_windows = np.random.randint(0, 100, size=(len(cities), 2))

    best_path, best_path_length = ant_colony_optimization(cities, n_ants=30, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.5, Q=1, time_windows=time_windows)

    print("Cheapest path:", best_path)
    print("Cheapest path length:", best_path_length)
    
    x_coords = cities[:, 0]
    y_coords = cities[:, 1]
    z_coords = cities[:, 2]

    #plot all cities in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_coords, y_coords, z_coords, c='b', marker='o', label='Cities')

    path_x = x_coords[np.array(best_path) - 1]
    path_y = y_coords[np.array(best_path) - 1]
    path_z = z_coords[np.array(best_path) - 1]
    ax.plot(path_x, path_y, path_z, c='r', marker='o', label='Path', linestyle='-')

    start_city_x, start_city_y, start_city_z = x_coords[best_path[0] - 1], y_coords[best_path[0] - 1], z_coords[best_path[0] - 1]
    ax.scatter(start_city_x, start_city_y, start_city_z, c='g', marker='*', s=200, label='Starting City')

    #adding city labels
    for i, (x, y, z) in enumerate(zip(x_coords, y_coords, z_coords)):
        ax.text(x, y, z, f'City {i + 1}', color='black', fontsize=8)

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Z Coordinate')
    ax.set_title('TSP Path with Ant Colony Optimization')
    plt.legend()
    plt.grid(True)
    plt.show()
