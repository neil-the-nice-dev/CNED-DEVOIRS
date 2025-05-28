def nb_repetitions(nb, tab):
    nb_rep = 0
    for i in tab :
        if i == nb:
            nb_rep += 1
    return nb_rep


def binaire(a):
    '''convertit un nombre entier a en sa representation binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0' 
    bin_a = ''
    while a > 0:
        bin_a = str(a%2) + bin_a 
        a = a//2
    return bin_a



if __name__ == "__main__":
    print(binaire(83))