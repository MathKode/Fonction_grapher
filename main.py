from matplotlib import pyplot
import numpy as np
def run(f) :
    #Supprime les espaces
    for c in ['+','-','*','/','(',')',' '] :
        l = f.split(c)
        f = f' {c} '.join(l)
    f = f.split(' ')
    print(f)
    l = []
    for i in f :
        if i != '' :
            l.append(i)
    f = " ".join(l)
    print(f)
    #calcule la fonction (avec un espace entre chaque cartacère)
    
    fc = f.split(' ')
    p = 0
    while p < len(fc)-1 :
        if str(fc[p]) == "*" :
            nb1 = float(fc[p-1])
            nb2 = float(fc[p+1])
            fc[p] = str(nb1*nb2)
            del fc[p+1]
            del fc[p-1]
            p -= 1
        elif str(fc[p]) == '/' :
            nb1 = float(fc[p-1])
            nb2 = float(fc[p+1])
            
            try :
                fc[p] = str(nb1/nb2)
            except :
                print('ERREUR /0')
                fc[p] = "0"
            
            del fc[p+1]
            del fc[p-1]
            p -= 1
        p+=1
    print("".join(fc))

    print(fc)
    p = 0
    while p < len(fc)-1 :
        if str(fc[p]) == "+" :
            nb1 = float(fc[p-1])
            nb2 = float(fc[p+1])
            fc[p] = str(nb1+nb2)
            del fc[p+1]
            del fc[p-1]
            p -= 1
        elif str(fc[p]) == '-' :
            nb1 = float(fc[p-1])
            nb2 = float(fc[p+1])
            fc[p] = str(nb1-nb2)
            del fc[p+1]
            del fc[p-1]
            p -= 1
        p+=1
    print(fc)
    return float(fc[0])

def parenthese(f) :
    # Découpe une formule comme ceci : x*(3+(6-9)) = ['x*@1@',3+@2@,6-9]
    bloc = [] # ls contenant les groupes de parenthèse
    deb = 0
    re = ''
    fonc = ''
    for i in f :
        if i == '(' and deb != -10:
            if deb == 0 :
                fonc += "@ "
            deb += 1
        if i == ')' and deb != -10 :
            deb -= 1
            if deb == 0 :
                r = list(re)
                del r[0]
                del r[0]
                del r[-1]
                re = "".join(r)
                deb = -10
            else :
                re += i
        elif deb == 0 or deb == -10 :
            fonc += i
        else :
            re += i
    print(fonc, re)
    return fonc, re
    
def calcul(f) :
    g = [str(f)]
    while True :
        if '(' in g[-1] :
            fonc, new = parenthese(g[-1])
            g[-1] = fonc
            g.append(new)
        else :
            if len(g) == 1 :
                break 
            else :
                print('Non PR :', g[-1])
                result = run(g[-1])
                del g[-1]
                ls = g[-1].split('@')
                g[-1] = str(result).join(ls)
        print(g)

    print("fin :",g)
    result = run(g[-1])
    print(result)   

while True :
    f = input('Fonction : ')
    for c in ['+','-','*','/','(',')',' '] :
        l = f.split(c)
        f = f' {c} '.join(l)
    f = f.split(' ')
    print(f)
    l = []
    for i in f :
        if i != '' :
            l.append(i)
    f = l
    deb = int(input('Begin : '))
    fin = int(input('End : '))
    result = []
    x = []
    for i in range(fin-deb+1) :
        fc = []
        for j in l :
            if j == 'x' :
                fc.append(str(deb))
            else :
                fc.append(str(j))
        print(' '.join(fc))
        result.append(calcul(' '.join(fc)))
        x.append(deb)
        deb += 1
    x = np.array(x)
    y = np.array(result)
    print(x)
    print(y)
    pyplot.plot(x, y)
    pyplot.show()
