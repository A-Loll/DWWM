# demande un nombre de depart

start   =   input('entrez un nombre :\n')
while start.isdigit() == False : 
    start   =   input('entrez un nombre :\n')
start   =   int(start)
print('débt du comptage')
for nbDisplay in range(1,11) : # range(1,11) == [1,2,3,4,5,6,7,8,9,10]
    print(start+nbDisplay)