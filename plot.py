import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2
Data = np.loadtxt(filename, skiprows = 33, delimiter = ','  ) # separated the matrix of data from the material
Material =  sys.argv[2] # adds an argument to change the title 
Color =  sys.argv[3] # lets you add color 
Stress= Data[:,3] # y axis data 
Strain = Data [:,7] # x axis data 
plt.plot(Strain, Stress, color = Color , label = 'darkgrey' , linestyle = '-.') # plots the variable
plt.xlabel('Strain') # adds x axis label 
plt.ylabel('Stress Mpa') # adds y axis label 
plt.title('Stress vs Strain for '+ Material) # adds the title for the graph 
plt.grid() # adds grid 
plt.show()
print(Stress) # dont think this did anything 
print(Strain) # or this ... 


# Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable
# ----------------------------------------------------------------------
#I had to split the files into separate files for this to work 
# this means only one specimin per data file 


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)
# ----------------------------------------------------------------------------------

def bestfit (x,y):
	mean_x = mean (x)
	mean_y = mean (y)
	z = np.sum(y*(x-mean_x))/np.sum(x*(x-mean_x))
	z0 = mean_y - z*mean_x
	lin_arr = mp.linspace(0,10,100,True)
	degree_1 = z*lin_arr + z0
	return degree_1
Best_Fit = (Strain, Stress)
lin_arr = (0,10,100,True)
plt.plot(lin_arr, Best_Fit , color = 'darkgrey' , linestyle = '-.', label = 'Youngs Modulus')
plt.show();
exit ()	
# it doesnt seem to plot this so i added exit here instead 




## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.



