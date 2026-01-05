# demander le nombre de photocopie et le stocker dans un variable nbPhotocopie |nb_photocpie 
# si le nombre de photocopie est inférieur ou égal à 10
#     alors affcher 0.10*nbPhotocopie
# sinon si le nombre de photocopie est inférieur ou égal à 30
#     alors afficher 0.10*10 + 0.09 * (nbPhotocopie-10)
# sinon si le nombre de photocopie est strictement supérieur à 30
#     alors afficher 0.10*10+0.09*20+0.08*nbPhotocopie-30

nbPhotocopie    =   int(input("indiquez le nombre de photocopies : "))

if (nbPhotocopie <= 10):
    print(f"facture de {nbPhotocopie*0.10: .2f} €") | print("facture de ", nbPhotocopie, "€")
elif (nbPhotocopie <= 30):
    print(f"facture de {10 * 0.10 + ( nbPhotocopie - 10 ) * 0.09: .2f} €")
elif (nbPhotocopie > 30):
    print(f"facture de {10 * 0.10 + 20 * 0.09 + ( nbPhotocopie - 30 ) * 0.08: .2f} €")