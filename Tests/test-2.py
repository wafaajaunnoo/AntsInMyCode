
import numpy as np
import random

# Define the number of cities and ants
num_cities = 10
num_ants = 20

# Define ACO parameters
num_iterations = 100
alpha = 1.0   # Pheromone weight
beta = 2.0    # Heuristic weight
rho = 0.5     # Pheromone evaporation rate

# Initialize pheromone levels on each edge using a matrix
pheromone = np.ones((num_cities, num_cities))

  '''
     Define the distance matrix (random values for demonstration purposes)
     for each pair of cities, the function generates a random distance between 5 and 10.
     The distance is rounded to two decimal places. The function returns the distance matrix.
     
  ''' 
distance = np.random.randint(5, 10, size=(num_cities, num_cities))

np.fill_diagonal(distance, 0)  # Set diagonal elements to 0 (distance to itself)

# Define the time windows (random values for demonstration purposes)
time_windows = []
for _ in range(num_cities):
    earliest_arrival = random.randint(0, 5)
    latest_arrival = earliest_arrival + random.randint(5, 10)
    time_windows.append([earliest_arrival, latest_arrival])

# Function to calculate the time window violation for a given tour
def calculate_time_window_violation(tour):
    time_violation = 0
    for i in range(len(tour)):
        city = tour[i]
        earliest_arrival, latest_arrival = time_windows[city]
        if i == 0:  # Starting city, no violation
            continue
        arrival_time = sum([distance[tour[i-1]][tour[i]] for tour[i] in tour])
        if arrival_time < earliest_arrival:
            time_violation += earliest_arrival - arrival_time
        elif arrival_time > latest_arrival:
            time_violation += arrival_time - latest_arrival
    return time_violation

# Ant Colony Optimization algorithm
def ant_colony_optimization():
    best_tour = None
    best_tour_length = float('inf')

    for iteration in range(num_iterations):
        tours = []  # List to store the tours of each ant

        # Construct solutions for each ant
        for ant in range(num_ants):
            current_city = random.randint(0, num_cities - 1)
            tour = [current_city]

            # Traverse the graph using the probabilities based on pheromone levels and heuristic information
            for step in range(num_cities - 1):
                next_city = choose_next_city(current_city, tour)
                tour.append(next_city)
                current_city = next_city

            tours.append(tour)

        # Update pheromone levels on each edge based on the tours constructed by ants
        update_pheromone(tours, pheromone)

        # Find the best tour among all the tours constructed by ants
        for tour in tours:
            tour_length = calculate_tour_length(tour)
            if tour_length < best_tour_length:
                best_tour = tour
                best_tour_length = tour_length

    return best_tour, best_tour_length

# Function to choose the next city for an ant to move to based on pheromone levels and heuristic information
def choose_next_city(current_city, tour):
    unvisited_cities = set(range(num_cities)) - set(tour)
    probabilities = [calculate_probability(current_city, city, tour) for city in unvisited_cities]

    # Check if all probabilities are zero, return the current city
    if all(prob == 0 for prob in probabilities):
        return current_city

    # Otherwise, use the random.choices() function as before
    next_city = random.choices(list(unvisited_cities), probabilities)[0]
    return next_city

# Function to calculate the probability of moving from the current city to a neighboring city
def calculate_probability(current_city, next_city, tour):
    pheromone_level = pheromone[current_city][next_city]
    distance_to_next_city = distance[current_city][next_city]
    time_window_violation = calculate_time_window_violation(tour + [next_city])
    if time_window_violation > 0:
        return 0
    return (pheromone_level ** alpha) * ((1.0 / distance_to_next_city) ** beta)

# Function to update pheromone levels on each edge after the ants have constructed their tours
def update_pheromone(tours, pheromone):
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1.0 - rho)  # Evaporate pheromone
            for tour in tours:
                if j in tour and i in tour:
                    pheromone[i][j] += 1.0 / calculate_tour_length(tour)

# Function to calculate the total length of a tour
def calculate_tour_length(tour):
    length = 0
    for i in range(len(tour) - 1):
        length += distance[tour[i]][tour[i + 1]]
    length += distance[tour[-1]][tour[0]]  # Return to the starting city

    return length

def print_time_windows():
    for i in range(num_cities):
        earliest_arrival, latest_arrival = time_windows[i]
        print(f"City {i + 1}: {earliest_arrival} - {latest_arrival}")

# Main function to run the Ant Colony Optimization algorithm
if __name__ == "__main__":
    best_tour, best_tour_length = ant_colony_optimization()
    print_time_windows()
    print("Best tour:", best_tour)
    print("Best tour length:", best_tour_length)
'''
Times executed: 1

Runtime: 3s

City 1: 3 - 10
City 2: 3 - 11
City 3: 0 - 8
City 4: 2 - 10
City 5: 2 - 7
City 6: 2 - 10
City 7: 0 - 6
City 8: 5 - 15
City 9: 3 - 10
City 10: 4 - 10
Best tour: [3, 2, 8, 8, 8, 8, 8, 8, 8, 8]
Best tour length: 15

'''
