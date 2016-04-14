from visual import *
import sys
from generuj import hilbert3D
from modyfikuj import mod

''' default variables '''
X = 0
Y = 0
Z = 0

''' List with points '''
lista = [(X,Y,Z)]

''' arguments '''
N = int(sys.argv[1])

''' Generating and modifying '''
hilbert3D(lista, N)
lista = mod(lista, N)


''' Generating curve in PARTS '''
tab = []
for i in range(len(lista)):
	if i and i%512 == 0:
		curve(pos=tab, radius=0.10)
		tab = []
	elif i == len(lista)-1:
		tab.append(lista[i])
		curve(pos=tab, radius=0.10)
	else:
		tab.append(lista[i])