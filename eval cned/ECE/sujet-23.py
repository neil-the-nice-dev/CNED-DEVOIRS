#vrai condition d'exam ( if __name__ == '__main__' : )

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2 
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)
    
    
def bin_to_dec(nb_bin): 
    if len(nb_bin) == 1:
        if nb_bin == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0': 
            bit_droit = 0
        else:
            bit_droit = 1
    return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

if __name__ == '__main__':
    print(dec_to_bin(25)) 
    print(bin_to_dec('101010')) # [2,0,1,0,1,4,2,1,0,5,1]
     # [0,0,2,4,5,5,5,5,6,6,7,9,9,9,9,9,10]