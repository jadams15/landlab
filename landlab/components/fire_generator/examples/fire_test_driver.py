""" fire_test_driver.py

Sample driver for the generate_fire component and FireGenerator class.

This file will use the default parameters to find the scale parameter for
the fire distribution. 

The fire time series is generated using that scale and shape parameters.
The histogram is sorted and plotted to verify the Weibull distribution.

Written by Jordan Marie Adams, 2013. 
"""
import os
from landlab.components.fire_generator.generate_fire import FireGenerator
from matplotlib import pyplot as plt

# Input text file name and location
filename = os.path.join(os.path.dirname(__file__), 'fire.txt')

# Initializing the FireGenerator() class from generate_fire.py'
FG = FireGenerator(filename)

# Finding the unknown scale parameter for the distribution
FG.get_scale_parameter()

# Finding a time series based on the Weibull distribution
FG.generate_fire_time_series()

# Sorting the fire series to test the distribution...
FG.fire_events.sort()

# Plotting the histogram to show the distribution.
ymax = int(FG.total_run_time)+1
yaxis = range(0, ymax)
#plt.plot(FG.fire_events)
plt.hist(FG.fire_events)
plt.show()
