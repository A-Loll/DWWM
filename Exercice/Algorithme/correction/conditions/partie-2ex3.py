# demande un nombre et stock dans une variable age
# si l'age est au dessus ou égale à 8 et en dessous ou égal à 9ans 
#     alors ecrire "microbe"
# sinon si l'age est au dessus ou égale à 10 et en dessous ou égal à 11ans 
#     alors ecrire "poussin"
# sinon si l'age est au dessus ou égale à 12 et en dessous ou égal à 13ans 
#     alors ecrire "Benjamin.e"
# sinon si l'age est au dessus ou égale à 14 et en dessous ou égal à 15ans 
#     alors ecrire "minime"
# sinon si l'age est au dessus ou égale à 16 et en dessous ou égal à 17ans 
#     alors ecrire "Cadet.te"
# sinon si l'age est au dessus ou égale à 18 et en dessous ou égal à 19ans 
#     alors ecrire "Junior"
# sinon si l'age est au dessus ou égale à 20 et en dessous ou égal à 39ans 
#     alors ecrire "Sénior"
# sinon si l'age est au dessus ou égale à 40
#     alors ecrire "Vétéran.e"


age =   int(input("entrez l'age pour avoir la catégorie : "))

if ( 8 <= age <= 9 ):
    print("Microbe")
elif  (age >= 10) & (age <= 11) :
    print("Poussin")
elif  age >= 12  and  age <= 13 :
    print("Benjamin.e")
elif ((age >= 14) & (age <= 15)):
    print("Minime")
elif ((age >= 16) & (age <= 17)):
    print("Cadet.te")
elif ((age >= 18) & (age <= 19)):
    print("Junior")
elif ((age >= 20) & (age <= 39)):
    print("Senior")
elif age >= 40:
    print("Vétéran.e")
elif 0 < age < 8 :
    print('trop jeune')
else :
    print("hors catégories")