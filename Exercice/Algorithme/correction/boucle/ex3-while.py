# demande un nombre de depart
# stock ce nombre dans un variable start 
# on declare une variable nbDisplay égale à 0
# tant que nbDisplay < 10
#     alors on affiche start + nbDisplay
#     et on incrémente nbDisplay
# Fin tant que

start   =   input('entrez un nombre :\n')
while start.isdigit() == False : 
    start   =   input('entrez un nombre :\n')
start   =   int(start)
nbDisplay:int   =   0
print('débt du comptage')
# nbDisplay == 10 || nbDisplay < 10
while nbDisplay < 10:
    nbDisplay   +=  1
    print(start + nbDisplay)
