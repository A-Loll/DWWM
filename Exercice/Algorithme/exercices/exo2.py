# nombre=input("entrez un nombre : ")
# nombre2=input("entre un second nombre : ")
# nombre=float (nombre)
# nombre2=float (nombre2)
# valeur=(nombre*nombre2)
#if (valeur<0) :
#     print ("négatif")
# else :
#     print ("positif")


# age=input ("entrez un âge : ")
# age=int (age)
# if (age==8 or age==9):
#    print ("Microbe")
# if (age==10 or age==11):
#    print ("Poussin")
# if (age==12 or age==13):
#    print ("Benjamine/Benjamin")
# if (age==14 or age==15):
#    print ("Minime")
# if (age==16 or age==17):
#    print ("Cadette/Cadet")
# if (age==18 or age==19):
#    print ("Junior")
# if (age==20 or age<=39):
#    print ("Sénior")
# if (age>=40):
#    print ("Vétérane/Vétéran")



nbPhotocopie=input ("Nombre de photocopie : ")
if (nbPhotocopie <= 10):
    print(f"facture de {nbPhotocopie*0.10: .2f} €")
elif (nbPhotocopie <= 30):
    print(f"facture de {10 * 0.10 + (nbPhotocopie - 10) * 0.09: .2f} €")
elif (nbPhotocopie > 30):
    print(f"facture de {10 * 0.10 + 20 *0.09 + (nbPhotocopie - 30) * 0.08: .2f} €")