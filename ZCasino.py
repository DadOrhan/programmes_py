#/Users/MrBombastic/Desktop/py/ZCasino.py
import random
import math

bankroll_player = 50
numero_player = input('Faites vos jeux : ')
numero_gagnant = random.randrange(50)
couleur_numero_gagnant = numero_gagnant % 2
mise_joueur = input('Choississez votre mise : ')
continuer_partie = True
print('Le numéro gagant est:', numero_gagnant)



try:
    numero_player = int(numero_player) # Conversion du numéro en Integer
    assert numero_player < 50
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("Impossible de sélectionner un nombre supérieur à 50")

try:
    mise_joueur = int(mise_joueur) # Conversion du numéro en Integer
except ValueError:
    print("Vous n'avez pas saisi un nombre.") 

if(numero_gagnant == numero_player): # Si joueur gagne
    bankroll_player = bankroll_player + mise_joueur * 3
    print('Vous avez gagné !', 'Il vous reste', ' ', bankroll_player) # Si joueur a la bonne couleur
elif(numero_gagnant % 2 == 0 and numero_player % 2 == 0) or (numero_gagnant % 2 == 1 and numero_player % 2 == 1):   
    bankroll_player = bankroll_player - math.ceil(mise_joueur/2)
    print('Vous récupérez la moitié de votre mise:', (mise_joueur/2), 'Il vous reste', ' ', bankroll_player)
elif (numero_gagnant != numero_player): # Si joueur perd
    bankroll_player = bankroll_player - mise_joueur
    print('Vous avez perdu !', 'Il vous reste', ' ', bankroll_player)

while continuer_partie: # Tant qu'on doit continuer la partie
    # on demande à l'utilisateur de saisir le nombre sur
    # lequel il va mise
 # On interrompt la partie si le joueur est ruiné
    if bankroll_player <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", bankroll_player, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False
        if quitter == "n" or quitter == "N":
            input('La chnce va tourner.. Choisissez un nouveau numéro ')

