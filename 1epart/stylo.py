from reservoir import *
class Stylo:
    def __init__(self, couleur):
        self.reservoir = Reservoir(couleur)

    def getCouleur(self):
        return self.reservoir.getCouleur()

    def setCouleur(self, couleur):
        self.reservoir.setCouleur(couleur)