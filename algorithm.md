# 3. Intuition of the algorithm's operation
In this section, I describe the optimization algorithm I implemented and I provide an intuition on how it works for the TSP I formulated previously.

## 3.1 Ant Colony Optimization

### A brief Overview

### The Algorithm
I begin the algorithm by first initializing  a pheromone trail between all cities.  The algorithm brings in a number of ants, each of which will navigate the search space randomly, leaving pheromone behind, until they have visited all cities. I proceed the algorithm by depositing the most pheromone on the shortest path found by the ants.  This will make it more likely that other ants will follow that path in the future.  I repeat this process for a number of iterations.  Later on, I converge the algorithm on the shortest path.  To help visualize the solution and better understand how the algorithm works, I print the cheapest path and its length.  I also plot the cheapest path on a labelled 3D subplot that is embedded within a larger graph.

## 3.2 Steps

read how [this repo](https://github.com/Akavall/AntColonyOptimization/blob/master/README.md) explains the algorithm.

**Step 1:**

**Step 2:**

**Step n:**

## 3.3 Pseudocode
The algorithm can be defined as follows:

```
# function
    do while
  end
```
