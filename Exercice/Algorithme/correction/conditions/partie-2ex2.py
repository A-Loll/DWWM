# demande une valeur à l'utilisateur
# stock ce cette valeur dans une variable val1
# demande une valeur à l'utilisateur 
# stock cette valeur dans une variable val2
# si val1 * val2 > 0
#     alors on ecrit "produit positif"
# sinon si val1 * val2 < 0
#     alors on ecrit "produit négatif"
# fin si 

val1:int    =   int(input("entrez la première valeur : "))
val2:int    =   int(input("entrez la seconde valeur : "))
if (val1 * val2 > 0):
    print("produit positif")
if val1 * val2 < 0 : 
    print("produit négatif")

