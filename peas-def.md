# 3. PEAS Definition

In this section, I provide a structured perspective on how the ACO algorithm I designed interacts with its environment, makes decisions and achieves its goals.

## 3.1 Performance Measure

For detailed tests and benchmarking, please visit [this GitHub folder](https://github.com/wafaajaunnoo/AntsInMyCode/tree/main/Tests).

Initially, when dealing with a Traveling Salesman Problem (TSP) involving 20 cities, the algorithm exhibited a runtime of 48 seconds and became trapped in local optima. The output also exhibited variations across different runs. These phenomena are primarily attributed to the stochastic nature inherent in ACO, arising from several sources, including:

1. The random initialization of pheromone levels.
2. The random selection of initial cities for each ant.
3. The random tie-breaking during the selection of the next city based on probabilities.

At this stage, I realized that tuning the parameters in the code could enhance the algorithm's performance. Increasing the number of ants and iterations served to improve the quality of solutions. Additionally, elevating the pheromone evaporation rate rendered the algorithm less greedy, resulting in superior solutions.

When maintaining the same number of cities but reducing the number of ants, the runtime improved significantly from 48 seconds to 17 seconds.

To ensure the dynamic update of pheromone levels, the values were printed for each iteration using the following lines of code, which were subsequently commented out for sanity. 

```python
        print(f"Iteration {iteration+1} - Pheromone Matrix:")
        print(pheromone) -- gives output for the pheromone level at each
```

The output gave something like this:

--insert s.s of PL

Essentially, since the agent in the ACO algorithm balances between intensification and diversification, a good combination of these 2 components will usually ensure that global optimality is achievable.  The selection of the best component guarantees that solutions converge to the optimum, but diversification via randomization enables the search to diverge from local optima while increasing the diversity of solutions.

## 3.2 Environment

The environment for the TSP consists of a graph with a set of cities and their coordinates.  The environment also includes the following constraints:

1. Full journey should form a Hamiltonian Cycle.
2. All cities must be visited at least once.
3. Cities must be vities during their respective time windows.
4. If time windows are violated, the violations should be minimized.

These constraints affect the feasibility of the solutions.

## 3.3 Actuators

The actuators responsible for decision-making and influencing the environment are the agents/ants.  The agents decide on which city to visit next based on pheromone levels, cost, and time window constraints.  The agents also deposit pheromone on the edges of the TSP's graph. 

## 3.4 Sensors

In the TSP solved using ACO, the sensors include the ability of the agents to sense:
1. The pheromone on the graph's edges.
2. The cost (distance) between cities.
3. The time windows for each city.

[View the Python program here.](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/aco.py)
