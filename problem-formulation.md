# 2. Combinatorial Problem Formulation
<!--In Artificial Intelligence, the following steps are to be followed when solving problems:

1. Problem definition (specify inputs and acceptable solutions).
2. Problem analysis.
3. Knowledge representation (provide detailed information about problem and define all possible techniques).
4. Problem-solving (selection of best technique(s)).
-->
I start this section by defining a TSP.  I follow with the simplification of the problem's complexity, which I define as the *constraints*, *objectives* and *miscellaneous **relevant** information that adds to the complexity*.  Later, I argue the rationale behind my choice to solve the TSP with the Ant Colony Optimization (ACO) algorithm.

## 2.1 The Travelling Salesman Problem
The TSP is an NP-Hard combinatorial problem which consists of a salesman and a set of cities.  The salesman has to visit each city, starting from a certain one, and return to the same city at the end of the journey.  The main challenge of the problem is that the salesman wants to minimize the total length and cost of the trip.

In the case of **_n_** cities, the possibilities of getting a solution are given by 

$$ n! \over 2 $$

Given **_n_** = 30.  If a computer can do 10<sup>6</sup> calculations in 1 second, it will take 

$$ 30! \over (2 \times 10^6) $$ 

seconds to solve the problem, or

$$ 30! \over (2 \times 10^6 \times 24 \times 60 \times 60) $$ 

days. And that is huge! It is impossible to find all possible routes and then get the optimal solution.  Therefore, the TSP is an NP-Hard problem.  The discovery of a fast algorithm to solve it will mean that there will be fast algorithms to solve all nP-Hard problems.

### Context:
My father is a salesman who must deliver his merchandise to n shops around Mauritius by car. Each shop has different opening and closing hours. Once my father leaves home, he must continue driving forward to each shop and return home only after completing all deliveries. His goal is to maximize efficiency and profit by selecting the most economical path. Therefore, his objective is to optimize his route, ensuring that he covers all shops in a single continuous journey while adhering to their operating hours.

### TSP Formulation
For simplicity, I formulate the following TSP:

Given a graph **_G_** representing a set of **_n_** cities, where each city is denoted as a node in **_G_** and has a different time window during which the salesman can arrive.  The distances between pairs of cities in _G_ are symmetric (the distance between City A and City B is identical to the distance between City B and City A).  Find an optimal route that minimizes both the total distance travelled and the time window violations by the salesman.  Other than satisfying all constraints, the route must form a Hamiltonian Cycle.

## 2.2 Problem Complexity
-- problem analysis
An optimization problem is represented by an objective function and its constraints.

### 2.2.1 Constraints
1. Each city can only be visited once.
2. The salesman should arrive at each city within the specified time window.
3. The salesman must minimize both the total distance travelled and the time window violations.
4. The pheromone levels are dynamically updated.
5. The salesperson must return to the starting city after visiting all cities.
   
### 2.2.2 Objectives
One of the core tenets of the philosophy of the TSP is that there is no single, perfect solution to any problem. The objective function of the TSP is to minimize the total distance travelled and form a Hamiltonian Cycle while satisfying the above constraints. However, the shortest route may not always be the best route, as it may take longer if it passes through more difficult terrain. Ergo, our functional aim here is to find a solution that is good enough, rather than a perfect solution.

### 2.2.3 Heuristics and Techniques
1. Constructive heurisitics: I start the algorithm with an initial solution - a randomly selected city.
2.  

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



