def correspond(mot, mot_troue):
    if len(mot) == len(mot_troue):
        count = 0
        for i in range (len(mot)):
            if mot[i] != mot_troue[i] and mot_troue[i] != '*':
                return False
        return True     
    else :
        return False    
    
if __name__ == '__main__':
    print(correspond('AUTO', '*UT*'))    
        