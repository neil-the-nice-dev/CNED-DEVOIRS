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




if __name__ == '__main__':
    eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
    notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
    
    print(eleves_du_mois(eleves_nsi, notes_nsi))
    print(fibonacci(7))