### ici le 1er exo c'est de la moyenne 



def tri(tab):
    i = 0
    j = len(tab)
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else : 
            valeur =  tab[j]
            tab[j] = 1
            tab[i]= valeur
            j = j-1    



if __name__ == '__main__':
    tab = [0,1,0,1,0,1,0,1,0,1]
    tri(tab)
    print(tab)
    