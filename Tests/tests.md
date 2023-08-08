
# 5. Tests
**If you want to skip this detailed analysis of each test scenario, you can jump to [this](#) excel sheet for a systematic summary and a brief, but methodical, analysis of the tests.**
### 5.1.1 Test 1: First execution
**At this point in time, [this](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/Tests/test-1.py) is the code I executed.**

**Times executed:** 3.

**Problem(s):**
1. The algorithm is stuck in a local optimum.
2. The city that the algorithm started with is not the city that the algorithm ended with.

**Analysis:**

The algorithm returned a solution that is not the global optimum.  There are 2 possibilities as to why the algorithm got stuck in a local optimum;
  1. Pheromone levels on edges are not updated enough, discouraging the ants to explore new paths.
  2. Time windows set are too restrictive.  The ants are not able to find a tour that satisfies all of the time windows.

The algorithm is free to explore different paths, even if the ants to do not start and end at the same city.

**Actions taken to improve code:**
1. Increase number of iterations.
2. Increase number of ants.
3. Adjust pheromone evaporation rate.
4. Relax time windows


### 5.1.2 Test 2: Check time windows
**At this point in time, [this](https://github.com/wafaajaunnoo/AntsInMyCode/blob/main/Tests/test-2.py) is the code I executed.**

Time(s)** executed:** 1.

**Problem:** Time windows are taken as digits instead of hours/minutes/seconds.

**Analysis:**


**Actions taken to improve code:**
  1. Change format for time windows to `{hour}:{minute}`

### 5.1.3 Test 3: Check pheromone levels
**At this point in time, [this](#) is the code I executed.**

Time(s)** executed:** 1.

**Problem:** Describe what was the pheromone level from the code.

**Analysis:** Describe why the pheromone levels were not dynamic int he code


**Action taken to improve code:** Make pheromone levels dynamic.

#### Optimal Path Identification
The algorithm should correctly identify the best path or
schedule that optimizes the defined objective(s) of the complex combinatorial problem.
