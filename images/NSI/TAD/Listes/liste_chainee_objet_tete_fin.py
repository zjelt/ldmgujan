'''MODULE implémentant une Liste Chaînée MUABLE sous forme d'un objet stockant Tête et Fin

Description
-----------
* Une Liste VIDE est un objet dont l'attribut tete contient None
* Une Liste NON VIDE est un objet qui possède deux attributs : tete et fin
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
+ CST : Liste.acces_fin(self:'Liste NON VIDE') -> Cellule
+ LIN : Liste.acces(self:'Liste NON VIDE', i:'int VALIDE') -> Cellule

+ CST : Liste.inserer_tete(self:'Liste', elt:'Element') -> None
+ CST : Liste.inserer_fin(self:'Liste', elt:'Element') -> None
+ LIN : Liste.inserer(self:'Liste', elt:'Element', i:'int VALIDE') -> None

+ CST : Liste.supprimer_tete(self:'Liste NON VIDE') -> 'Element'
+ LIN : Liste.supprimer_fin(self:'Liste NON VIDE') -> 'Element'
+ LIN : Liste.supprimer(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element'

+ LIN : Liste.longueur(self:'Liste') -> int

+ CST : Liste.premier(self:'Liste NON VIDE') -> 'Element'
+ CST : Liste.dernier(self:'Liste NON VIDE') -> 'Element'
+ LIN : Liste.ieme(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element'


Fonctions d'interface cachant l'aspect objet
---------------------------------------------
+ CST : nouvelle_liste() -> Liste
+ CST : est_liste_vide(lst:'Liste') -> bool

+ CST : inserer_tete(lst:'Liste', elt:'Element') -> None
+ CST : inserer_fin(lst:'Liste', elt:'Element') -> None
+ LIN : inserer(lst:'Liste', elt:'Element', i:'int VALIDE') -> None

+ CST : supprimer_tete(lst:'Liste NON VIDE') -> 'Element'
+ LIN : supprimer_fin(lst:'Liste NON VIDE') -> 'Element'
+ LIN : supprimer(lst:'Liste NON VIDE', i:'int VALIDE') -> 'Element'

+ LIN : longueur(lst:'Liste') -> int

+ CST : premier(lst:'Liste NON VIDE') -> 'Element'
+ CST : dernier(lst:'Liste NON VIDE') -> 'Element'
+ LIN : ieme(lst:'Liste NON VIDE', i:'int VALIDE') -> 'Element'


'''

class Cellule:
    '''Cellule (valeur, successeur)'''
     
    def __init__(self, valeur:'Element', successeur:'Cellule|None'):
        self.v = valeur      # Valeur ne peut pas être None si File homogène
        self.s = successeur  # successeur vaut None si Cellule de Fin     

    def nb_cellules(self:'Cellule') -> int:  #Coût Linéaire O(n)
        '''Renvoie le nombre de cellules dans la chaîne à partir de cette cellule'''
        if self.s is None:                  # si la cellule actuelle n'a pas de successeur
            return 1                        # il y a au moins la cellule actuelle
        else:
            return 1 + self.s.nb_cellules()  # on demande au successeur et on rajoutera la cellule actuelle

    def contenu(self:'Cellule') -> 'Element':  # Coût constant
        '''Renvoie le contenu de la Cellule'''
        return self.v
     
    def successeur(self:'Cellule NON FIN') -> 'Cellule':  # Coût constant
        '''Renvoie la Cellule qui succède à une cellule NON FIN'''
        return self.s

class Liste:
    '''Liste chaînée MUABLE Tete et Fin'''
     
    def __init__(self):
        self.tete = None   
        self.fin = None

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
    
    def acces_fin(self:'Liste NON VIDE') -> Cellule:  # Coût constant
        '''Renvoie l'adresse de la cellule de Fin dans la liste NON VIDE'''
        return self.fin
    
    def acces(self:'Liste NON VIDE', i:'int VALIDE') -> Cellule:  # Coût Linéaire O(n)
        '''Renvoie l'adresse de la cellule i dans la liste NON VIDE'''
        c = self.acces_tete()  # récupère la cellule de tête
        for _ in range(i):     # Faire i fois
            c = c.s            # passe au successeur
        return c
    
    def inserer_tete(self:'Liste', elt:'Element') -> None:  # coût constant
        '''Rajoute une nouvelle cellule contenant elt en tête de liste'''
        nouvelle = Cellule(elt, None)    # Etape 1 : création de la cellule
        if self.est_liste_vide():        # si la liste est vide initialement, il faut gérer la fin
            self.fin = nouvelle
        nouvelle.s = self.tete           # Etape 2 : on relie la nouvelle cellule à l'"ancienne" Tête
        self.tete = nouvelle             # Etape 3 : modification de la liste    
  
    def inserer_fin(self:'Liste', elt:'Element') -> None:  # Coût constant
        '''Rajoute une nouvelle cellule de Fin contenant elt dans la liste'''
        if self.est_liste_vide():          # Si la liste est vide,
            self.inserer_tete(elt)         # on active inserer_tete() puisque tete et fin sont la même cellule
        else:
            nouvelle = Cellule(elt, None)  # Etape 1 : on crée la nouvelle Cellule
            self.fin.s = nouvelle          # Etape 2 : on relie l'ancienne Fin à la nouvelle
            self.fin = nouvelle            # Etape 3 : mise à jour de la liste

    def inserer(self:'Liste', elt:'Element', i:'int VALIDE') -> None:  # Coût Linéaire O(n)
        '''Rajoute une nouvelle cellule contenant elt en position i VALIDE de la liste'''
        if i == 0:                             # si on veut insérer en Tête en réalité
            self.inserer_tete(elt)             # on fait appel à inserer_tete
        else:
            pred = self.acces(i-1)             # Etape 1 : recherche de la cellule i-1
            if pred.s == None:                 # si on veut insérer en Fin en réalité
                self.inserer_fin(elt)          # on fait appel à inserer_fin...
            else:                              # Ici, on insère ni en Tête, ni en Fin
                nouvelle = Cellule(elt, None)  # Etape 2 : création de la cellule
                nouvelle.s = pred.s            # Etape 3 : liaison nouvelle i vers ancienne i
                pred.s = nouvelle              # Etape 4 : liaison i-1 vers nouvelle i
 
    def supprimer_tete(self:'Liste NON VIDE') -> 'Elt':  # coût constant
        """Supprime la tête et renvoie son contenu"""
        memoire = self.tete.v      # Etape 1 : on mémorise l'ancienne valeur
        self.tete = self.tete.s    # Etape 2 : la tête devient le successeur de l'ancienne tête
        if self.est_liste_vide():  # si la liste est maintenant VIDE
            self.fin = None
        return memoire

    def supprimer_fin(self:'Liste NON VIDE') -> 'Element':  # Coût Linéaire θ(n)
        '''Supprime la cellule de fin d'une liste NON VIDE et renvoie l'élément qui y était stocké'''
         
        if self.tete == self.fin:       # si la liste ne possède qu'une seule cellule
            return self.supprimer_tete() # on demande à l'autre fonction de faire le travail
        else :
            # Etape 1 : on cherche le prédécesseur de la Fin
            c = self.tete             # on part de la tête
            while c.s.s is not None:  # tant que c n'est pas le prédécesseur de la Fin
                c = c.s               # on passe à la cellule suivante
             
            ancienne_valeur = c.s.v   # Etape 2 : on mémorise la valeur de Fin actuelle
            c.s = None                # Etape 3 : on fait pointer le prédécesseur sur None
            self.fin = c              # Etape 4 : on met la liste à jour
            return ancienne_valeur       # Etape 5 : on renvoie la valeur mémorisée
 
    def supprimer(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element':  # Coût linéaire θ(i) O(n)
        """Supprime la cellule en position i VALIDE et renvoie l'élément qui y était stocké"""
        if i == 0:                          # En réalité, on veut supprimer la Tête
            return self.supprimer_tete()
        else:
            pred = self.acces(i-1)          # Etape 1 : recherche de la cellule i-1
            if pred.s == self.fin:          # on veut alors supprimer la Fin
                return self.supprimer_fin()
            else:                           # on ne supprime ni la tête, ni la fin
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
        return self.tete.v   # ou mieux : return self.tete.contenu()
        
    def dernier(self:'Liste NON VIDE') -> 'Element':  # Coût constant
        '''Renvoie l'élément stocké en Fin de liste NON VIDE'''
        return self.fin.v     # ou mieux : return self.fin.contenu()

    def ieme(self:'Liste NON VIDE', i:'int VALIDE') -> 'Element':  # Coût Linéaire O(n)
        '''Renvoie l'élément stocké en position i de la liste NON VIDE'''
        return self.acces(i).v    





# Primitives en version fonction pour cacher qu'on manipule un objet

def nouvelle_liste() -> 'Liste':
    '''Renvoie une nouvelle liste vide'''
    return Liste()

def est_liste_vide(lst:'Liste') -> bool:
    '''Prédicat qui renvoie True si la liste est vide'''
    return lst.est_liste_vide()

def inserer_tete(lst:'Liste', elt:'Element') -> 'None':
    '''Rajoute elt en Tête de liste'''
    lst.inserer_tete(elt)
    
def inserer_fin(lst:'Liste', elt:'Element') -> 'None':
    '''Rajoute elt en Fin de liste'''
    lst.inserer_fin(elt)
    
def inserer(lst:'Liste', elt:'Element', i:'int VALIDE') -> 'None':
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
        assert lst.tete == lst.fin
        lst.inserer_tete(10)
        assert lst.tete != lst.fin
        assert lst.tete.v == 10
        assert lst.fin.v == 5
        lst.inserer_tete(20)
        assert lst.tete != lst.fin
        assert lst.tete.v == 20
        assert lst.fin.v == 5
        print("ok")
 
    def tester_supprimer_tete():
        print("Tests de supprimer_tete())...", end="")
        lst = Liste()
        lst.inserer_tete(5)
        lst.inserer_tete(10)
        lst.inserer_tete(20)
        lst.supprimer_tete()
        assert lst.tete != lst.fin
        assert lst.tete.v == 10
        assert lst.fin.v == 5
        lst.supprimer_tete()
        assert lst.tete == lst.fin
        assert lst.fin.v == 5
        lst.supprimer_tete()
        assert lst.tete == lst.fin
        assert lst.fin == None
        print("ok")
 
    def tester_inserer_fin():
        print("Tests de inserer_fin())...", end="")
        lst = Liste()
        lst.inserer_fin(5)
        assert lst.tete == lst.fin
        lst.inserer_fin(10)
        assert lst.tete != lst.fin
        assert lst.tete.v == 5
        assert lst.fin.v == 10
        lst.inserer_fin(20)
        assert lst.tete != lst.fin
        assert lst.tete.v == 5
        assert lst.fin.v == 20
        lst.inserer_tete(200)
        assert lst.tete != lst.fin
        assert lst.tete.v == 200
        assert lst.fin.v == 20
        print("ok")

    def tester_inserer():
        print("Tests de inserer())...", end="")
        lst = Liste()
        lst.inserer(5, 0)
        assert lst.tete == lst.fin
        lst.inserer(10, 1)
        assert lst.tete.v == 5
        assert lst.fin.v == 10
        lst.inserer(500, 1)
        assert lst.tete.v == 5
        assert lst.tete.s.v == 500
        assert lst.fin.v == 10       
        print("ok")
        
    def tester_supprimer_fin():
        print("Tests de supprimer_fin())...", end="")
        lst = Liste()
        lst.inserer_tete(5)
        lst.inserer_tete(10)
        lst.inserer_tete(20)
        lst.inserer_tete(200)
        lst.supprimer_fin()
        assert lst.tete != lst.fin
        assert lst.tete.v == 200
        assert lst.fin.v == 10
        lst.supprimer_tete()
        assert lst.tete != lst.fin
        assert lst.tete.v == 20
        assert lst.fin.v == 10
        lst.supprimer_fin()
        assert lst.tete == lst.fin
        assert lst.fin.v == 20
        lst.supprimer_fin()
        assert lst.tete == lst.fin
        assert lst.fin == None
        print("ok")

    def tester_supprimer():
        print("Tests de inserer())...", end="")
        lst = Liste()
        lst.inserer(5, 0)
        lst.inserer(10, 1)
        lst.inserer(500, 1)
        lst.supprimer(1)
        assert lst.tete.v == 5
        assert lst.fin.v == 10
        lst.supprimer(0)
        assert lst.tete.v == 10
        assert lst.fin.v == 10
        lst.supprimer(0)
        assert lst.tete == None
        assert lst.fin == None
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