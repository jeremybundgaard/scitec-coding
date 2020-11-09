# import csv
import sys
import numpy as np
import pandas as pd
import csv

import funcs

print ('\n')
print("SciTec_code_problem.py \n")


# Read the CSV file
csv_in="data/SciTec_code_problem_data.csv"
lla = np.genfromtxt(csv_in, delimiter=',')
print("read data/SciTec_code_problem_data.csv -> time, lat, lon, alt\n")

# create empty array for ECEF values
ecef = np.empty(np.shape(lla), int)

# Convert LLA to ECEF
for t in range(len(lla)):
	position_ecef = funcs.lla2ecef(lla[t,1],lla[t,2],lla[t,3])
	t = lla[t,0]
	x = position_ecef[0]
	y = position_ecef[1]
	z = position_ecef[2]
	newRow = np.array([[t],[x],[y],[z]]).T
	print(newRow)
	np.vstack((ecef,newRow))



# plotting these data with the wgs84 spheriod using PyGeodesy 20.10.30: https://pypi.org/project/PyGeodesy/
# install via terminal: $


# Calculate ECEF velocity at the time points given in the input file • Interpolate ECEF velocity for any requested time



print ('\n')
exit
