import math
import random as rnd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# TASK 1
N = 1000  # how many numbers we want to generate
N_list = []

for i in range(N):
    X_n = rnd.random()
    N_list.append(X_n)

# print(N_list)

# TASK 2
mean, var = 0, 1  # mean and variance
std = math.sqrt(var)
s = np.random.normal(mean, std, N)
# print(s)

mean1, var1 = 2.2, 3.8  # mean and variance
std1 = math.sqrt(var1)
s1 = np.random.normal(mean1, std1, N)
# print(s1)

# TASK 3
plt.plot(s, '.')
plt.show()

hist = plt.hist(s1, density=True, bins=30, alpha=0.7)
x = np.linspace(s1.min(), s1.max(), N)
y = norm.pdf(x, mean1, std1)
plt.plot(x, y, 'r:')

plt.xlabel('Data')
plt.ylabel('Frequency / Probability Density')
plt.title('Histogram with Probability Density Function')
plt.show()


# TASK 4
def isPrime(n):
    if (n == 1 or n == 0):
        return False
    # loop from 2 to n-1
    # without n+1 => N, because every number divide by itself
    for i in range(2, n):
        if (n % i == 0):
            return False
    # number first must exit the for loop
    return True


def get_sum(N_list):
    Sum = sum(N_list)
    return Sum


print('Print list of prime numbers from 1 to N, enter N: ')
N = input()
N_number = N.isnumeric()
N_list = []
while N_number is False:
    print('Please enter number!')
    N = input()
    N_number = N.isnumeric()
else:
    # loop from 1 to N
    for i in range(1, int(N) + 1):
        if (isPrime(i)):
            N_list.append(i)

print(N_list)

proportions = []
n = len(N_list)
for i in range(1, n):
    p_i = N_list[i - 1]
    p_i1 = N_list[i]
    print(p_i1)
    diff = p_i1 - p_i
    prop = diff / p_i
    proportions.append(prop)

print(proportions)

N_sum = get_sum(N_list)
# print(N_sum)
N_sum_list = []
if (isPrime(N_sum)):
    for i in range(1, int(N_sum) + 1):
        if (isPrime(i)):
            N_sum_list.append(i)
            # print(N_sum_list)

    title = "The sum is " + str(N_sum) + ", which is a " + str(len(N_sum_list)) + "th prime number."
    # print(title)

else:
    title = "The sum is " + str(N_sum) + ", which is not a prime number."
    # print(title)

plt.plot(proportions, 'k')
plt.title(title)
plt.show()
