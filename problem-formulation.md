# 2. Combinatorial Problem Formulation
<!--In Artificial Intelligence, the following steps are to be followed when solving problems:

1. Problem definition (specify inputs and acceptable solutions).
2. Problem analysis.
3. Knowledge representation (provide detailed information about the problem and define all possible techniques).
4. Problem-solving (selection of best technique(s)).
-->
I start this section by defining a TSP.  I follow with the simplification of the problem's complexity, which I define as the *constraints*, *objectives* and *miscellaneous **relevant** information that adds to the complexity*.  Later, I argue the rationale behind my choice to solve the TSP with the Ant Colony Optimization (ACO) algorithm.

## 2.1 The Travelling Salesman Problem
The TSP is an NP-Hard combinatorial problem which consists of a salesman and a set of cities.  The TSP is for the salesman to find the shortest possible tour that visits each city exactly once and returns back to the starting city.  The main challenge of the problem is that the salesman wants to minimize the total length and cost of the trip.

In the case of **_n_** cities, the possibilities of getting a solution are given by 

$$ n! \over 2 $$

Given **_n_** = 30.  If a computer can do $10^6$ calculations in 1 second, it will take 

$$ 30! \over (2 \times 10^6) $$ 

seconds to solve the problem, or

$$ 30! \over (2 \times 10^6 \times 24 \times 60 \times 60) $$ 

days. _And that is huge!_ It is impossible to find all possible routes and then get the optimal solution.  Therefore, the TSP is an NP-Hard problem.  The discovery of a fast algorithm to solve it will imply the existence of algorithms to solve all NP-Hard problems.

### Context:
My father is a salesman who must deliver his merchandise to **_n_** shops around Mauritius by car. Each shop has different opening and closing hours. Once my father leaves home, he must continue driving forward to each shop and return home only after completing all deliveries. His goal is to maximize efficiency and profit by selecting the most economical path. Therefore, his objective is to optimize his route, ensuring that he covers all shops in a single continuous journey while adhering to their operating hours.

### TSP Formulation
For simplicity, I formulate the following TSP:

Given a graph **_G_** representing a set of **_n_** cities, where each city is denoted as a node in **_G_** and has a different time window during which the salesman can arrive.  The distances between pairs of cities in _G_ are symmetric.  Find an optimal route that minimizes both the total distance travelled and the time window violations by the salesman.  Other than satisfying all constraints, the route must form a Hamiltonian Cycle.

## 2.2 Problem Complexity

A logical way to present an optimization problem is by its constraints and an objective function.

### 2.2.1 Constraints
1. Each city can only be visited once.
2. The salesman should arrive at each city within the specified time window.
3. The salesman must minimize both the total distance travelled and the time window violations.
4. The pheromone levels are dynamically updated.
5. The salesperson must return to the starting city after visiting all cities.
   
### 2.2.2 Objectives
One of the core tenets of the philosophy of the TSP is that there is no single, perfect solution to any problem. The **objective function** of the TSP is to minimize the total distance travelled and time window violations, and to form a Hamiltonian Cycle while satisfying all constraints. 

However, the shortest route may not always be the best route, as it may take longer if it passes through more difficult terrain. Ergo, our functional aim here is to find a solution that is good enough, rather than a perfect solution.

## 2.3 Problem-solving
In theoretical Computer Science, TSP is solved using approximation algorithms to try numerous permutations to maximize efficiency and profit.  3 common solutions to TSP are:

1. The brute-force approach
2. The branch and bound method
3. The nearest neighbour method

While all of these methods provide optimal solutions to TSP, they are rarely useful beyond the boundaries of theoretical Computer Science.  Therefore, academics came up with Evolutionary Optimization Algorithms. [6](https://www.sciencedirect.com/science/article/pii/S089812211101073X)

### 2.3.1 Evolutionary Optimization Algorithms
Finding an algorithm that reduces computation is necessary to solve the TSP.  The Ant Colony Optimization (ACO) algorithm is a good fit for discrete and non-deterministic optimization problems like the TSP because the algorithm searched through the solution space efficiently.  Ordinarily, genetic algorithms and simulated annealing provide efficient and good solutions to the TSP but are more complex to implement and tune than ACO.  In sum, the ACO algorithm is a better fit to solve the TSP.




