import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from mpl_toolkits.mplot3d import axes3d

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
	ecef[i] = np.array([[t],[x],[y],[z]]).T
	np.set_printoptions(precision=30, suppress=True)
	# print(ecef[i,:])

print('\n')

# make some plots to see these data
fig2 = plt.figure(2)
# fig.set_size_inches(10,10)
ax3d = fig2.add_subplot(111, projection='3d')
ax3d.set_xlim3d(min(ecef[1:10,1]),max(ecef[1:10,1]))
ax3d.set_ylim3d(min(ecef[1:10,2]),max(ecef[1:10,2]))
ax3d.set_zlim3d(min(ecef[1:10,3]),max(ecef[1:10,3]))
ax3d.set_xlabel('x', fontsize=30)
ax3d.set_ylabel('y', fontsize=30)
ax3d.set_zlabel('z', fontsize=30)
t = ecef[:,0]
x = ecef[:,1]
y = ecef[:,2]
z = ecef[:,3]

from scipy.interpolate import splprep, splev
tck, u = splprep([x, y, z], s=0)
spline = splev(u, tck)

ax3d.scatter3D(spline[0],spline[1],spline[2], 'g-');
ax3d.scatter3D(x, y, z, 'r');
fig2.show()
plt.show()

# ax.scatter3D(x, y, z, c=t, cmap="RdYlGn_r");

########## rotate the axes and update ########## 
# for angle in range(0, 360,10):
#     ax.view_init(10, angle)
#     plt.draw()
#     plotname = 'ecef_angle'+str(angle)+'.png'
#     fig.savefig(plotname, dpi=100)
#     print('saved: ',plotname)


#####################################################################
# Calculate ECEF velocity at the time points given in the input file
#####################################################################
ecef_vel = funcs.ecef_velocity_data(ecef)

# t = ecef[:,0]
# x = ecef[:,1]
# y = ecef[:,2]
# z = ecef[:,3]
# ax.scatter3D(x, y, z);
# fig.set_size_inches(20,20)

# Interpolate ECEF velocity for any requested time



print ('\n')
# exit
