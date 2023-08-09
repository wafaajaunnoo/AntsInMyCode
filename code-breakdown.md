_If you're not interested in the breakdown of the codes, you can see the full codes [here](#)._

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
1. `cities`: City coordinates represented as (x,y)
2. `pheromone`: Matrix to represent pheromone levels (PL) between cities. `pheromone[i,j]` represents PL between city `i` and city `j`.
3. `alpha`: Controls the importance of pheromone level in decision-making.
4. `beta`: Controls the importance of cost in decision-making.
5. `time_windows`: A dictionary where each key represents a city index.  The tuple `(start_time, end_time)` represents the time window for a city.

#### Lists, Arrays and loops in the UBA Function
1. `visited`: A list of list, where each sublist represents a city and stores:
    * The values "True" and "False" to check if a city is visited.
    * The arrival time at that city.
2. `unvisited`: A list to store the unvisited cities.
3.  
```python
def utility_based_agent(cities, pheromone, alpha, beta, time_windows):
    visited = [[False, 0] for _ in range(len(cities))]  
    current_point = np.random.randint(len(cities)) # initializes agent's current city randomly 
    visited[current_point][0] = True
    path = [current_point + 1]  # a list to store visited cities. Add 1 to the city number so city num starts at 1 and not 0
    path_length = 0 # initializes length of path

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
            # If no valid time window, allow visiting any city (non-time window constraint)
            probabilities = np.ones(len(unvisited))

        probabilities /= np.sum(probabilities)

        next_point = np.random.choice(unvisited, p=probabilities)
        arrival_time = max(visited[current_point][1] + cost(cities[current_point], cities[next_point]), time_windows[next_point][0])
        path.append(next_point + 1)  # Add 1 to the city number to adjust for starting from 1
        path_length += cost(cities[current_point], cities[next_point])
        visited[next_point][0] = True
        visited[next_point][1] = arrival_time
        current_point = next_point

    return path, path_length
```