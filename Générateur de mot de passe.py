import random
import string
import secrets

def generer_mot_de_passe(longueur=14, inclure_speciaux=True, inclure_chiffres=True, inclure_majuscule=True, inclure_minuscule=True):
    if longueur < 14:
        print("\n⚠️ Avertissement : Un mot de passe de moins de 14 caractères est moins sécurisé. Il est recommandé d'utiliser une longueur plus grande pour une meilleure protection.\n")

    # Définir les caractères possibles en fonction des préférences
    caracteres_possibles = ""
    
    if inclure_minuscule:
        caracteres_possibles += string.ascii_lowercase
    if inclure_majuscule:
        caracteres_possibles += string.ascii_uppercase
    if inclure_chiffres:
        caracteres_possibles += string.digits
    if inclure_speciaux:
        caracteres_possibles += string.punctuation

    # Vérifier que des catégories ont été sélectionnées
    if not caracteres_possibles:
        print("\nErreur : Vous devez inclure au moins une catégorie de caractères (minuscule, majuscule, chiffres ou caractères spéciaux).\n")
        return None

    # S'assurer que le mot de passe contient au moins un caractère de chaque catégorie
    mot_de_passe = []
    
    if inclure_minuscule:
        mot_de_passe.append(secrets.choice(string.ascii_lowercase))
    if inclure_majuscule:
        mot_de_passe.append(secrets.choice(string.ascii_uppercase))
    if inclure_chiffres:
        mot_de_passe.append(secrets.choice(string.digits))
    if inclure_speciaux:
        mot_de_passe.append(secrets.choice(string.punctuation))

    # Ajouter des caractères aléatoires jusqu'à atteindre la longueur souhaitée
    mot_de_passe += [secrets.choice(caracteres_possibles) for _ in range(longueur - len(mot_de_passe))]

    # Mélanger le mot de passe pour le rendre plus difficile à deviner
    random.shuffle(mot_de_passe)

    # Convertir la liste de caractères en une chaîne et retourner le mot de passe
    mot_de_passe_str = ''.join(mot_de_passe)
    
    # Afficher un message esthétique
    print("\n----------------------------------------------------")
    print("🔒 Ton mot de passe sécurisé a été généré avec succès ! 🔒")
    print("----------------------------------------------------\n")
    print(f"Mot de passe généré : {mot_de_passe_str}\n")
    print("----------------------------------------------------")
    print("✨ Assure-toi de bien le conserver dans un endroit sûr ! ✨")
    print("----------------------------------------------------\n")
    return mot_de_passe_str


# Exemple d'utilisation avec des options personnalisées
longueur = 16  # Longueur du mot de passe
mot_de_passe = generer_mot_de_passe(longueur, inclure_speciaux=True, inclure_chiffres=True, inclure_majuscule=True, inclure_minuscule=True)
