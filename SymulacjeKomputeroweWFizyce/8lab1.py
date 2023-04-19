from scipy import linspace, polyfit, randn
import matplotlib.pyplot as plt 
from random import randint, random, uniform
import numpy as np

L = 100
N = 1000
siatka = np.array( [[0]*100]*100)
pattern_x = [50]
pattern_y = [50]
R_wew = 2
R_zew = 5*R_wew
R_a = 0
siatka[50][50] = 1
print(siatka[0][50])
print(siatka[50][50])


for czastka in range(N):
    #wylosuj x i y
    theta = uniform(0, 2*np.pi)
    x = int(50 + round(R_wew*np.cos(theta)))
    y = int(50 + round(R_wew*np.sin(theta)))
    rozwazana = 1
    dodano = 0
    while rozwazana == 1:
        #przesuń się
        p_kierunku = randint(1,4)
        if p_kierunku == 1:
            x -= 1
        elif p_kierunku == 2:
            y += 1
        elif p_kierunku == 3:
            x += 1
        elif p_kierunku == 4:
            y -= 1
        #sprawdź czy wyszła poza r_zew
        if (x-50)**2 + (y-50)**2 > R_zew**2:
            break
        #sprawdź czy jest na przylepiającym polu:
        try: 
            """
            print(siatka[x-1][y])
            print(siatka[x+1][y])
            print(siatka[x][y-1])
            print(siatka[x][y+1])
            """
            if siatka[x-1][y] == 1 or siatka[x+1][y] == 1 or siatka[x][y-1] == 1 or siatka[x][y+1] == 1:
                pattern_x.append(x)
                pattern_y.append(y)
                siatka[x][y]=1
                rozwazana = 0
                dodano = 1
        except IndexError:
            break        
        #sprawdź czy zmienił się promień agregatu
        if dodano == 1:
            if (x-50)**2 + (y-50)**2 > R_a**2:
                R_a = np.sqrt((x-50)**2 + (y-50)**2)
                R_wew = max(5, R_a+2)
                R_zew = min(5*R_wew, R_wew+15)
    if(czastka%100==0):
        plt.xlim((0,L)) # obszar do narysowania
        plt.ylim((0,L))
        plt.scatter(pattern_x,pattern_y , c='#000000', s=1)
        nStr=str(czastka) #nagraj na dysk – numer pliku z 5 cyframi, na początku zera, np 00324.png
        nStr=nStr.rjust(5,'0')
        plt.title("agregat"+nStr)
        plt.savefig('./8lab_togif/shorter/8lab'+nStr+'.png') 

plt.scatter(pattern_x, pattern_y, c='#000000', s=1)
plt.show()





