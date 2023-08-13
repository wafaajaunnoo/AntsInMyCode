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
* Initialize the graph with a constant amount of `cities`, `ants`, and `x`.
* The agent is deployed in the search space.
* In the `utility_based_agent` function, an agent is initialized with a random starting city `current_point`.
* The visited status of all cities is marked as `False` except for the starting city, which is set to `True`.
* In the `ant_colony_optimization` function, pheromone matrices are initialized.

### 3.2.2 Agent Behaviour
* Make _k_ agents start from a random node and traverse the graph using the algorithm defined above. 
* The agent considers time-based penalties and pheromone levels.
* The agent evaluates each path based on the utilities provided.

### 3.2.3 State Transition 

In the algorithm, there are 4 state transitions for the agents:

1. Initialization State: The agent starts in this state. It randomly selects a starting city, marks it as visited, and adds it to the path.
2. Path Construction State: The agent repeatedly performs the aforementioned actions until all cities are visited while considering pheromone levels, cost, and penalties.
3. Returning to the initial city.
4. Termination State.

### 3.2.4 Global and Local Updates
The primary updates that occur relate to pheromone levels.
* For each traversal, update the pheromone levels according to the function `Q`.
* If a cycle which is better than the current best cycle is found, update it.

### 3.2.5 Termination Conditions
* Iterate for a certain times, or until convergence.

### 3.2.6 In detail:
In detail, the steps of the algorithm are defined as:

read how [this repo](https://github.com/Akavall/AntColonyOptimization/blob/master/README.md) explains the algorithm.

[also read](https://www.matec-conferences.org/articles/matecconf/pdf/2018/105/matecconf_iswso2018_03015.pdf)


**Step 1:**

**Step 2:**

**Step n:**

## 3.3 Potential Improvements
Some potential enhancements to this technique that I did not have time to implement:

1. Because each ant is autonomous, traversals might be easily parallelelized. This is simple to accomplish with the multiprocessing Python module, however it does not operate by default on Mac. I chose portability above performance in this compromise.

2. Choosing the next step in a traversal may be done in parallel with numpy vector multiplication, resulting in a 5x quicker overall performance. However, because to numerical instability, a leap to the same node may be repeated even though I was multiplying by zero, and fixing this error would have required more work than I believed was worthwhile.



