import matplotlib.pyplot as plt
import numpy as np
import sys


filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
test1stress = np.loadtxt(filename, delimiter = " ", skiprows = 32, usecols = (1), max_rows = 1000)   # Attempts to load filename into local variable data.
test2stress = np.loadtxt(filename, delimiter = " ", skiprows = 1051, usecols = (1), max_rows = 1000)
test3stress = np.loadtxt(filename, delimiter = " ", skiprows = 2070, usecols = (1), max_rows = 1000) 
test1strain = np.loadtxt(filename, delimiter = " ", skiprows = 32, usecols = (5), max_rows = 1000)   # Attempts to load filename into local variable data.
test2strain = np.loadtxt(filename, delimiter = " ", skiprows = 1051, usecols = (5), max_rows = 1000)
test3strain = np.loadtxt(filename, delimiter = " ", skiprows = 2070, usecols = (5), max_rows = 1000)



## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw
# Make sure to include axis labels and units!
# plt.plot(xdata, ydata, arguments-to-make-plot-pretty)
plt.plot(test1strain, test1stress)
plt.show()
## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable

# Don't worry about deleting parts you might need later -- that's why we use git!


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.


