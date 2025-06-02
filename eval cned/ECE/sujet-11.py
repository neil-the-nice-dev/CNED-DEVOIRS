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

print(parcours_largeur(arbre))        