
import numpy as np

# 	coordinate transformations on the WGS-84 spheriod: [lat, lon, alt] -> [x, y, z] in ECEF
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


# coordinate transformations on the WGS-84 spheriod: [lat, lon, alt] -> [x, y, z] in ECEF
def ecef_velocity(ecef):

	t = ecef[:,0]
	x = ecef[:,1]
	y = ecef[:,2]
	z = ecef[:,3]

	for i in range(1,len(ecef)):
		Vx = (x[i-1]-x[i])/(x[i-1]-x[i])
		Vy = (y[i-1]-y[i])/(y[i-1]-y[i])
		Vz = (z[i-1]-z[i])/(z[i-1]-z[i])

	return ecef_velocity
