from stylo import *

#ex 2.2
class Carte: # Définition de la classe

    def __init__(self,value,color):
        self.value = value
        self.color=color

    def getAttributs(self): 
        return (self.value,self.color)
    
    def getvalue(self): 
        return self.value
    
    def getcolor(self): 
        return self.color
    
    def setvalue(self,v): 
        if 2<=v<=14:
            self.value=v
            return True
        else:
            return False
    
    def setcolor(self,c):
        if c == 'spade' or 'diamond' or 'heart' or 'clubs' :
            self.color=c
            return True
        else:
            return False
        
c2 = Carte(13, 'heart')
c2.setcolor('spade')
c2.setvalue(8)
#-------------------------------
pen = Stylo("Rouge")
print(pen.getCouleur())
pen.setCouleur("Bleu")
print(pen.reservoir.getCouleur())
#-------------------------------
#ex 4.3
# self.paquetCarte est une liste