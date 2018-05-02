l1=[4,8,2,9]
#dos metodos para copiar la informacion de una lista
l2 = list(l1)#1
l2=l1[:]#2
l2=l1
l2[1]=-3
print l1
print l2

# for
lista= [4,7,9,1,5]

#interador, reemplaza al for
for e in lista:
    print e

if 4 in lista:
    print 'esta'
