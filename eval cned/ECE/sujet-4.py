def ecriture_binaire_entier_positif(n):
    nb = ''
    if n == 0 or n == 1:
        return f'{n}'
    return ecriture_binaire_entier_positif(n //2 ) + str(n%2)

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.''' 
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp
def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n):
        for j in range(n):
            if tab[j] > tab[i]:
                echange(tab, j, i)


tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
print(tab2)
        