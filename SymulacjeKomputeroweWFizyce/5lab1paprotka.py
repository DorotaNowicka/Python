from scipy import linspace, polyfit, randn
from matplotlib.pyplot import plot, title, show , legend, rcParams, scatter, grid
from random import randint
import numpy

x, y = 0, 0
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)
m = [ [ 0.85, 0.04,-0.04, 0.85, 0.0, 1.6], [ 0.2,-0.26, 0.23, 0.22, 0.0, 1.6], [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44],[ 0.0, 0.0, 0.0, 0.16, 0.0, 0.0]]
prob = [0.73, 0.13, 0.11, 0.03]

for _ in range(10000):
    i =numpy.random.choice(4, p=prob)
    x_new = m[i][0]*x + m[i][1]*y + m[i][4]
    y_new = m[i][2]*x + m[i][3]*y + m[i][5] 
    xpoints.append(x_new)
    ypoints.append(y_new)
    x = x_new
    y = y_new

title('Paprotka')
#plot(xpoints,ypoints,'k.')
rcParams['axes.facecolor'] = 'pink'
scatter(xpoints, ypoints, s=1, marker="o", lw=0,
c=(0.,1.,0.))
show()

