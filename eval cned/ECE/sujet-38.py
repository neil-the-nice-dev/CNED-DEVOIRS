def moyenne(tab):
    moy = 0
    for i in tab :
        moy = moy + i 
    return moy/len(tab)    


def binaire(a):
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a    







if __name__ == '__main__':
    print(binaire(0))