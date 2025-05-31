def voisins_entrants(adj, x):
    t = []
    for i in range(len(adj)):
        if x in adj[i]:
            t.append(i)
    return t


def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)):
        if s[i] == chiffre: 
            compte = compte+1
        else:
            resultat += str(compte) + chiffre 
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre 
    return resultat


if __name__ == '__main__':
    print(nombre_suivant('1211'))