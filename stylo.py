from reservoir import *
class Stylo:
    ''' classe permettant de construire un stylo
    avec un réservoir d'encre.
    On ne s'occupe pas de ses autres caractérisques'''
    def __init__(self, couleur):
        ''' On se contente d'un seul paramètre pour l'exemple
        les dimensions ou autres composants ne seront donc
        pas inclus dans cette description '''
        self.reservoir = Reservoir(couleur)
    # Accesseur du self.couleur de self.reservoir
    def getCouleur(self):
        return self.reservoir.getCouleur()
    # Mutateur du self.couleur de self.reservoir
    def setCouleur(self, couleur):
        self.reservoir.setCouleur(couleur)