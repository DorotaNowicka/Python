from scipy import linspace, polyfit, randn
from matplotlib.pyplot import plot, title, show , legend
from random import randint

x, y = 0, 0
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)
m = [[0.5, 0, 0, 0.5, 0.0, 0], [0.5, 0, 0, 0.5, 0.5, 0], [0.5, 0, 0, 0.5, 0.25, ((3.)**(1/2))/4]]
p = [1./3, 1./3, 1./3]

for _ in range(10000):
    i = randint(0, 2)
    x_new = m[i][0]*x + m[i][1]*y + m[i][4]
    y_new = m[i][2]*x + m[i][3]*y + m[i][5] 
    xpoints.append(x_new)
    ypoints.append(y_new)
    x = x_new
    y = y_new

title('Trójkąt Sierpińskiego')
plot(xpoints,ypoints,'k.')
show()

