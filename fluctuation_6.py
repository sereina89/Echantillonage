from random import *
import matplotlib.pyplot as plt

### Initialisation
nombre_de_6 = 0
liste_lancers = []
liste_frequence = []


### Lancers des 10000 dés et stockage des résultats dans des listes
for n in range(1,10001):
    liste_lancers.append(n) # append : ajouter
    de=randint(1,6) # Tirage au sort du dé
    if de==6 :
        nombre_de_6 = nombre_de_6 + 1
    frequence = nombre_de_6/n
    liste_frequence.append(frequence)

#### représentations graphique
plt.xlabel("Nombre de lancers") # Titre de l'axe horizontal
plt.ylabel("Fréquence du 6") # Titre de l'axe vertical
plt.plot(liste_lancers, liste_frequence) # Tracé des points
plt.show() # Affiche le graphique
