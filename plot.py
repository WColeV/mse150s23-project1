import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
from sklearn import linear_model
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
## linear regression calculations and plot of lin reg line vs data
x = np.array(np.loadtxt(filename, delimiter = " ", skiprows = 32, usecols = (5), max_rows = 1000))
y = np.array(np.loadtxt(filename, delimiter = " ", skiprows = 32, usecols = (1), max_rows = 1000))

# Create a design matrix with a column of ones for the intercept
X = np.vstack([x, np.ones(len(x))]).T

# Use the linear algebra function lstsq to find the coefficients
coef, residuals, _, _ = np.linalg.lstsq(X, y, rcond=None)

# Print the coefficients
print("the coef are", coef)
# Print the coefficients

#turning test data into 1d arrays for lin reg to work
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)

## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.


