

def riffel(seq):
    lista=[]
    a=seq[:(len(seq))//2] #  halva listan, ( mindre än  mitten)
    b=seq[(len(seq))//2:len(seq)] # halva listan (större än mitten)
    for i in range(len(seq)):
        if i%2==0: # Alla jämna tal
            lista.append(b[i//2]) 
        else: lista.append(a[i//2]) # lägg in alla tal i varannan ordning

    return lista


def riffelblandning(n):
    lista=[]
    seq=[]
    for i in range(n):
        lista.append(i+1) # Skapar en lista av kortleken
    #print(lista, len(lista))
    t=0
    seq = lista
    while True:
        seq=riffel(seq)
        t+=1
        if lista == seq:
            break
   # print(lista,'\n',seq, t)
    return ("antal jämförelser:",t)

print(riffelblandning(8))


