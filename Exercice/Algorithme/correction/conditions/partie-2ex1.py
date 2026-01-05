# demande à l'utilisateur un nombre
# on stock ce nombre dans une variable nombre
# si nombre > 0
#     alors on affiche "positif"
# sinon si nombre < 0 
#     alors on affiche "négatif"
# fin si

nombre = input()
if int(nombre) > 0 :
    print("positif")
elif int(nombre) < 0 :
    print("négatif")