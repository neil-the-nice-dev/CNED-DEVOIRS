def verifie(tab):
    for i in range (len(tab)):
        if tab[i] == tab[i+1]:
            return True 
    return False

def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un dictionnaire avec le nombre de voix pour chaque candidat''' 
    resultat = {}
    for bulletin in urne:
        if resultat[bulletin] in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = resultat[bulletin]
    return resultat
    
def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre
    ↪ de voix
    pour chaque candidat et renvoie la liste des vainqueurs''' 
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax : 
            nmax = election[candidat]
    liste_finale = [ nom for nom in election if election[nom] == nmax ] 
    return liste_finale

print(verifie([0, 5, 8, 8, 9]))