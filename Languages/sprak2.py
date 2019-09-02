

vokaler = ['a','o','u','å','e','i','y','ä','ö']
konsonanter = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
mellanslag = " "



def viskspråket(inrad):
    utrad = ""
    for tkn in inrad:
         if tkn in konsonanter or tkn == mellanslag:
            utrad +=tkn
            
            
    return utrad


def rövarspråk(inrad):
    utrad=""
    for tkn in inrad:
        if tkn in konsonanter:
            utrad +=tkn
            utrad +='o'
            utrad +=tkn
        if tkn in vokaler or tkn == mellanslag:
            utrad +=tkn

    return utrad


def fyllespråk(inrad):
    utrad=""
    for tkn in inrad:
        if tkn in konsonanter or tkn ==mellanslag:
            utrad+=tkn
        if tkn in vokaler:
            utrad+=tkn
            utrad+='f'
            utrad+=tkn

    return utrad


def bebisspråk(inrad):
    utrad=[]
    ordlista = inrad.split()
    for ordet in ordlista:
        n = 0
        for tkn in ordet:

            if ordet[0] in vokaler:
                utrad +=3*(tkn[:1])
                utrad+= ' '
                break

            if tkn in vokaler:
                n+=2
                utrad+=3*(ordet[:n-1])
                utrad+= ' '
                break
            if tkn in konsonanter:
                n+=1
           

    utrad = "".join(utrad)
         
    return utrad



def allspråk(inrad):
    utrad =[]
    ordlista =inrad.split()
    for ordet in ordlista:
        n =0
        for tkn in ordet:
            if tkn in konsonanter:
                n+=1
            if tkn in vokaler:
                
                utrad+=ordet[n:]
                utrad+=ordet[:n]
                
                utrad+='all '
                
                break
        
                
    
    utrad="".join(utrad)            

    return utrad

def fikonspråket(inrad):
    utrad=[]
    ordlista=inrad.split()
    for ordet in ordlista:
        n=0
        for tkn in ordet:
            if tkn in konsonanter:
                n+=1
            if tkn in vokaler:
                n+=1
                utrad+='fi'
                utrad+=ordet[n:]
                utrad+=ordet[:n]
                utrad+='kon '
                break
            
    utrad="".join(utrad)

    return utrad


                
#n = int(input("Vilket språk önskas?\:"))


                
            
        


