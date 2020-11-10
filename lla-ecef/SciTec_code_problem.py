import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from mpl_toolkits.mplot3d import axes3d

import funcs

print ('\n')
print("SciTec_code_problem.py \n")

#####################################################################
# Read the CSV file
#####################################################################

print("Read the CSV file: data/SciTec_code_problem_data.csv ... ")

csv_in="data/SciTec_code_problem_data.csv"
lla = np.genfromtxt(csv_in, delimiter=',')

print("DONE\n")
#####################################################################
# Convert LLA to ECEF
#####################################################################

print("Converting input LLA timeseries to ECEF ... ")

# create empty array for ECEF values
ecef = np.empty(np.shape(lla), float)

for i in range(len(lla)):
	position_ecef = funcs.lla2ecef(lla[i,1],lla[i,2],lla[i,3])
	t = lla[i,0]
	x = position_ecef[0]
	y = position_ecef[1]
	z = position_ecef[2]
	ecef[i] = np.array([[t],[x],[y],[z]]).T
	np.set_printoptions(precision=30, suppress=True)
	# print(ecef[i,:])

print("DONE\n")

#####################################################################
# Calculate ECEF velocity at the time points given in the input file
#####################################################################
print("Calculating ECEF velocity at the time points given in the input file ... ")

# create empty velocity array for loop
ecef_velocity = np.zeros(np.shape(ecef))

for i in range(1,len(ecef)):
	Vx = (ecef[i,1]-ecef[i-1,1])/(ecef[i,0]-ecef[i-1,0])
	Vy = (ecef[i,2]-ecef[i-1,2])/(ecef[i,0]-ecef[i-1,0])
	Vz = (ecef[i,3]-ecef[i-1,3])/(ecef[i,0]-ecef[i-1,0])
	ecef_velocity[i] = np.array([[ecef[i,0]],[Vx],[Vy],[Vz]]).T
	# print(ecef_velocity[i,:],'\n')

print("DONE\n")

#####################################################################
# Interpolate ECEF velocity for any requested time
#####################################################################
print("Interpolating ECEF velocity for the requested time: 1532333000")
funcs.interpolateVelocity(ecef_velocity, 1532333000)

print("Interpolating ECEF velocity for the requested time: 1532335268")
funcs.interpolateVelocity(ecef_velocity, 1532335268)


#####################################################################
# Interpolate ECEF velocity for any requested time
#####################################################################

# # makes some plots to see these data
# fig = plt.figure(2)
# fig.set_size_inches(10,10)
# ax3d = fig.add_subplot(111, projection='3d')
# ax3d.set_xlim3d(min(ecef[:,1]),max(ecef[:,1]))
# ax3d.set_ylim3d(min(ecef[:,2]),max(ecef[:,2]))
# ax3d.set_zlim3d(min(ecef[:,3]),max(ecef[:,3]))
# ax3d.set_xlabel('x', fontsize=30)
# ax3d.set_ylabel('y', fontsize=30)
# ax3d.set_zlabel('z', fontsize=30)

# t = ecef[:,0]
# x = ecef[:,1]
# y = ecef[:,2]
# z = ecef[:,3]

# for i in range(len(ecef)):
# 	if i%25 != 0:
# 		print()
# 		t[i] = 0
# 		x[i] = 0
# 		y[i] = 0
# 		z[i] = 0

# ######### rotate the axes and update ########## 
# for angle in range(0, 360,10):
# 	ax3d.view_init(10, angle)
# 	plotname='ecef_angle'+str(angle)+'.png'
# 	ax3d.plot(spline[0],spline[1],spline[2], 'g-')
# 	ax3d.scatter3D(x, y, z, 'r*')
# 	# plt.show()
# 	fig.savefig(plotname, dpi=100)
# 	print('saved: ',plotname)
# 	fig.canvas.flush_events()
    

print("SciTec Coding Problem Completed \n")


exit
