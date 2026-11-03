# script 1 : etude de l'effet du materiau sur une seule paroi,
#introduction de R
import numpy as np
import matplotlib.pyplot as plt
#parametres
R=float(input("Quel coefficient de réflexion du matériau?"))
celerite=343
frequence=float(input("Quelle frequence?"))
Amplitude=float(input("Quelle amplitude"))


#modelisation piece, maillage
l=float(input("Quelle largeur?"))
L=float(input("Quelle longueur?"))
points=np.array([[0,0],[0,l],[l,L],[0,L]])
plt.plot(points[:,0], points [:,1])
plt.axis('equal')
plt.grid()
plt.show()

pas_x=float(input("Quel pas selon x?"))
pas_y=float(input("Quel pas selon y?"))

x=np.arange(0,L+pas_x,pas_x)
y=np.arange(0,l+pas_y,pas_y)

X,Y=np.meshgrid(x,y)
plt.scatter(X,Y)
plt.axis('equal')
plt.grid()
plt.show()

#maillage

for i in range (len(x)):
    plt.axvline(x[i], color='grey', linewidth=0.5)
for j in range(len(y)):
    plt.axhline(y[j], color='grey', linewidth=0.5)
    
plt.xlim(0,L)
plt.ylim(0,l)
plt.axis('equal')
plt.show()

#modelisation mur et source
M=np.array([0,l, L,l])
Source=[l/2,L/2]

#Calcul du champ accoustique 
#chaque point represente un noeud 
#et à chaque noeud on va associer un signal
dt=float(input("Quel pas de temps?"))
temps_total=float(input("Quel temps total?"))

t=np.arange(0,temps_total,dt)

S=np.zeros((len(t),len(y),len(x)))

for n in range (len(t)-1):
    S[n,:,:]=np.sin(2*np.pi*2*frequence*t[n]-2*np.pi*frequence/celerite*X)

iter=int(input("Combien de temps différents observe-t-on?"))

for k in range (iter-1):
    n=int(input("Quel indice temporel afficher?"))
    plt.imshow(S[n,:,:],extent=[0,L,0,l], origin='lower', cmap='RdBu_r',aspect='equal')
    plt.colorbar(label='Valeur du signal s')
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title('Signal dans la piece')
    plt.show()
