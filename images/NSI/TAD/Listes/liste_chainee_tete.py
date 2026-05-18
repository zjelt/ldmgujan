'''MODULE implémentant une Liste Chaînée MUABLE sous forme d'un objet stockant Tête

Description
-----------
* Une Liste VIDE est un objet dont l'attribut tete contient None
* Une Liste NON VIDE est un objet qui possède un attribut : tete
* Une Cellule est un objet qui possède deux attributs : v et s

Primitives de la classe Cellule
-------------------------------

+ LIN : nb_cellules(self:'Cellule') -> int
+ CST : contenu(self:'Cellule') -> 'Element'
+ CST : successeur(self:'Cellule NON FIN') -> 'Cellule'


Méthodes de la classe Liste Tete-Fin
--------------------------------------
+ CST : Liste.est_liste_vide(self:'Liste') -> bool

+ CST : Liste.acces_tete(self:'Liste NON VIDE') -> Cellule
+ LIN : Liste.acces_fin(self:'Liste NON VIDE') -> Cellule
+ LIN : Liste.acces(self:'Liste NON VIDE', i:'int VALIDE') -> Cellule

+ CST : Liste.inserer_tete(self:'Liste', elt:'Element') -> None
+ LIN : Liste.inserer_fin(self:'Liste', elt:'Element') -> None
+ LIN : Liste.inserer(self:'Liste', elt:'Element', i:'int VALIDE') -> None

+ CST : Liste.supprimer_tete(self:'Liste NON VIDE') -> 'Element'
+ LIN : Liste.supprimer_fin(self:'Liste NON VIDE') -> 'Element'
+ LIN : Liste.supprimer(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element'

+ LIN : Liste.longueur(self:'Liste') -> int

+ CST : Liste.premier(self:'Liste NON VIDE') -> 'Element'
+ LIN : Liste.dernier(self:'Liste NON VIDE') -> 'Element'
+ LIN : Liste.ieme(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element'


Fonctions d'interface cachant l'aspect objet
---------------------------------------------
+ CST : nouvelle_liste() -> Liste
+ CST : est_liste_vide(lst:'Liste') -> bool

+ CST : inserer_tete(lst:'Liste', elt:'Element') -> None
+ LIN : inserer_fin(lst:'Liste', elt:'Element') -> None
+ LIN : inserer(lst:'Liste', elt:'Element', i:'int VALIDE') -> None

+ CST : supprimer_tete(lst:'Liste NON VIDE') -> 'Element'
+ LIN : supprimer_fin(lst:'Liste NON VIDE') -> 'Element'
+ LIN : supprimer(lst:'Liste NON VIDE', i:'int VALIDE') -> 'Element'

+ LIN : longueur(lst:'Liste') -> int

+ CST : premier(lst:'Liste NON VIDE') -> 'Element'
+ LIN : dernier(lst:'Liste NON VIDE') -> 'Element'
+ LIN : ieme(lst:'Liste NON VIDE', i:'int VALIDE') -> 'Element'


'''

class Cellule:
    '''Cellule (valeur, successeur)'''
     
    def __init__(self, valeur:'Element', successeur:'Cellule|None'):
        self.v = valeur      # Valeur ne peut pas être None si File homogène
        self.s = successeur  # successeur vaut None si Cellule de Fin     

    def nb_cellules(self:'Cellule') -> int:  #Coût Linéaire O(n)
        '''Renvoie le nombre de cellules dans la chaîne à partir de cette cellule'''
        if self.s is None:                  # si il n'y a pas de successeur
            return 1                        # il y a au moins la fin
        else:
            return 1 + self.s.nb_cellules()  # on demande au successeur...

    def contenu(self:'Cellule') -> 'Element':  # Coût constant
        '''Renvoie le contenu de la Cellule'''
        return self.v
     
    def successeur(self:'Cellule NON FIN') -> 'Cellule':  # Coût constant
        '''Renvoie la Cellule qui succède à une cellule NON FIN'''
        return self.s

class Liste:
    '''Liste chaînée MUABLE Tete'''
     
    def __init__(self):
        self.tete = None    

    def afficher(self:'Liste') -> None:  # Coût linéaire
        actuellement = self.acces_tete()
        while actuellement is not None:
            print(f"{actuellement.v} -> ", end='')
            actuellement = actuellement.s
        print('x') 
 
 
    def est_liste_vide(self:'Liste') -> bool:  # Coût constant
        '''Prédicat qui renvoie True si la liste est vide'''
        return self.tete is None
     
    def acces_tete(self:'Liste NON VIDE') -> Cellule:  # Coût constant
        '''Renvoie l'adresse de la cellule de Tête dans la liste NON VIDE'''
        return self.tete
    
    def acces_fin(self:'Liste NON VIDE') -> Cellule:  # Coût linéaire 𝞗(n)
        '''Renvoie l'adresse de la cellule de Fin dans la liste NON VIDE'''
        c = self.tete           
        while c.s is not None:  # TANT QUE la cellule ne mène pas à None (n'est pas la fin donc)
            c = c.s             # on passe à la cellule suivante
        return c                # on renvoie la cellule c qui est donc la fin
    
    def acces(self:'Liste NON VIDE', i:'int VALIDE') -> Cellule:  # Coût Linéaire O(n)
        '''Renvoie l'adresse de la cellule i dans la liste NON VIDE'''
        c = self.tete          # récupère la cellule de tête
        for _ in range(i):     # Faire i fois
            c = c.s            # passe au successeur
        return c
    
    def inserer_tete(self:'Liste', elt:'Element') -> None:  # coût constant
        '''Rajoute une nouvelle cellule contenant elt en tête de liste'''
        nouvelle = Cellule(elt, None)    # Etape 1 : création de la cellule
        nouvelle.s = self.tete           # Etape 2 : on relie la nouvelle cellule à l'"ancienne" Tête
        self.tete = nouvelle             # Etape 3 : modification de la liste    
  
    def inserer_fin(self:'Liste', elt:'Element') -> None:  # Coût constant
        '''Rajoute une nouvelle cellule de Fin contenant elt dans la liste'''
        if self.est_liste_vide():   # Si la liste est vide, on fait appel
            self.inserer_tete(elt)  # à inserer_tete()
        else:
            nouvelle = Cellule(elt, None)  # Etape 1 : on crée la nouvelle Cellule
            ancienne_fin = self.acces_fin()
            ancienne_fin.s = nouvelle

    def inserer(self:'Liste', elt:'Element', i:'int VALIDE') -> None:
        """Rajoute une nouvelle cellule contenant elt en position i VALIDE de la liste"""
        if i == 0:
            self.inserer_tete(elt)
        else:
            pred = self.acces(i-1)         # Etape 1 : recherche de la cellule i-1
            nouvelle = Cellule(elt, None)  # Etape 2 : création de la cellule
            nouvelle.s = pred.s            # Etape 3 : liaison nouvelle i vers ancienne i
            pred.s = nouvelle              # Etape 4 : liaison i-1 vers nouvelle i
 
    def supprimer_tete(self:'Liste NON VIDE') -> 'Elt':  # coût constant
        """Supprime la tête et renvoie son contenu"""
        memoire = self.tete.v      # Etape 1 : on mémorise l'ancienne valeur
        self.tete = self.tete.s    # Etape 2 : la tête devient le successeur de l'ancienne tête
        return memoire

    def supprimer_fin(self:'Liste NON VIDE') -> 'Element':  # Coût Linéaire θ(n)
        '''Supprime la cellule de fin d'une liste NON VIDE et renvoie l'élément qui y était stocké'''
         
        if self.tete.s is None:       # si la liste ne possède qu'une seule cellule
            return self.supprimer_tete() # on demande à l'autre fonction de faire le travail
        else :
            # Etape 1 : on cherche le prédécesseur c de la Fin
            c = self.tete             # on part de la tête
            while c.s.s is not None:  # tant que c n'est pas le prédécesseur de la Fin
                c = c.s               # on passe à la cellule suivante             
            ancienne_valeur = c.s.v   # Etape 2 : on mémorise la valeur de Fin actuelle
            c.s = None                # Etape 3 : on fait pointer le prédécesseur sur None
            return ancienne_valeur    # Etape 4 : on renvoie la valeur mémorisée
 
    def supprimer(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element':  # Coût linéaire θ(i) O(n)
        """Supprime la cellule en position i VALIDE et renvoie l'élément qui y était stocké"""
        if i == 0:                          # En réalité, on veut supprimer la Tête
            return self.supprimer_tete()
        else:
            pred = self.acces(i-1)      # Etape 1 : recherche de la cellule i-1
            ancienne_valeur = pred.s.v  # Etape 2 : on mémorise la valeur en position i actuellement
            pred.s = pred.s.s           # Etape 3 : on fait pointer le prédécesseur sur le successeur de son successeur
            return ancienne_valeur      # Etape 4 : on renvoie la valeur mémorisée

    def longueur(self:'Liste') -> int:  # Coût Linéaire θ(n) 
        '''Renvoie la longueur de la liste'''
        if self.est_liste_vide():
            return 0
        else:
            return self.tete.nb_cellules()
    
    def premier(self:'Liste NON VIDE') -> 'Element':  # Coût constant
        '''Renvoie l'élément stocké en Tête de liste NON VIDE'''
        return self.tete.v   
        
    def dernier(self:'Liste NON VIDE') -> 'Element':  # Coût linéaire
        '''Renvoie l'élément stocké en Fin de liste NON VIDE'''
        return self.acces_fin().v     

    def ieme(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element':  # Coût Linéaire O(n)
        '''Renvoie l'élément stocké en position i de la liste NON VIDE'''
        return self.acces(i).v    





# Primitives en version fonction pour cacher qu'on manipule un objet

def nouvelle_liste() -> 'Liste':  # Coût constant
    '''Renvoie une nouvelle liste vide'''
    return Liste()

def est_liste_vide(lst:'Liste') -> bool:  # Coût constant
    '''Prédicat qui renvoie True si la liste est vide'''
    return lst.est_liste_vide()

def inserer_tete(lst:'Liste', elt:'Element') -> 'None':  # Coût constant
    '''Rajoute elt en Tête de liste'''
    lst.inserer_tete(elt)
    
def inserer_fin(lst:'Liste', elt:'Element') -> 'None':  # Coût linéaire
    '''Rajoute elt en Fin de liste'''
    lst.inserer_fin(elt)
    
def inserer(lst:'Liste', elt:'Element', i:'int VALIDE') -> 'None':  # Coût linéaire
    '''Rajoute elt en Fin de liste'''
    lst.inserer(elt, i)
    
def supprimer_tete(lst:'Liste NON VIDE') -> 'Element':  # Coût constant
    '''Supprime la Tete d'une liste NON VIDE et renvoie l'élément qui y était stocké'''
    return lst.supprimer_tete()

def supprimer_fin(lst:'Liste NON VIDE') -> 'Element':  # Coût Linéaire θ(n)
    '''Supprime la Fin d'une liste NON VIDE et renvoie l'élément qui y était stocké'''
    return lst.supprimer_fin()

def supprimer(lst:'Liste', i:'int VALIDE') -> 'Element':  # Coût Linéaire O(n)
    '''Supprime l'élément en position i VALIDE et renvoie cet élément'''
    return lst.supprimer(i)

def longueur(lst:'Liste') -> int:  # Coût Linéaire θ(n) 
    '''Renvoie la longueur de la liste'''
    return lst.longueur()

def premier(lst:'Liste NON VIDE') -> 'Element':  # Coût constant
    '''Renvoie l'élément stocké en Tête de liste NON VIDE'''
    return lst.premier()
        
def dernier(lst:'Liste NON VIDE') -> 'Element':  # Coût constant
    '''Renvoie l'élément stocké en Fin de liste NON VIDE'''
    return lst.dernier() 

def ieme(lst:'Liste NON VIDE', i:'int VALIDE') -> 'Element':  # Coût Linéaire O(n)
    '''Renvoie l'élément stocké en position i VALIDE de la liste NON VIDE'''
    return lst.ieme(i)


 
 
if __name__ == '__main__':
    
    def tester_inserer_tete():
        print("Tests de inserer_tete())...", end="")
        lst = Liste()
        lst.inserer_tete(5)
        assert lst.tete.v == 5
        lst.inserer_tete(10)
        assert lst.tete.v == 10
        assert lst.tete.s.v == 5
        lst.inserer_tete(20)
        assert lst.tete.v == 20
        assert lst.tete.s.v == 10
        assert lst.tete.s.s.v == 5
        print("ok")
 
    def tester_supprimer_tete():
        print("Tests de supprimer_tete())...", end="")
        lst = Liste()
        lst.inserer_tete(5)
        lst.inserer_tete(10)
        lst.inserer_tete(20)
        lst.supprimer_tete()
        assert lst.tete.v == 10
        lst.supprimer_tete()
        assert lst.tete.v == 5
        lst.supprimer_tete()
        assert lst.tete is None
        print("ok")
 
    def tester_inserer_fin():
        print("Tests de inserer_fin())...", end="")
        lst = Liste()
        lst.inserer_fin(5)
        assert lst.tete.v == 5        
        lst.inserer_fin(10)
        assert lst.tete.v == 5
        assert lst.tete.s.v == 10
        lst.inserer_fin(20)
        assert lst.tete.v == 5
        assert lst.tete.s.s.v == 20
        lst.inserer_tete(200)
        assert lst.tete.v == 200
        assert lst.tete.s.v == 5
        assert lst.tete.s.s.v == 10        
        assert lst.tete.s.s.s.v == 20
        print("ok")

    def tester_inserer():
        print("Tests de inserer())...", end="")
        lst = Liste()
        lst.inserer(5, 0)
        lst.inserer(10, 1)
        assert lst.tete.v == 5
        assert lst.acces_fin().v == 10
        lst.inserer(500, 1)
        assert lst.tete.v == 5
        assert lst.tete.s.v == 500
        assert lst.acces_fin().v == 10       
        print("ok")
        
    def tester_supprimer_fin():
        print("Tests de supprimer_fin())...", end="")
        lst = Liste()
        lst.inserer_tete(5)
        lst.inserer_tete(10)
        lst.inserer_tete(20)
        lst.inserer_tete(200)
        lst.supprimer_fin()
        assert lst.tete.v == 200
        assert lst.acces_fin().v == 10
        lst.supprimer_tete()
        assert lst.tete.v == 20
        assert lst.acces_fin().v == 10
        lst.supprimer_fin()
        assert lst.acces_fin().v == 20
        lst.supprimer_fin()
        assert lst.tete is None
        print("ok")

    def tester_supprimer():
        print("Tests de inserer())...", end="")
        lst = Liste()
        lst.inserer(5, 0)
        lst.inserer(10, 1)
        lst.inserer(500, 1)
        lst.supprimer(1)
        assert lst.tete.v == 5
        assert lst.acces_fin().v == 10
        lst.supprimer(0)
        assert lst.tete.v == 10
        assert lst.acces_fin().v == 10
        lst.supprimer(0)
        assert lst.tete == None
        print("ok")

    def tester_ieme_premier_dernier():
        print("Tests ieme() premier() dernier()...", end="")
        lst = Liste()
        lst.inserer_tete(5)
        lst.inserer_tete(10)
        lst.inserer_tete(20)
        lst.inserer_fin(30)
        assert lst.premier() == 20
        assert lst.ieme(0) == 20
        assert lst.ieme(1) == 10
        assert lst.ieme(2) == 5
        assert lst.ieme(3) == 30
        assert lst.dernier() == 30
        lst.supprimer(1)
        assert lst.premier() == 20
        assert lst.ieme(0) == 20
        assert lst.ieme(1) == 5
        assert lst.ieme(2) == 30
        assert lst.dernier() == 30    
        lst.supprimer(0)
        assert lst.premier() == 5
        assert lst.ieme(0) == 5
        assert lst.ieme(1) == 30
        assert lst.dernier() == 30     
        lst.supprimer_tete()
        assert lst.premier() == 30
        assert lst.ieme(0) == 30
        assert lst.dernier() == 30   
        lst.supprimer_fin()
        assert lst.est_liste_vide()
        print("ok")
        
    tester_inserer_tete()
    tester_supprimer_tete()
    tester_inserer_fin()
    tester_supprimer_fin()
    tester_inserer()
    tester_supprimer()
    tester_ieme_premier_dernier()