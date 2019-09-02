#Linjärsökning




def linsok(li, x):
    if x in li:
        return True
    else:
        return False

    

def linsokup(li):
    for j in li:
        ordpar=""
        ordpar+=j[2:]
        ordpar+=j[:2]
        if linsok(li, ordpar)==True:
            print(j,ordpar)


#Finns elementet elem i den sorterade listan list ?

def binsok(li, x):
    lo = 0
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
        
        if x < li[mid]:
            hi = mid - 1
        elif x > li[mid]:
            lo = mid + 1
        else:
            return True
    return False


def binsokup(li):
    for j in li:
        ordpar=""
        ordpar+=j[2:]
        ordpar+=j[:2]
        if binsok(li,ordpar)==True:
            print(j,ordpar)   
        




def main():
    fil = open('ordlistau.txt')
    filstr = fil.read()
    ordlista = filstr.split()
    fil.close()
    a =int(input("välj,1:linsök, 2:linsökup, 3:binärsök, 4binärsökup:"))

    while True:
        if a == 1:
            elem=input("Ditt ord:")
            linsok(ordlista, elem)
            if linsok(ordlista,elem)==True:
                print(elem, "finns")
            else:
                print(elem,"Finns ej")

        if a ==2:
            linsokup(ordlista)
            break
        if a ==3:
            elem=input("Ditt ord:")
            binsok(ordlista, elem)
            if binsok(ordlista,elem)==True:
                print(elem,"finns")
            else:
                print(elem,"Finns ej")

        if a ==4:
            binsokup(ordlista)
            break
        

            
main()



