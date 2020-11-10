import numpy as np

#####################################################################
####    coordinate transformations on the WGS-84 spheriod:
####    [lat, lon, alt] -> [x, y, z] in ECEF
#####################################################################

def lla2ecef(lat, lon, alt):

	f = 1/298.257223563
	a = 6378137
	b = a*(1-f)
	e = np.sqrt((a**2-b**2)/a**2)

	# convert deg->radians
	rad=np.pi/180
	lat = lat*rad
	lon = lon*rad

	N = a/np.sqrt(1 - e**2*np.sin(lat)**2)
	x = (N+alt)*np.cos(lat)*np.cos(lon)
	y = (N+alt)*np.cos(lat)*np.sin(lon)
	z = ((b**2/a**2)*N+alt)*np.sin(lat)

	return [x, y, z]


#####################################################################
####    velocity interpolation 
#####################################################################

def interpolateVelocity(input_velocity, time):

	# redefine some local variables for readability 
	Vt = input_velocity[:,0]
	Vx = input_velocity[:,1]
	Vy = input_velocity[:,2]
	Vz = input_velocity[:,3]

	# Closeset Time Index
	iCls = np.abs(Vt-time).argmin()

	# determin Vt array indeces which contain the input time 
	if np.abs(Vt[iCls-1]) < np.abs(time) and np.abs(time) < np.abs(Vt[iCls]) :
		iUpper = iCls
		iLower = iCls-1
	elif np.abs(Vt[iCls]) < np.abs(time) and np.abs(time) < np.abs(Vt[iCls+1]) :
		iUpper = iCls+1
		iLower = iCls

	# print("\n")
	# print("upper Bound   Vt[",iUpper,"]: ",Vt[iUpper],'\n')
	# print("time to be interpolated: ",time,'\n')
	# print("lower Bound   Vt[",iLower,"]: ",Vt[iLower],'\n')
	# print("\n")

	time_bounds = [ Vt[iLower], Vt[iUpper] ]
	Vx_bounds   = [ Vx[iLower], Vx[iUpper] ]
	Vy_bounds   = [ Vy[iLower], Vy[iUpper] ]
	Vz_bounds   = [ Vz[iLower], Vz[iUpper] ]

	Vx_interp = np.interp(time, time_bounds, Vx_bounds)
	Vy_interp = np.interp(time, time_bounds, Vy_bounds)
	Vz_interp = np.interp(time, time_bounds, Vz_bounds)
	
	# graphical validation
	import matplotlib.pyplot as plt
	import matplotlib.ticker as mtick
	fig, ax = plt.subplots()
	plt.subplots_adjust(left=0.15, bottom=0.15, right=0.95, top=0.9)
	plt.ylabel('Velocity')
	plt.xlabel('time')
	plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
	ax.set_xticks([time_bounds[0],time,time_bounds[1]])
	ax.set_xticklabels([time_bounds[0],time,time_bounds[1]])
	plt.xticks(rotation=-10)
	plt.title('velocity interpolation at time:'+str(time))

	ax.plot(time_bounds, Vx_bounds, 'ro--', linewidth=1, markersize=12)
	ax.plot(time_bounds, Vy_bounds, 'go--', linewidth=1, markersize=12)
	ax.plot(time_bounds, Vz_bounds, 'bo--', linewidth=1, markersize=12)
	ax.plot(time, Vx_interp, 'yo', linewidth=2, markersize=12)
	plt.gca().legend(('Vx_bounds','Vy_bounds','Vz_bounds','V_interp'))
	ax.plot(time, Vy_interp, 'yo', linewidth=2, markersize=12)
	ax.plot(time, Vz_interp, 'yo', linewidth=2, markersize=12)
	plotname='Vxyz_interpolation_time'+str(time)+'.png'
	fig.savefig(plotname, dpi=100)

	Vxyz_interp_out = [time, Vx_interp ,Vy_interp, Vz_interp]

	
	print("     time_bounds      : ",time_bounds)
	print("     Vx_bounds        : ",Vx_bounds)
	print("     Vy_bounds        : ",Vy_bounds)
	print("     Vz_bounds        : ",Vz_bounds)
	print("     Vxyz_interp_out  : ",Vxyz_interp_out,'\n')
	print("     See",plotname,"for a graphical interpolation validation")

	print('\n')

	return Vxyz_interp_out