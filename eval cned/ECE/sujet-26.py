from random import randint

def ajoute_dictionnaires(d1, d2):
    d = {}
    for k in d1:
        if k in d2 :
            d[k] = d1[k] + d2[k]
        else :
            d[k] = d1[k]
    for k in d2:
        if k not in d:
            d[k] = d2[k]
    return d        
            

def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre nécessaire de coups pour visiter toutes les cases.''' 
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = ...
    while ... < ...:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + ...) % ... 
        if ...:
            cases_vues[case_en_cours] = True
            nombre_cases_vues = ...
            n = ...
    return n       
    
    
        
    
if __name__ == '__main__':
        print(ajoute_dictionnaires({}, {2: 9, 3: 11}))