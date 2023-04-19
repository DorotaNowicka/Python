from scipy import linspace, polyfit, randn
import matplotlib.pyplot as plt 
from random import randint, random, uniform
import numpy as np
import matplotlib

N = 30
z =  np.array( [[7]*N]*N)
zs = 3

#dodawanie ziarenek
def dodaj_ziarnko():
    x = int(N/2)
    y = int(N/2)
    z[x][y] += 1

def przesypywanie(i):
    x=i[0]
    y=i[1]
    z[x][y]-=4
    if x-1>-1:
        z[x-1][y]+=1
    if x+1<N:
        z[x+1][y]+=1
    if y-1>-1:
        z[x][y-1]+=1
    if y+1<N:
        z[x][y+1]+=1






przepelnione = []


for t in range(3000):
    for x in range(N):
        for y in range(N):
            if z[x][y]>zs:
                przepelnione.append((x,y))
    if len(przepelnione) == 0:
        break
    while len(przepelnione)>0:
        przesypywanie(przepelnione[0])
        przepelnione.pop(0)      
      
    if(t%10==0):
        #rysowanie
        fig=plt.figure()
        ax=fig.add_subplot(111)
        ax.set_title('Height of the Sandpile')
        cax = ax.imshow(z, interpolation='nearest')
        cax.set_clim(vmin=0, vmax=8)
        cbar = fig.colorbar(cax, ticks=[0,3, 5, 8], orientation='vertical')
        filename = 'zad3' + str('%03d' % t) + '.png'
        plt.savefig(filename, dpi=100)
        plt.clf()

