a=8
b=4
print(f"a={a}")
print(b)

# algo 1
# a   b   c
# 5
# 5   3
# 5   3   8
# 2   3   8
# 2   3   1

a=5
print(a)
b=3
print(a,b)
c=a+b
print(a,b,c)
a=2
print(a,b,c)
c=b-a
print(a,b,c)

# algo 4
# a=5
# b=2
# a=b
# b=a

a=5
print(a,b)
b=2
print(a,b)
a=b
print(a,b)
b=a
print(a,b)


a=5
b=2
temp=a
a=b
b=temp

print("------")
a=5
b=2
print(a,b)
a,b=b,a
print(a,b)

print("carré")
reponse=input("entrez une valeure entiere : ")
nombre=int(reponse)
carre=nombre*nombre
print(f"le carré de {nombre} est : {carre}")

print("---- prix du panier")
reponse1=input("prix de l'article HT : ")
reponse2=input("quantité : ")
reponse3=input("taux de TVA : ")
prixht=float(reponse1)
qte=int(reponse2)
tva=float(reponse3)
totalht=prixht*qte
totalttc=round(totalht*(1+tva/100),2)
print(totalttc)
