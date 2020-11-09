# import csv
import sys
import numpy as np
import pandas as pd
import csv

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


import funcs

print ('\n')
print("SciTec_code_problem.py \n")


# Read the CSV file
csv_in="data/SciTec_code_problem_data.csv"
lla = np.genfromtxt(csv_in, delimiter=',')
print("read data/SciTec_code_problem_data.csv -> time, lat, lon, alt\n")

# create empty array for ECEF values
ecef = np.empty(np.shape(lla), float)

# Convert LLA to ECEF
for i in range(len(lla)):
	position_ecef = funcs.lla2ecef(lla[i,1],lla[i,2],lla[i,3])
	t = lla[i,0]
	x = position_ecef[0]
	y = position_ecef[1]
	z = position_ecef[2]
	newRow = np.array([[t],[x],[y],[z]]).T
	ecef[i] = newRow
	print(ecef[i,:])


# make some plots to see what these data look like
fig = plt.figure()
ax = plt.axes(projection="3d")

z_line = np.linspace(0, 15, 1000)
x_line = np.cos(z_line)
y_line = np.sin(z_line)
ax.plot3D(x_line, y_line, z_line, 'gray')

z_points = 15 * np.random.random(100)
x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv');

# plt.show()
fig.savefig('plot.png')

# Calculate ECEF velocity at the time points given in the input file • Interpolate ECEF velocity for any requested time



print ('\n')
# exit
