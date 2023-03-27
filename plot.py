import matplotlib.pyplot as plt
import numpy as np
import sys
from statistics import mean
## loading in filename and test data
filename = sys.argv[1]
test1stress = np.loadtxt(filename, delimiter = " ", skiprows = 32, usecols = (1), max_rows = 1000)
test2stress = np.loadtxt(filename, delimiter = " ", skiprows = 1051, usecols = (1), max_rows = 1000)
test3stress = np.loadtxt(filename, delimiter = " ", skiprows = 2070, usecols = (1), max_rows = 1000)
test1strain = np.loadtxt(filename, delimiter = " ", skiprows = 32, usecols = (5), max_rows = 1000)
test2strain = np.loadtxt(filename, delimiter = " ", skiprows = 1051, usecols = (5), max_rows = 1000)
test3strain = np.loadtxt(filename, delimiter = " ", skiprows = 2070, usecols = (5), max_rows = 1000)
## Plotting the test data
plt.plot(test1strain, test1stress, color= 'r', label = 'Test1')
plt.plot(test2strain, test2stress, color= 'g', label = 'Test2')
plt.plot(test3strain, test3stress, color= 'b', label = 'Test3')
plt.xlabel("Strain(%)")
plt.ylabel("Stress(Pa)")
plt.title("Test1 Stress/Strain Curve")
plt.legend()
plt.show()
## linear regression calculations

def best_fit_slope(test1strain,test1stress):
    m = (((mean(test1strain)*mean(test1stress)) - mean(test1strain*test1stress)) /
         ((mean(test1strain)**2) - mean(test1stress**2)))
    return m

m = best_fit_slope(test1strain,test1stress)
print("youngs Modulus is", m)

