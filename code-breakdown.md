_If you're not interested in the breakdown of the codes, you can see the full codes [here](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/aco.py)._

### Importing Required Libraries
Import the following libraries for:
1. numpy: numerical computation
2. random: generating random numbers
3. matplotlib.pyplot: creating visualizations
4. mpl_toolkits.mplot3d: 3D plotting of the scenario

      
```python
import numpy as np
import random 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
```

### Defining Utility Functions
The utility functions will act as utility-based agents.  They will be used to calculate distances and costs and to validate time windows.

`distance`: calculates the Euclidean distance between 2 points (cities).

`cost`: adds distance between 2 cities to calculate the cost.  It also generates a random value between 0 and 100 to simulate pheromone influence.

`is_valid_time_window`: checks if the current time of visiting for the city is within the time window specified for the city being visited. The function returns 'True' if the time window is valid, else it returns 'False'.

      
```python
def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def cost(point1, point2):
    return distance(point1, point2) + 100 * np.random.rand()

def is_valid_time_window(visited, current_city, time_windows):
    current_time = visited[current_city][1]
    return time_windows[current_city][0] <= current_time <= time_windows[current_city][1]
```

### Define Utility-Based Agent (UBA) Function
The function `utility_based_agent` takes 5 parameters:
1. `cities`: City coordinates are represented as (x,y).
2. `pheromone`: Matrix to represent pheromone levels (PL) between cities. `pheromone[i,j]` represents PL between city `i` and city `j`.
3. `alpha`: Controls the importance of pheromone level in decision-making.
4. `beta`: Controls the importance of cost in decision-making.
5. `time_windows`: A dictionary where each key represents a city index.  The tuple `(start_time, end_time)` represents the time window for a city.

* `visited`: A list of list, where each sublist represents a city and stores:
    * The values "True" and "False" to check if a city is visited.
    * The arrival time at that city.
* `unvisited`: A list to store the unvisited cities.
* Penalties for each unvisited city are calculated.
* Time window validity is checked for the current city.
* Probabilities are normalized.
* Arrival time for the next city is calculated, considering the cost and time windows.
* The path, path length and visited status of the next city are updated.

```python
def utility_based_agent(cities, pheromone, alpha, beta, time_windows):

    visited = [[False, 0] for _ in range(len(cities))] 
    current_point = np.random.randint(len(cities)) # initializes agent's current city randomly
    visited[current_point][0] = True
    path = [current_point + 1]
    path_length = 0

    while False in [v[0] for v in visited]:
        unvisited = np.where(np.logical_not([v[0] for v in visited]))[0]
        probabilities = np.zeros(len(unvisited))

        for i, unvisited_point in enumerate(unvisited):
            penalties = 0
            if cities[current_point][1] > cities[unvisited_point][1]:
                penalties += 100
            if cities[current_point][1] < cities[unvisited_point][1]:
                penalties -= 100

            # Normalize penalties factor to ensure non-negative probabilities
            penalties = penalties - np.min(penalties)
            penalties = np.maximum(penalties, 0.0000001)

            if is_valid_time_window(visited, visited[current_point][1], current_point, unvisited_point):
                pheromone_factor = pheromone[current_point, unvisited_point]**alpha
                cost_factor = 1 / cost(cities[current_point], cities[unvisited_point])**beta
                probabilities[i] = pheromone_factor * cost_factor * np.exp(-penalties)

        probabilities = np.where(np.isnan(probabilities), 0, probabilities)
        probabilities /= np.sum(probabilities)

        next_point = unvisited[np.argmax(probabilities)]
        arrival_time = max(visited[current_point][1] + cost(cities[current_point], cities[next_point]), time_windows[next_point][0])
        path.append(next_point + 1) #add 1 to the city number to adjust for starting from 1
        path_length += cost(cities[current_point], cities[next_point])
        visited[next_point][0] = True
        visited[next_point][1] = arrival_time
        current_point = next_point


        #print(f"Ant visited city {next_point + 1} at time {arrival_time:.2f}")
        #print("Probabilities:", probabilities)
    return path, path_length

```

### Ant Colony Optimization Function
The function `ant_colony_optimization` takes 5 parameters:
1. `cities`: City coordinates are represented as (x,y).
2. `n_ants`: For each iteration, the inner loop runs `n_ants` times, representing the number of ants used for the optimization.
3. `n_iterations`: The outer loop iterates `n_iterations` times, representing the number of optimization cycles.
4. `alpha`: Importance of pheromone levels in decision-making.
5. `beta`: Importance of cost (distance) in decision-making.
6. `evaporation_rate`: reduces pheromone levels for all edges.
7. `Q`: A hyperparameter to determine the amount of pheromone deposited on edges during local and global pheromone updates.  The higher the value of 'Q', the more pheromone is deposited.
5. `time_windows`

* Every 10 iterations, the evaporation rate is adjusted based on the best length found so far.
* After all iterations, the function appends the initial city to the best path to form a Hamiltonian Cycle.
* Returns the best path and its length.
In sum, this function orchestrates the optimization process by coordinating multiple agents (ants) to traverse paths based on utility-based decision-making.  The pheromone levels are dynamically updated and adjusted to influence the agent's decisions in favour of shorter and more efficient paths.  The optimal path is found by considering pheromone levels and time window constraints.

```python
def ant_colony_optimization(cities, n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
    n_cities = len(cities)
    pheromone = np.ones((n_cities, n_cities))
    best_path = None
    best_path_length = np.inf

    for iteration in range(n_iterations):
        paths = []
        path_lengths = []

        for ant in range(n_ants):
            # Call utility_based_agent to get the path and path length
            path, path_length = utility_based_agent(cities, pheromone, alpha, beta, time_windows)
            paths.append(path)
            path_lengths.append(path_length)

            if path_length < best_path_length:
                best_path = path
                best_path_length = path_length

        pheromone *= evaporation_rate

        for path, path_length in zip(paths, path_lengths):
            for i in range(n_cities - 1):
                pheromone[path[i] - 1, path[i + 1] - 1] += Q / path_length
            pheromone[path[-1] - 1, path[0] - 1] += Q / path_length

        #dynamic pheromone update based on best path length found so far
        if iteration % 10 == 0:
            best_path_length_so_far = min(path_lengths)
            evaporation_rate = 0.5 * (1 - (best_path_length_so_far / best_path_length))

    best_path.append(best_path[0])
```
