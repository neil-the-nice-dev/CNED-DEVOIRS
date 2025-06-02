def fusion(tab1, tab2):
    tab = tab1 + tab2
    tab.sort()
    return tab

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


def traduire_romain(nombre):
    
    if len(nombre) == 1:
        return romains[nombre] 
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return  traduire_romain(nombre[1:]) - romains[nombre[0]]


if __name__ == '__main__':
    romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    print(traduire_romain("CXLII"))