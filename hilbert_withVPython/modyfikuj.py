''' functions for modifying points '''
from math import radians, sin, cos

def obrocY(vec, angle):
	x = vec[0]
	y = vec[1]
	z = vec[2]
	alfa = radians(angle)
	si = sin(alfa)
	co = cos(alfa)
	return ( x*co + z*si,
		y,
		-x*si + z*co)

def obrocX(vec, angle):
	x = vec[0]
	y = vec[1]
	z = vec[2]
	alfa = radians(angle)
	si = sin(alfa)
	co = cos(alfa)
	return (x,
		y*co - z*si,
		y*si + z*co)

def rzut(vec,d):
	x = vec[0]
	y = vec[1]
	z = vec[2]
	return(	x/(1+z/d),
		y/(1+z/d),
		0)

def resize( lista, k ):
	res = []
	for i in lista:
		res.append( (i[0]*k, i[1]*k, i[2]*k) )
	return res

''' Only this function is imported ''' 
def mod(lista, n):
	res = []
	CC = float(2**n - 1) / 2
	for i in lista:
		i = (i[0]-CC, i[1]+CC, i[2]-CC) # centers
		res.append( i )
	return res
