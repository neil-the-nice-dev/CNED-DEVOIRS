def renverse(phrase):
    if phrase == '':
        return ''
    count = len(phrase)
    mot = ''
    for i in range(count+1):
        mot = mot + phrase[- i] 
    return mot[1:]     


def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]: 
            premiers.append(i)
            multiple = 0 
            while multiple < n:
                    tab[multiple] = False
                    multiple = multiple + i
    return premiers

if __name__ == '__main__':
    print(crible(40))