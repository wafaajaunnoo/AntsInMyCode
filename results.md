# aco.py
Runtime: 48secs

## Output 1:
* Best tour: [11, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
* Best tour length: 15

-- observation1: the algorithm got stuck in a local optima!  

-- hence, it did **not** visit all the cities at once, which is the main point of TSP

-- the algorithm also did not return to the first city with which it started

--  trying other tests before refactoring!

## Output 2: 
* Best tour: [7, 14, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
* Best tour length: 15

## Output 3:
* Best tour: [14, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
* Best tour length: 15

## Output 4
* Best tour: [13, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
* Best tour length: 10

**Note:** 
It is totally normal to have different outputs at each run.  This is because ACO is a stochastic algorithm.  Its behaviour varies across different runs due to its randomness, which arises from several sources, including:

* the random initialization of pheromone levels
* the random selection of initial cities for each ant
* the random tie-breaking in the selection of the next city based on probabilities
  
# Test 1: Decrease the number of ants
--- num_ants = 20
Runtime: 17 seconds

-- the runtime is a bit weird.  
-- If I'm not mistaken, the more ants we have, the more pheromones should be released, hence the ants will better remember the paths  
-- This leads to better exploitation and exploration of solution space =>should give a lower runtime compared to a bigger number of ants
-- i wonder if increasing num_ants, num_iteration & pheromone before refactoring will provide different analyses compared to when refactoring prior to improving performance?

## Output1: 
* Best tour: [8, 8, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
* Best tour length: 11

## Output 2: 
Runtime: 18 seconds
* Best tour: [6, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
* Best tour length: 13

# Test 2: Increase the number of ants
--- num_cities = 15
--- num_ants = 60
Runtime: 1min 0secs

## Output 1
* Best tour: [11, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
* Best tour length: 16.54

## Output 2
* Best tour: [11, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
* Best tour length: 16.54

# Test 3: Increase the number of cities
--- num_cities = 50
--- num_ants = 20

## Output 1
* Best tour: [41, 0, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]
* Best tour length: 15
  
  -- annnd..all of them are stuck.

  -- it's good because I wanted to see this output at least once.
  
  -- It's bad because now I have to refactor my codes.
  
  -- to refactor:
      * use a "recency" heuristic, which gives more weight to the cities that have been visited recently.
      * use a "backtracking" heuristic, which allows the algorithm to backtrack to previous cities if it finds that it is not making progress
  
**Note:**
1. The parameters used in the code can be tuned to improve the performance of the algorithm. Increase the number of ants and the number of iterations to improve the quality of the solutions
2. Increasing the pheromone evaporation rate will make the algorithm less greedy, which can sometimes lead to better solutions
