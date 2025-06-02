def recherche(tab, x):
    debut = 0
    fin = len(tab)-1
    while debut <= fin :
        m = (debut+fin)//2
        if tab[m] == x:
            return True
        elif x >= tab[m]:
            debut = m + 1
        else : 
            fin = m - 1    
    return False

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet''' 
    return ord(lettre) - ord('A')


def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César pour le decalage donné'''
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+ decalage) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat
if __name__ == '__main__':
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))

        