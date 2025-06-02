def correspond(mot, mot_troue):
    if len(mot) == len(mot_troue):
        count = 0
        for i in range (len(mot)):
            if mot[i] != mot_troue[i] and mot_troue[i] != '*':
                return False
        return True     
    else :
        return False    
    
def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1
    while destinataire != expediteur: 
        destinataire = plan[destinataire]
        nb_destinataires = nb_destinataires+1 
    return nb_destinataires == len(plan)
        
if __name__ == '__main__':
    print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'}))    
        