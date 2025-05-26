def recherche_motif(motif, texte):
    t = []
    for i in range(len(texte) - len(motif) + 1):
        j = 0
        corr = True
        while  corr and j < len(motif):
            if texte[i+j] == motif[j]:
                j = j + 1
            else :
                corr = False 
        if corr:
            t.append(i)
    return t
        
def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif du graphe donné par les listes d'adjacence adj depuis le sommet x en accumulant les sommets rencontrés dans acc'''
    if x not in acc :
        acc.append(x) 
        for y in adj[x]:
            parcours(adj,y,acc)
def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le graphe donné par les listes d'adjacence adj depuis le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc



 
if __name__ == '__main__':
    print(recherche_motif("ab", "abracadabra"))
    print(accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 0))
    
        
    