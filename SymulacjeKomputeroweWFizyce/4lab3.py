import numpy as np
import matplotlib.pyplot as plt

#parametry
G = 0.01
M = 500.0
m = 0.1
dt = 0.001
lk = 10000

#warunki początkowe
r0 = np.array([2.0, 0.0])
p0 = np.array([0, 0.1])

def sila(r):
    return (-G*M*m/((np.dot(r,r))**(3/2)))*r

def potencjalna(r):
    return (-G*M*m/(np.dot(r,r)**(1/2)))

def kinetyczna(p):
    return (np.dot(p,p))/(2*m)

def Leapfrog():
    #Utworzenie list na wyniki
    polozenia_x = []
    polozenia_y = []
    pedy_x = []
    pedy_y = []
    potencjaly = []
    kinetyczne = []
    #Początkowe dane
    r = r0
    polozenia_x.append(r[0])
    polozenia_y.append(r[1])
    p = p0
    pedy_x.append(p[0])
    pedy_y.append(p[1])
    #Pęd połówkowy
    p_pop = p0 - sila(r0)*dt/2
    for i in range(lk):
        #Siły i energie:
        F = sila(r)
        V = potencjalna(r)
        T = kinetyczna(p)
        kinetyczne.append(T)
        potencjaly.append(V)
        print(i) #kontrola postępu
        #Obliczanie danych w kolejnej chwili:
        p_next = p_pop+F*dt
        r = r + p_next*dt
        polozenia_x.append(r[0])
        polozenia_y.append(r[1])
        p = (p_next+p_pop)/2
        pedy_x.append(p[0])
        pedy_y.append(p[1])
        #aktualizacja:
        p_pop = p_next
    return [polozenia_x, polozenia_y, pedy_x, pedy_y, potencjaly, kinetyczne]
    

tor = Leapfrog()
energia_kin = tor[5]
energia_pot = tor[4]
energia_cal = []
print(len(energia_kin))
for i in range(len(energia_kin)):
    energia_cal.append(energia_kin[i]+energia_pot[i])

t = np.linspace(0, lk-1, lk)
print(len(t))

plt.plot(tor[0], tor[1], 'g', label='orbita')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('J')
plt.title(f'Leapfrog')
plt.grid()
plt.show()

plt.plot(t, energia_kin, 'g', label='energia kinetyczna')
plt.plot(t, energia_pot, 'b', label='energia potencjalna')
plt.plot(t, energia_cal, 'c', label='energia całkowita')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('J')
plt.title(f'Leapfrog')
plt.grid()
plt.show()

plt.plot(t, energia_cal, 'c', label='energia całkowita')
plt.show()