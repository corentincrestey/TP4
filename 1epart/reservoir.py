class Reservoir:
    ''' classe permettant de construire un réservoir d'encre
    pour des stylos toutes marques, toutes dimensions '''
    def __init__(self, couleur):
        ''' On se contente d'un seul paramètre pour l'exemple
        les dimensions ne seront donc pas incluses dans
        cette description '''
        # un seul attribut toujours par souci de clarté
        self.couleur = couleur
    # Accesseur de self.couleur
    def getCouleur(self):
        return self.couleur
    # Mutateur de self.couleur
    def setCouleur(self, couleur):
        self.couleur = couleur
