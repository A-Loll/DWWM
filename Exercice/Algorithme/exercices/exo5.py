# def helloWorld():
#     return "Bonjour tout le monde"
# print (helloWorld())

# def helloYou(firstname):
#     return "Bonjour" + firstname
# firstname = input("Entrez votre prénom :\n")
# print (helloYou(firstname))

# def average(a, b):
#     return (a + b) / 2
# nbr1 = float(input("Entrez un nombre : "))
# nbr2 = float(input("Entrez un nombre : "))
# moyenne = average(nbr1, nbr2)
# print(f"La moyenne de {nbr1} et {nbr2} est : {moyenne}")

def my_calcul(operation="add", *valeurs):
    resultat=None
    for valeur in valeurs:
        match operation:
            case "add":
                if resultat is None:
                    resultat=valeur
                else:
                    resultat+=valeur
            case "sub":
                if resultat is None:
                    resultat=valeur
                else:
                    resultat-=valeur
            case "mul":
                if resultat is None:
                    resultat=valeur
                else:
                    resultat*=valeur
            case "div":
                if resultat is None:
                    resultat=valeur
                else:
                    resultat/=valeur
    return resultat

res=my_calcul("sub",5,4)
print(f"calculatrice : {res}")