def occurrences(caractere, chaine):
    ocu = 0
    for i in chaine:
        if caractere == i :
            ocu = ocu + 1
    return ocu 

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return [] 
    v = valeurs[rang]
    if v <= a_rendre: 
        return [v] + rendu_glouton(a_rendre - v, rang) 
    else:
        return rendu_glouton(a_rendre, rang+1) 




if __name__ == '__main__':
    print(rendu_glouton(291, 0))
    print(occurrences('i',"mississippi"))
    print(occurrences('a',"mississippi"))