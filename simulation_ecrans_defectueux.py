from random import *
import matplotlib.pyplot as plt

def defectueux():
    valeur = random()
    if valeur<0.21:
        return True
    else:
        return False

def frequence_defectueux_echantillon(n):
    # renvoie la fréquence d'écran défectueux
    # dans un échantillon de taille n
    nb_defectueux = 0
    for i in range(n):
        if defectueux():
            nb_defectueux = nb_defectueux +1
    frequence = nb_defectueux/n
    return frequence

### Initialisation
liste_echantillon = []
liste_frequence = []


### simulation de 100 échantillons de taille 40 et stockage des résultats dans des listes
for i in range(100):
    liste_echantillon.append(i) # append : ajouter
    liste_frequence.append(frequence_defectueux_echantillon(40))

#### représentations graphique
plt.xlabel("Numéro de l'échantillon") # Titre de l'axe horizontal
plt.ylabel("Fréquence de défectueux") # Titre de l'axe vertical
plt.scatter(liste_echantillon, liste_frequence, marker='+') # Tracé des points
plt.show() # Affiche le graphique
