def compte_occurrences(nb, tab):
    if tab == []:
        return 0
    compte = 0
    for i in tab:
        if nb == i:
            compte +=1
    return compte



pieces = [1, 2, 5, 10, 20, 50, 100, 200]



def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        while pieces[i] > a_rendre: 
            i=i-1
        rendu.append(pieces[i])
        a_rendre = a_rendre - pieces[i]
    return rendu





if __name__=='__main__':
    print(rendu_monnaie(700, 700))
    print(rendu_monnaie(102, 500))    
    
    
    
    