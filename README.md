Final Project Repository - The Knapsack Problem
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Logo_de_l%27Université_Jean_Monnet_Saint-Etienne.png/640px-Logo_de_l%27Université_Jean_Monnet_Saint-Etienne.png" alt="Université Jean Monnet" title="Université Jean Monnet">
============

This repository contains the source code presented on the final project of the Advanced Algorithms class, MLDM Cohort 2022-2024, Université Jean Monnet. The members of this group and contributors to this repository include Ariel Guerra-Adames, Mohamed Moudjahed, Franck Sirguey, Thomas Martinerie, and Josh Trivedi.

---
## Project Description
This project aimed at implementing and exhaustively testing the performance of different popular approaches to solve the 0/1 Knapsack Problem.

Algorithms or approaches implemented and tested: 
- [Brute Force](bruteforce.py)
- [Meet in the Middle](middle.py)
- [Backtracking](backtracking.py)
- [Branch and Bound](BaB.py)
- [Dynamic programming](dynamic.py)
- [Greedy](greedy.py)
- [Genetic](genetic.py)
- [Fully Polynomial-Time Approximation Scheme](poly.py)
- [Randomized](randomize.py)
- Multi-knapsack adaptations of the [brute force](multiBruteForce.py) and [greedy](multigreedy.py) approaches.

Additionally, this repository contains [files facilitating the extraction of data](extract.py) contained in the low-dimensional and multiple knapsack data directories, as well as a customizable [problem generator](problem_generator.py). 

## Datasets Used for Testing
Data used for experimenting on these algoritms was extracted from the following sources:
- [Dataset for the low-dimensional 0/1 knapsack problem](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/)
- [Dataset for the multiple knapsack problem](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_multiple/knapsack_multiple.html)
