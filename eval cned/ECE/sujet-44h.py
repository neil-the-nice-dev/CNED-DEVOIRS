def moyenne(tab):
    moy = 0
    efi = 0
    for i in tab:
        u,v = i
        moy = moy + u * v
        efi = efi + v 
    return moy/efi     
        
def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
        un "*" , les 0 par une espace " " '''
    for ligne in dessin: 
        affichage = ''
        for col in ligne: 
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " " 
        print(affichage)     
        
def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
       liste_depart'''
    liste_zoomee = [] 
    for elt in liste_depart :
        for i in range(k): 
            liste_zoomee.append(elt)
    return liste_zoomee           

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee) 
    return grille_zoomee        
        
        
if __name__ == '__main__':
    coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
    print(affiche(dessin_zoom(coeur,2)))        