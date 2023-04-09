# Fonction pour calculer la somme de deux vecteurs
def somme_vecteurs(vecteur1, vecteur2):
    if len(vecteur1) != len(vecteur2):
        return "Erreur: Les vecteurs n'ont pas la même dimension"
    else:
        return [vecteur1[i] + vecteur2[i] for i in range(len(vecteur1))]

# Exemple d'utilisation de la fonction
vecteur1 = [1, 2, 3]
vecteur2 = [4, 5, 6]
somme = somme_vecteurs(vecteur1, vecteur2)
print(somme)
