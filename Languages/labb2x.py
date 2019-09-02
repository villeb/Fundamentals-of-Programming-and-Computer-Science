
from sprak2 import *



while True:
    
    n = int(input("Vilket språk önskas? \n 1 Visk 2 Rövar 3 Fylle 4 Bebis \n 5 All 6 Fikon 7 Avsluta programmet  \n"))

    while n < 8 and n!= 0:
        
        if n == 1:
            mening =  str(input("Din mening:"))
            print("Viskspråket:",viskspråket(mening), 2*'\n')
            break

        if n == 2:
            mening = str(input("Din mening:"))
            print("Rövarspråket:",rövarspråk(mening),2*'\n')
            break
        elif n == 3:
            mening = str(input("Din mening:"))
            print("Fyllespråket:",fyllespråk(mening), 2*'\n')
            break
        elif n== 4:
            mening = str(input("Din mening:"))
            print("Bebisspråket:",bebisspråk(mening), 2*'\n')
            break
        elif n == 5:
            mening = str(input("Din mening:"))
            print("Allspråket:",allspråk(mening), 2*'\n')
            break

        elif n == 6:
            mening = str(input("Din mening:"))
            print("Fikonspråket:",fikonspråket(mening), 2*'\n')
            break
        else: n == 7
        print("Hej då")
        
        raise SystemExit(0)

    
    
    
    

