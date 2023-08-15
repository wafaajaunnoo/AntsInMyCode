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

To ensure that the agent is taking into consideration the time window constraints and that the probabilities and the dynamic updates of the pheromone levels are working, their values were printed for each iteration and commented out for sanity.

```python
        print(f"Iteration {iteration+1} - Pheromone Matrix:")
        print(pheromone) -- gives output for the pheromone level at each
        #print(f"Ant visited city {next_point + 1} at time {arrival_time:.2f}")
        #print("Probabilities:", probabilities)
```

The same TSP was tested using the brute-force approach and the branch and bound method.  The results were compared and analyzed in [this](https://docs.google.com/spreadsheets/d/19O5P_cwfMBUUsHBFT-onme_q60WSVtzXhvDenepc0oc/edit?usp=sharing) sheet.
Brute force does an extensive exploration of all city permutations, which results in a combinatorial explosion. As more cities are built, this method quickly becomes unfeasible.  Branch and bound involves considerable investigation of various routes even if its goal is to cut search tree branches that cannot lead to the best results. If the problem instance doesn't lend itself to efficient pruning, branch and bound may, in the worst case, display exponential time complexity.  ACO may concentrate on promising areas of the solution space thanks to its emergent behaviour without having to thoroughly investigate every possibility. This flexibility is very notable.  Pheromone levels are used by ACO to strike a balance between using established pathways and exploring unexplored ones. Due to the algorithm's dynamic modification, it is possible for it to avoid becoming caught in local optima and to stimulate the exploration of novel ideas, which increases the possibility of finding better answers more quickly.  Essentially, since the agent in the ACO algorithm balances between intensification and diversification, a good combination of these 2 components will usually ensure that global optimality is achievable.  The selection of the best component guarantees that solutions converge to the optimum, but diversification via randomization enables the search to diverge from local optima while increasing the diversity of solutions.  As far as the algorithm I built is concerned, the optimal path was identified at all times when the [final codes](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/aco.py) were executed. 

## 3.2 Environment

The environment for the TSP consists of a graph with a set of cities and their coordinates.  The environment also includes the following constraints:

1. Full journey should form a Hamiltonian Cycle.
2. All cities must be visited at least once.
3. Cities must be visited during their respective time windows.
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
