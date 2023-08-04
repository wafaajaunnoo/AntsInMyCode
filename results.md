# aco.py
Runtime: 48secs

## Output 1:
* Best tour: [11, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
* Best tour length: 15

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
-- If I'm not mistaken, the more ants we have, the more pheromones should be released, hence the ants will better remember the paths.  
-- This leads to better exploitation and exploration of solution space =>should give a lower runtime compared to a bigger number of ants

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
  
**Note:**
1. The parameters used in the code can be tuned to improve the performance of the algorithm. Increase the number of ants and the number of iterations to improve the quality of the solutions
2. Increasing the pheromone evaporation rate will make the algorithm less greedy, which can sometimes lead to better solutions
