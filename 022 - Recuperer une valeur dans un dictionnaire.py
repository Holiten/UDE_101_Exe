employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}

print(employes.get("01").get("identite").get("prenom"))

# avec vérification d'erreur

print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))