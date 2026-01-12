PROJECT DOCUMENTATION
Solving the Traveling Salesman Problem Using Genetic Algorithms

============================================================
1. INTRODUCTION
============================================================

The Traveling Salesman Problem (TSP) is one of the most well-known problems in
combinatorial optimization. The problem consists of finding the shortest
possible route that visits a set of cities exactly once and returns to the
starting city.

TSP belongs to the class of NP-hard problems, meaning that the time required
to find the optimal solution increases exponentially with the number of cities.
For this reason, heuristic and metaheuristic approaches, such as genetic
algorithms, are commonly used for large problem instances.

The purpose of this project is to implement a genetic algorithm to obtain an
efficient approximate solution to the Traveling Salesman Problem.

============================================================
2. PROBLEM DESCRIPTION
============================================================

Given a set of N cities, each defined by two-dimensional coordinates (x, y),
the objective is to:
- visit each city exactly once;
- return to the starting city;
- minimize the total travel distance.

The number of possible routes is (N - 1)!, which makes exhaustive search
computationally infeasible for large values of N.

============================================================
3. OVERVIEW OF GENETIC ALGORITHMS
============================================================

Genetic Algorithms (GAs) are optimization techniques inspired by the principles
of natural evolution. They operate on a population of candidate solutions and
apply evolutionary operators such as:
- selection;
- crossover;
- mutation;
- elitism.

By repeatedly applying these operators, the population evolves toward better
solutions over successive generations.

============================================================
4. SOLUTION REPRESENTATION
============================================================

4.1 Chromosome Representation

Each chromosome represents a possible solution to the TSP and is encoded as a
permutation of city indices.

Example:
[2, 0, 4, 1, 3]

This permutation defines the order in which the cities are visited.

------------------------------------------------------------

4.2 Population

The population consists of multiple chromosomes generated randomly, each
representing a valid TSP route.

============================================================
5. FITNESS FUNCTION
============================================================

The fitness function evaluates the quality of a solution. Since TSP is a
minimization problem, the fitness value is defined as the inverse of the total
route distance:

fitness = 1 / total_distance

In this way, shorter routes correspond to higher fitness values.

============================================================
6. GENETIC OPERATORS
============================================================

6.1 Selection – Tournament Selection

Selection is performed using the tournament selection method:
- k individuals are randomly selected from the population;
- the individual with the highest fitness is chosen as a parent.

This method provides a good balance between exploration and exploitation.

------------------------------------------------------------

6.2 Crossover – Order Crossover (OX)

Order Crossover is a recombination operator designed specifically for
permutation-based problems such as TSP. The procedure is as follows:
1. A random segment is selected from the first parent.
2. This segment is copied directly into the offspring.
3. The remaining cities are inserted in the order in which they appear in the
   second parent, avoiding duplicates.

------------------------------------------------------------

6.3 Mutation – Swap Mutation

Mutation is applied with a certain probability and consists of:
- selecting two random positions in the chromosome;
- swapping the cities at those positions.

This operator helps maintain genetic diversity and prevents premature
convergence.

------------------------------------------------------------

6.4 Elitism

Elitism ensures that the best individuals from the current generation are
carried over directly into the next generation, preserving high-quality
solutions.

============================================================
7. CITY GENERATION
============================================================

Cities are generated randomly in a two-dimensional space using real-valued
coordinates within a predefined range. This approach allows the algorithm to
be tested on different problem instances.

============================================================
8. ALGORITHM FLOW
============================================================

The main steps of the genetic algorithm are:
1. Random generation of cities
2. Initialization of the population
3. Fitness evaluation
4. Parent selection
5. Crossover application
6. Mutation application
7. Elitism application
8. Iteration over a fixed number of generations
9. Output of the best solution found

============================================================
9. RESULTS
============================================================

The genetic algorithm produces efficient approximate solutions for the
Traveling Salesman Problem. Although optimality is not guaranteed, the quality
of the solutions is high and the execution time remains reasonable even for
larger problem sizes.

============================================================
10. ADVANTAGES AND LIMITATIONS
============================================================

Advantages:
- suitable for large problem instances;
- flexible and easy to extend;
- does not require exhaustive search.

Limitations:
- does not guarantee the global optimum;
- performance depends on parameter tuning;
- results may vary between runs.

============================================================
11. CONCLUSIONS
============================================================

Genetic algorithms provide an effective approach for solving the Traveling
Salesman Problem approximately. By combining selection, crossover, mutation,
and elitism, high-quality solutions can be obtained within acceptable
computational time.

This project demonstrates the practical applicability of genetic algorithms
to complex optimization problems.
