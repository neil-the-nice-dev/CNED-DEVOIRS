def couples_consecutifs(tab):
    couple = []
    for i in range(len(tab)-1):
        if (tab[i]+1) == (tab[i+1]):
            couple.append((tab[i],tab[i+1])) 
    return couple   


def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return
    M[i][j] = val
    if i-1 >= 0: # propage Ã  gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage Ã  droite 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0 : # propage en haut 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[0]): # propage en bas 
        colore_comp1(M, i, j+1, val)     
    
if __name__ == '__main__':
    M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
    colore_comp1(M, 2, 1, 3)
    print(M[0])