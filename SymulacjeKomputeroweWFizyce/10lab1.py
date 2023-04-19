import numpy as np
import matplotlib.pyplot as plt

A=3
B=20
E=3
N0_ryb = 300
N0_rek = 10
N = 40
mapa = np.array( [[0]*N]*N)
nrki_obiektow = np.array( [[0]*N]*N)
sea = []

class Zwierze():
    def __init__(self, xposition, yposition, timetobirth):
        self.x = xposition
        self.y = yposition
        self.timetobirth = timetobirth
        self.time = np.random.randint(0, timetobirth)
        mapa[self.x][self.y] = 1
        self.zyje = True

    def death(self):
        self.zyje = False
        mapa[self.x][self.y] = 0


class Ryba(Zwierze):
    def __init__(self, xposition, yposition):
        super().__init__(xposition, yposition, A)   

    def krok(self):
        if self.zyje:
            pusci_sasiedzi = []
            if mapa[(self.x+1)%N][self.y]==0:
                pusci_sasiedzi.append((x+1, y))
            if mapa[(self.x-1)%N][self.y]==0:
                pusci_sasiedzi.append((x-1, y))
            if mapa[self.x][(self.y+1)%N]==0:
                pusci_sasiedzi.append((x, y+1))
            if mapa[self.x][(self.y-1)%N]==0:
                pusci_sasiedzi.append((x, y-1))
            #new position:
            if len(pusci_sasiedzi)>0:
                mapa[self.x][self.y] = 0
                if self.time % self.timetobirth == 0:
                    sea.append(Ryba(x, y))
                i = np.random.randint(0, len(pusci_sasiedzi))
                self.x = pusci_sasiedzi[i][0]
                self.y = pusci_sasiedzi[i][1]
                mapa[self.x][self.y] = 1
            self.time += 1

class Rekin(Zwierze):
    def __init__(self, xposition, yposition, energia):
        super().__init__(xposition, yposition, B)  
        self.energia = np.random.randint(1, energia)
        self.e_max = energia
        mapa[self.x][self.y]=2

    def krok(self):
        self.energia -= 1
        if self.energia < 1:
            self.death()
        ryby_w_okolicy = []
        if self.zyje:
            if mapa[(self.x+1)%N][self.y]==1:
                ryby_w_okolicy.append((x+1, y))
            if mapa[(self.x-1)%N][self.y]==1:
                ryby_w_okolicy.append((x-1, y))
            if mapa[self.x][(self.y+1)%N]==1:
                ryby_w_okolicy.append((x, y+1))
            if mapa[self.x][(self.y-1)%N]==1:
                ryby_w_okolicy.append((x, y-1))
            #jeśli nie ma ryb
            if len(ryby_w_okolicy) == 0:
                pusci_sasiedzi = []
                if mapa[self.x+1][self.y]==0:
                    pusci_sasiedzi.append((x+1, y))
                if mapa[self.x-1][self.y]==0:
                    pusci_sasiedzi.append((x-1, y))
                if mapa[self.x][self.y+1]==0:
                    pusci_sasiedzi.append((x, y+1))
                if mapa[self.x][self.y-1]==0:
                    pusci_sasiedzi.append((x, y-1))
                #new position:
                if len(pusci_sasiedzi)>0:
                    mapa[self.x][self.y] = 0
                    if self.time % self.timetobirth == 0:
                        sea.append(Rekin(x, y, E))
                    i = np.random.randint(0, len(pusci_sasiedzi))
                    self.x = pusci_sasiedzi[i][0]
                    self.y = pusci_sasiedzi[i][1]
                    mapa[self.x][self.y] = 2
            #a jeśli są
            if len(ryby_w_okolicy)>0:
                mapa[self.x][self.y] = 0
                if self.time % self.timetobirth == 0:
                    sea.append(Rekin(x, y, E))
                i = np.random.randint(0, len(ryby_w_okolicy))
                new_x = ryby_w_okolicy[i][0]
                new_y = ryby_w_okolicy[i][1]
                mapa[self.x][self.y] = 2
                # ryba death
                sea[nrki_obiektow[new_x][new_y]].death()
                self.energia = self.e_max
                self.x = new_x
                self.y = new_y

            self.time += 1
             
for i in range(N0_ryb):
    x = np.random.randint(0,N-1)
    y = np.random.randint(0,N-1)
    sea.append(Ryba(x, y))
    nrki_obiektow[x][y] = i

for i in range(N0_ryb, N0_ryb + N0_rek):
    x = np.random.randint(0,N-1)
    y = np.random.randint(0,N-1)
    sea.append(Rekin(x, y, E))
    nrki_obiektow[x][y] = i

print(mapa)

for t in range(10):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_title('The sea')
    cax = ax.imshow(mapa, interpolation='nearest')
    cax.set_clim(vmin=0, vmax=2)
    cbar = fig.colorbar(cax, ticks=[0,3, 5, 8], orientation='vertical')
    filename = 'lab10' + str('%03d' % t) + '.png'
    plt.savefig(filename, dpi=100)
    plt.clf()
 
    for i in range(len(sea)):
        if i>301:
            print("rekin")
            print(sea[i].energia)
        if sea[i].zyje:
            sea[i].krok()

print(mapa)
 

