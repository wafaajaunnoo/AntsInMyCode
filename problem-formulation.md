# 2. Combinatorial Problem Formulation
<!--In Artificial Intelligence, the following steps are to be followed when solving problems:

1. Problem definition (specify inputs and acceptable solutions).
2. Problem analysis.
3. Knowledge representation (provide detailed information about problem and define all possible techniques).
4. Problem-solving (selection of best technique(s)).
-->
Logically, I start this section by defining a TSP.  I follow with the simplification of the problem's complexity, which I define as the *constraints*, *objectives* and *miscellaneous **relevant** information that add to the complexity*.  Later, I argue the rationale behind my choice to solve the TSP with the Ant Colony Optimization (ACO) algorithm.

## 2.1 The Travelling Salesman Problem
-- problem definition ( add important points, anything from research papers) 

-- Why the problem is NP-Hard
* the number of alternative solution sequences rises exponentially with the number of cities.
* no known algorithm exists to solve it in polynomial time

[Proof that TSP is np-Hard](https://www.tutorialspoint.com/proof-that-travelling-salesman-problem-is-np-hard)
## 2.2 Problem complexity
-- problem analysis
An optimization problem is represented by an objective function and its constraints.
### 2.2.1 Constraints
### 2.2.2 Objectives
One of the core tenets of the philosophy of the TSP is that there is no single, perfect solution to any problem. The main objective of the TSP is to find the shortest possible route that visits each city exactly once and returns to the origin city. However, the shortest route may not always be the best route, as it may take longer if it passes through more difficult terrain. Our aim here is to find a solution that is good enough, rather than a perfect solution.
### 2.2.3 Miscellanous

## 2.3 Problem-solving
-- knowledge representation (provide detailed information about problem and define all possible techniques).

### 2.3.1 Optimization Algorithms
Finding an algorithm that reduces computation is necessary to solve the TSP.

### 2.3.2 Selection of best Technique

#### Advantages of ACO for solving TSP
#### Disadvantages of other algorithms for solving TSP
Other algorithms, such as genetic algorithms and simulated annealing, can be effective in finding good solutions to the TSP, but they can be more difficult to implement and tune than the ACO algorithm.
#### What makes ACO a good fit?
* TSP is a discrete optimization problem, which means that the solutions are a set of discrete values. The ACO algorithm is a good fit for discrete optimization problems because it is able to search through the solution space efficiently.
* TSP is a non-deterministic problem, which means that there is no guarantee that the same solution will be found every time the problem is solved. The ACO algorithm is a good fit for non-deterministic problems because it is able to adapt to different problem instances.
* TSP is a multi-objective problem, which means that there are multiple competing objectives that need to be optimized. The ACO algorithm is a good fit for multi-objective problems because it is able to find solutions that are good on multiple objectives.

I have used the ACO algorithm to solve the TSP on a number of different problem instances, including problems with hundreds of cities. In my experience, ACO has been able to find good solutions to all of the problems that I have tried it on.  The ACO algorithm is a relatively easy algorithm to implement, and it can be parallelized to speed up the search process.  The ACO algorithm is a good fit for a variety of TSP problems, including problems with different numbers of cities, different distances between cities, and different constraints.



