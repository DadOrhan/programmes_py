#/Users/MrBombastic/Desktop/py/multipli.py

"""module multipli contenant la fonction table"""
msg = 'Ouverture du programme réussie'
def message():
    print(msg)

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# test de la fonction table
if __name__ == "__main__":
    message()