# 3. Intuition of the algorithm's operation
Having formulated the problem, I now design the algorithm for the TSP based on the behaviour of ants, while taking inspiration from the principles of a Turing Machine.  I describe the optimization algorithm I implemented and I provide an intuition on how it works for the TSP I formulated previously. 

## 3.1 Ant Colony Optimization

Ant colony optimisation (ACO) draws its inspiration from several ant species' foraging strategies. These ants leave pheromone trails on the ground to indicate a good route for the colony's other ants to take. An analogous method is used by ant colony optimisation to address optimisation issues. <sup><sub>[[7]](https://www.researchgate.net/publication/308953674_Ant_Colony_Optimization).</sub></sup>
### The Algorithm
To solve any problem that exists, a Turing Machine would:
1. Start with an input string on its tape.
2. Use its rules to process the input, one symbol at a time.
3. Reach a state where it has solved the problem.
4. Output the answer.
5. Give up if a solution is not found.
   
I begin the algorithm by first initializing a pheromone trail between all cities.  The algorithm brings in a number of ants, each of which will navigate the search space randomly, leaving pheromone behind, until they have visited all cities. I set the constraints and objectives of the algorithm.  I proceed with the algorithm by depositing the most pheromone on the shortest path found by the ants.  Even though ants will randomly choose which edge to travel through at each step of their traversal, they will give higher preference to paths with more pheromones than those with fewer pheromones.  This will make it more likely that other ants will follow that path in the future.  Furthermore, if a path is longer, it will earn less preference as it suggests longer transit durations.  I also dynamically update the pheromone levels so that future generations of ants are not confused by the old pheromone trails.  I repeat this process for a number of iterations.  Later on, I converge the algorithm on the shortest path.  To help visualize the solution and better understand how the algorithm works, I print the cheapest path and its length.  I also plot the cheapest path on a labelled 3D subplot that is embedded within a larger graph.

## 3.3 Pseudocode
The algorithmic design can be defined as follows:

<sup><sub>You can view the codes for the below algorithmic design [here](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/pseudocode.js-master/docs/pseudocode.html).</sub></sup>
<p align="center">
<img width="573" alt="Screenshot 2023-08-11 at 22 32 46" src="https://github.com/wafaajaunnoo/AntsInMyCode/assets/95095359/fe23a9d5-ca73-46c1-8414-c296d0fab371">
</p>

## 3.2 Steps

### 3.2.1 Initialization  
* The graph is initialized with a constant amount of cities (`cities`), ants (`n_ants`), iterations (`n_iterations`), evaporation rate (`evaporation_rate`) and pheromone reinforcement factor (`Q`).
* At the beginning, the pheromone matrix (`pheromone`) is initialized with a constant value of '1'.
* The agent is deployed in the search space.
* In the `utility_based_agent` function, an agent is initialized with a random starting city `current_point`.
* The visited status of all cities is marked as `False` except for the starting city, which is set to `True`.
* In the `ant_colony_optimization` function, pheromone matrices are initialized dynamically.

### 3.2.2 Agent Behaviour
* Make _k_ agents start from a random node and traverse the graph using the algorithm defined above. 
* Agent balances between intensification.
* The agent considers time-based penalties and pheromone levels.
* The agent evaluates each path based on the utilities provided.
* Agent becomes more likely to exploit paths with higher pheromone levels.
* Agent uses probabilities to decide the next city to visit.
* Agent contributes to global updates by reinforcing successful paths.

### 3.2.3 State Transition 

1. **Initialization State:** The agent starts in this state. It randomly selects a starting city, marks it as visited, and adds it to the path.
2. **Path Construction State:** The agent repeatedly performs the aforementioned actions until all cities are visited. 
3. **Rules:** When transitioning from one state to another, the agent also considers pheromone levels, cost, penalties, and heuristic information derived from the cost betwene cities.  These factors are used to calculate probabilities for selecting the next city to visit, guiding the agent's decision-making process.
4. Returning to the initial city.
5. **Termination State.**

### 3.2.4 Global and Local Updates
The primary updates that occur relate to pheromone levels.
* For each traversal, update the pheromone levels according to the function `Q`.
* If a cycle which is better than the current best cycle is found, update it.
* Global updates includes the addition of pheromone to all edges in the best cycle,
* local updates involves the addition of a smaller amount of pheromone to the edges visited by each ant, promoting exploitation of shorter paths.

### 3.2.5 Termination Conditions
* Agent can explore path only if the time window of the next city allows it.
* Iterate for a certain times, or until convergence.
* Do not terminate until all cities have been visited.


### 3.2.6 In detail:
In detail, the steps of the algorithm are defined as:

Alternatively, you can view a breakdown of the codes [here](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/code-breakdown.md).

**Step 1: Importing libraries.**

**Step 2: Defining utility functions.**

**Step 3: Define function for the utility-based agent** 
* Keeps track of visited cities in list `visited`.
* Randomly selects an initial city for the agent and marks it as visited.
* Initializes `path` to store visited cities and `path_length` for the total length of the path
* Calculates probabilities for selecting next city to be visited based on constraints provided.
* If no valid time windows exists, set all probabilities to 1, to allow visiting any next city.
* Calculate arrival time at the next city and update `path`, `path_length` and `visited`.
* Return calculated `path` and `path_length`.
    
**Step 4: Define function `ant_colony_optimization`**
* Proceeds with iterations to find best path and cheapest length.
* Stores the path and length in lists `paths` and `path_lengths`.
* Updates pheromone levels by evaporating previous pheromones and depositing new pheromones based on paths taken by agents.
* Pheromone is dynamically updated.
* Ensures the best path ends with the same city as the first-visited city.
* Returns `best_path` and `best_path_length`.
    
**Step 5: Main execution block** 
* Used mainly to output results.
* Sets a random seed for reproducibility.
* Generates random city coordinates using `np.random.rand`.
* Calls `ant_colony_optimization` with specified parameters to find the best path and length.
* Prints cheapest path and its length.
* Extract and plot x, y, and z coordinates for all cities.

## 3.3 Potential Improvements
Some potential enhancements to this technique that I did not have time to implement:

1. Because each ant is autonomous, traversals might be easily parallelelized. This is simple to accomplish with the multiprocessing Python module, however it does not operate by default on Mac. I chose portability above performance in this compromise.

2. Choosing the next step in a traversal may be done in parallel with numpy vector multiplication, resulting in a 5x quicker overall performance. However, because to numerical instability, a leap to the same node may be repeated even though I was multiplying by zero, and fixing this error would have required more work than I believed was worthwhile.

[Read about the PEAS definition.](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/peas-def.md)


