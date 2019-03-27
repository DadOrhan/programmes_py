def triListe(data):
    return data[1]

inventaire = [("pommes", 22),("melons", 4),("poires", 18),("fraises", 76),("prunes", 51),]

# Sorting list of Integers in descending 
inventaire.sort(key = triListe, reverse = True)
print(inventaire)