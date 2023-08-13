# 3. PEAS Definition

In this section, I provide a structured perspective on how the ACO algorithm I designed interacts with its environment, makes decisions and achieves its goals.

## 3.1 Performance Measure

For detailed tests and benchmarking, please visit [this GitHub folder](https://github.com/wafaajaunnoo/AntsInMyCode/tree/main/Tests).

Initially, with a TSP of 20 cities, the algorithm took a runtime of 48 seconds, and it also got stuck in a local optima.  The output also varied accross different runs.  i assume his is mainly of the stochastic nature of ACO, which arises from several sources, including:

1. The random initialization of pheromone levels.
2. The random selection of initial cities for each ant.
3. The random tie-breaking in the selection of the enxt city based on probabilities.

At this stage, I figured that the parameters used in the code can be tuned to improve the performance of the algorithm.  The number of ants and iterations were increased to improve the quality of the solutions.  An increase in the pheromone evaporation rate also made the algorithm less greedy, leading to better solutions.

For the same number of cities but a lower number of ants, the runtime improved from 48 seconds to 17 seconds.

## 3.2 Environment

The environment for the TSP consists of a graph with a set of cities and their coordinates.  The environment also includes the following constraints:

1. Full journey should form a Hamiltonian Cycle.
2. All cities must be visited at least once.
3. Cities must be vities during their respective time windows.
4. If time windows are violated, the violations should be minimized.

These constraints affect the feasibiloty of the solutions.

## 3.3 Actuators

The actuators responsible for decision-making and influencing the environment are the agents/ants.  The agents decide on which city to visit next based on pheromone levels, cost, and time window constraints.  The agents also deposit pheromone on the edges of the TSP's graph. 

## 3.4 Sensors

In the TSP solved using ACO, the sensors include the ability of the agents to sense:
1. The pheromone on the graph's edges.
2. The cost (distance) between cities.
3. The time windows for each city.