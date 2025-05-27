def nombre_de_mots(phrase):
    nb_m = 0
    for i in phrase :
        if i == ' ':
            nb_m = nb_m + 1
        if i == '!' or i == '?':
            nb_m = nb_m - 1
    return nb_m +1


class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud. Crée une feuille d'étiquette donnée.''' 
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None
    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None:
                self.droit.inserer(cle) 
            else:
                self.droit = Noeud(cle)

if __name__ == '__main__':
    arbre = Noeud(7)
    for cle in (3, 9, 1, 6):
        arbre.inserer(cle)
    print(arbre.gauche.etiquette)   
        