import numpy as np
import matplotlib.pyplot as plt
import random
from numpy import array, dot, sqrt
from matplotlib.patches import Circle

nx = 4
ny = 4
particleNumber = nx*ny
b=8
b2 = b/2
eps=1.0
sigma=1.0
promien=0.3
deltat=0.001
temp=2.5
delta = 1.0
t = 0.0
t_max = 10
en = 0
#parametry siły:
sigma = 1
epsilon = 1


def sila(p1, p2):
    x = p2.r[0]-p1.r[0]
    y = p2.r[1]-p1.r[1]
    r12 = (x**2+y**2)**(1./2)
    wspolczynnik = 48.0*((1./r12)**14-((1./r12)**8)/2)
    return [-1.0*wspolczynnik*x, -1.0*wspolczynnik*y]


class czastka:
    """Klasa opisująca pojedynczą cząstkę"""
    def __init__(self, promien, pos, vel):
        self.promien = promien
        self.r = pos
        self.v = vel


particles = []
for i in range(nx):
    for j in range(ny):
        polozenie = array([i*delta, j*delta])
        predkosc=array([(random.random()-1./2),(random.random() -1./2)])
        particles.append(czastka(promien,polozenie,predkosc) )

for p in particles:
    print(f'położenie 0: {p.r}, prędkość 0: {p.v}')


sumv=0.0
sumv2=0.0
for p in particles:
    sumv=sumv+p.v
sumv=sumv/particleNumber 
for p in particles:
    p.v=(p.v-sumv) 
for p in particles:
    sumv2=sumv2+dot(p.v,p.v)/2.0
sumv2=sumv2/particleNumber 
fs=sqrt(temp/sumv2) 
for p in particles:
    p.v=p.v*fs 


while t < t_max:
    #RYSOWANIE
    #if True:
    if (en%100==0): # co 100-na klatka
        plt.clf() # wyczyść obrazek
        F = plt.gcf() # zdefiniuj nowy
        for i in range(particleNumber): # pętla po cząstkach
            p = particles[i]
            a = plt.gca() # ‘get current axes’ (to add smth to them)
            cir = Circle((p.r[0],p.r[1]), radius=p.promien) # kółko tam gdzie jest cząstka
            a.add_patch(cir) # dodaj to kółko do rysunku
            plt.plot() # narysuj
        plt.xlim((0,b)) # obszar do narysowania
        plt.ylim((0,b))
        F.set_size_inches((6,6)) # rozmiar rysunku
        nStr=str(en) #nagraj na dysk – numer pliku z 5 cyframi, na początku zera, np 00324.png
        nStr=nStr.rjust(5,'0')
        plt.title("Symulacja gazu Lennarda-Jonesa, krok "+nStr)
        plt.savefig('img'+nStr+'.png') 
    
    #SIŁA
    
    #najbliższy obraz:
    for i in range(len(particles)):
        sily = []
        for j in range(len(particles)):
            if i != j:
                r_vect = particles[j].r-particles[i].r # wektor pomiędzy cząstkami i oraz j
                l_r_vect = dot(r_vect, r_vect)**(1./2)
                if l_r_vect < 2.5:
                    #warynki brzegowe
                    if r_vect[0] > b2: # b2 – połowa pudełka b2=b/2
                        r_vect[0] = r_vect[0]-b # przesuwamy współrzędną x wektora r_vect
                    elif r_vect[0] <-b2:
                        r_vect[0] =r_vect[0]+b # b – bok pudełka
                    if r_vect[1] > b2: # to samo dla y
                        r_vect[1] =r_vect[1] -b
                    elif r_vect[1] <-b2:
                        r_vect[1] =r_vect[1] +b
                    if r_vect[0] < -8:
                        print("tu!")
                    if r_vect[0] > 8:
                        print("tu!")
                    sily.append(sila(particles[i], particles[j]))

        

        #Obliczanie siły
        Fx = 0
        Fy = 0
        for pojsila in sily:
            Fx += pojsila[0]
            Fy += pojsila[1]
        F = array([Fx, Fy])
        p = particles[i]
        
        #aktualizacja prędkości
        p.v = p.v + F*deltat
        print(f'położenie {en+1}: {p.r}, prędkość {en+1}: {p.v}')
        #aktualizacja położeń
        p.r = p.r + p.v*deltat

        #warunki brzegowe
        if p.r[0] > b:
            p.r[0] -= b
        if p.r[0] < 0:
            p.r[0] += b
        if p.r[1] >b:
            p.r[1] -= b
        if p.r[1] < 0:
            p.r[1] += b

    if (en%100==0):            
        for p in particles:
            print(f'położenie {en+1}: {p.r}, prędkość {en+1}: {p.v}')


    t = t + deltat
    en += 1


