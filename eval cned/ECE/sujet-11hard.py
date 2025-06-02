arbre = ( ( (None, 1, None), 2, (None, 3, None) ),
              4,
              ( (None, 5, None), 6, (None, 7, None) ) )

def parcours_largeur(arbre):
    file = [arbre]
    ordre = []
    while file:
        a = file.pop(0)
        print(a[1])
        if a[0]:
            file.append(a[0])
        if a[2]:    
            file.append(a[2])
    return ordre        


def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i 
    for i in range(1,n):
        if sommes_max[i-1] + sommes_max[i] > sommes_max[i]: 
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci 
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]: 
            maximum = i
    return sommes_max[maximum]

print(somme_max([1, -2, 3, 10, -4, 7, 2, -5]))        