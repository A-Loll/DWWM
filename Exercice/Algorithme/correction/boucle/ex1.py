# demande à l'utilisateur un chiffre compris et stocker dans une variable chiffre
# tant que chiffre est diférent à 1 ou 3
# demande à l'utilisateur un chiffre compris et stocker dans une variable chiffre

number  =   input('saisisez un chiffre compris entre 1 et 3 : \n')
while  ( number.isdigit() == False or int(number) < 1 or int(number) > 3 ):
    number  =   input('saisie invalide\nsaisisez un chiffre compris entre 1 et 3\n')
print(f'Merci d\'avoir saisi {number}')