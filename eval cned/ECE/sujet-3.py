def fibonacci(n):
    if n <=1:
        return n 
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci(n):
    a , b = 1,1
    for i in range(2,n):
        a, b = b , a +b
    return b    
        

def eleves_du_mois(eleves, notes): 
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(1,len(eleves)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]
    return (note_maxi, meilleurs_eleves)

def dicho(x, tab):
    debut = 0
    fin = len(tab)
    while fin > debut :
        m = debut+ (fin-debut)//2
        if tab[m ] < x:
            debut = m + 1
        else : 
            fin = m
    return m            

def bin(n):
    if n == 0 or n == 1:
        return str(n)
    return bin(n//2)+str(n%2)

if __name__ == '__main__':
    
    print(dicho(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    
    
    