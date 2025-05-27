def insertion_abr(a,cle):
    if a == None:
        return (None, cle, None)
    if cle == a[1]:
        return a
    elif cle > a[1] :
        return  (a[0], a[1], insertion_abr(a[2], cle))
    else :
        return  (insertion_abr(a[0], cle), a[1], a[2])


def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour empaqueter les objets de la liste liste_masses, sachant que chaque boîte peut contenir au maximum c kilogrammes""" 
    n = len(liste_masses)
    nb_boites = 0
    boites = [ 0 for _ in range(n) ]
    for masse in liste_masses:
        i=0
        while i < nb_boites and boites[i] + masse > c:
            i=i+1
        if i == nb_boites:
            nb_boites = nb_boites+1
        boites[i] = boites[i] + masse
    return nb_boites

if __name__ == '__main__':
    print(empaqueter([1, 2, 3, 4, 5], 10))
    print(empaqueter([1, 2, 3, 4, 5], 5))
    print(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))