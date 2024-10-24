# Random Numbers, Prime Sequences, and Data Visualization in Python

## Project Overview
This project focuses on generating random numbers, working with prime numbers, and visualizing data using libraries like `numpy`, `matplotlib`, and `scipy`. The tasks cover basic statistical simulations, plotting techniques, and prime number analysis.

## Task 1: Generate Uniformly Distributed Numbers
The script imports the `numpy` library and generates 1000 uniformly distributed random numbers in the interval [0, 1) using `np.random.random(...)`.

## Task 2: Generate Normally Distributed Numbers
This script generates a list of 1000 random variables with normal distribution using `np.random.normal(...)`. Two distributions are generated:
- With mean 0 and variance 1.
- With mean 2.2 and variance 3.8.

## Task 3: Data Visualization with Matplotlib
Using the `matplotlib` library, the following visualizations are created from the data generated in Task 2:
- **Scatter Plot:** The consecutive observations from Task 2a (mean 0, variance 1) are plotted using dots without connecting lines.
- **Histogram:** A density-based histogram (30 bins) is created using the data from Task 2b (mean 2.2, variance 3.8).
- **Probability Density Function Plot:** Using `scipy.stats`, the probability density function is generated and plotted over the histogram with a red, dotted line.

## Task 4: Prime Number Sequence and Analysis
This program performs operations on prime numbers and visualizes the results:
- **Prime Numbers Generation:** A list of the first N prime numbers is generated without the use of external libraries (N is set to 114).
- **Prime Number Proportions:** A series is computed based on the difference between consecutive prime numbers and their ratios to the smaller prime. The formula used is:  
  \[(p(i+1) – p(i)) / p(i)\]
- **Line Plot:** The series obtained in the previous step is plotted using a black line.
- **Plot Title Information:** The sum of the first N prime numbers is computed and displayed in the title of the plot. The program also checks if this sum is a prime number, and the title informs whether it is prime and, if so, which prime number it is (e.g., "The sum is 7, which is the 4th prime number").

## Libraries Used
- **NumPy** for random number generation and mathematical operations.
- **Matplotlib** for plotting and data visualization.
- **SciPy** for generating the probability density function.
