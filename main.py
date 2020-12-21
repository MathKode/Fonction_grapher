from matplotlib import pyplot
import numpy as np
def run(f) :
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


    

while True :
    f = input('Fonction : ')
    for c in ['+','-','*','/',' '] :
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
        result.append(run(' '.join(fc)))
        x.append(deb)
        deb += 1
    x = np.array(x)
    y = np.array(result)
    print(x)
    print(y)
    pyplot.plot(x, y)
    pyplot.show()




    
    
            