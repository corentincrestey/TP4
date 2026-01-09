class Carte:
    
    def __init__(self, nom, couleur):
        # Affectation de l'attribut nom et de l'attribut couleur
        couleurs = ('carreau', 'coeur', 'trefle', 'pique')
        noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi', 'as']
        valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'valet': 11, 'dame': 12, 'roi': 13, 'as': 14}
        
        if couleur in couleurs:
            self.couleur=couleur
        else:
            print("erreur de couleur")
        if nom in noms:
            self.nom=nom
        else:
            print("erreur de nom")
        
        self.valeur=valeurs[nom]

    def getattribute(self):
        return (self.nom, self.couleur, self.valeur)
    def setNom(self, nom):
        if nom in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi', 'as']:
            self.nom=nom
        else:
            print("erreur de nom")
        
        self.valeur={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'valet': 11, 'dame': 12, 'roi': 13, 'as': 14}[nom]
    def getNom(self):
        return self.nom
    def getCouleur(self):
        return self.couleur
    def getValeur(self):
        return self.valeur
    def egalite(self, carte):
        return self.valeur == carte.getValeur()
    def estSuperieureA(self, carte):
        return self.valeur > carte.getValeur()
    def estInferieureA(self, carte):
        return self.valeur < carte.getValeur()

"""c1 = Carte("valet", "coeur")
print(c1.getattribute())
c2 = Carte("as", "pique")
print(c2.getattribute())
c2.setNom('roi')
print(c2.getattribute())
c3 = Carte("8", "trefle")
def c1compare(c):
    print(f'c1 = c. : {c1.egalite(c)}')
    print(f'c1 > c. : {c1.estSuperieureA(c)}')
    print(f'c1 < c. : {c1.estInferieureA(c)}\n')

c1compare(c2)
c1compare(c3)"""


class Piece:
    def __init__(self,nom,surface):
        self.nom = nom
        self.surface = float(surface)

    def getSurface(self):
        return self.surface
    
    def getNom(self):
        return self.nom
    
    def setSurface(self,s):
        self.surface = float(s)


class Appartement:
    def __init__(self,nom):
        self.listeDePieces=[]
        self.nom=nom

    def getNom(self):
        return self.nom

    def ajouter(self,Piece):
        self.listeDePieces += [Piece]

    def nbPieces(self): 
        return len(self.listeDePieces)

    def SurfaceTotale(self):
        st = 0
        for i in self.listeDePieces:
            st += i.getSurface()
        return st

    def getListePieces(self):
        rooms = []
        for i in self.listeDePieces:
            rooms += [i.getNom()]
        return rooms
    
appart205 = Appartement("205")
chambre1 = Piece("chambre1", 20.00)
appart205.ajouter(chambre1)
sejour = Piece("sejour", 25.00)
appart205.ajouter(sejour)
cuisine = Piece("cuisine", 12.00)
appart205.ajouter(cuisine)

print(appart205.SurfaceTotale())
print(appart205.getListePieces())