chosenNumber    =   input('entrez un nombre compris entre 10 et 20 :\n')
# chosenNumber >= 10 et chosenNumber <= 20 -> inversion : chosenNumber < 10 ou chosenNumber > 20
while (chosenNumber.isdigit() == False) or int(chosenNumber) > 20 or int(chosenNumber) < 10:

    if( chosenNumber.isdigit() == True ) :
        chosenNumber    =   int(chosenNumber)
        if chosenNumber > 20 :
            print('Plus petit !')
        elif chosenNumber < 10 :
            print('Plus grand !')
        chosenNumber    =   input('entrez un nombre compris entre 10 et 20 :\n')
    else :
        chosenNumber    =   input(f'{chosenNumber} n\'est pas un nombre!\nentrez un nombre compris entre 10 et 20 :\n')
print(f'Merci d\'avoir selectionner {chosenNumber}')