# La forêt magique

## Génération de la forêt

Quelques règles lors de la génération aléatoire de la forêt:
* elle a une taille de 2 ou plus
* le joueur est positionné en (0, 0)
* un montre ou une crevasse ne peut pas se situer directement à droite ou en bas du joueur (soit en (1, 0) ou (0, 1))
* si un élément mortel (monstre ou crevasse) est généré à côté d'un autre élement mortel, l'indice généré autour (du caca de monstre ou du vent) ne remplace pas l'élément mortel