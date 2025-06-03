def recherche_motif(motif, texte):
    lst = []
    for i in range(len(texte)):
        if coincie(motif, texte, i):
            lst.append(i)
    return lst     

def coincie(motif, texte, i):
    for j in range(len(motif)):
        if motif[j] != texte[i+j]:
            return False
    return True
    
    
    
    
     
def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)
            
def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc                

print(accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 0))