# Générateur de mot de passe

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Licence](https://img.shields.io/badge/licence-MIT-green)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

## Description

Un simple programme Python permettant de généré des mots de passes sécurisés

## ✨ Fonctionnalités

- **Génération de mots de passe sécurisés** : Crée des mots de passe aléatoires et robustes avec des lettres majuscules, minuscules, des chiffres et des caractères spéciaux.
  
- **Personnalisation** : 
   - Définir la **longueur** du mot de passe.
   - Choisir si le mot de passe doit inclure **des majuscules**, **des minuscules**, **des chiffres**, et **des caractères spéciaux**.

- **Utilisation de `secrets` pour la sécurité** : Utilisation du module `secrets` de Python pour garantir des choix aléatoires cryptographiquement sûrs, idéal pour les mots de passe.

- **Vérification de la sécurité** : Si l'utilisateur entre une longueur trop courte (moins de 14 caractères), un avertissement est affiché pour garantir une meilleure sécurité.

- **Messages esthétiques** : Affichage de messages clairs et esthétiques pour indiquer que le mot de passe a été généré avec succès, avec des emojis et des séparateurs pour rendre l'interface agréable.

## Technologies utilisées

- Python 3.x

## 🚀 Installation

1. Installation de python :
   ```bash
   pip install python
## 🤝 Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Faites un fork de ce dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commitez vos changements (`git commit -am 'Ajout de ma fonctionnalité'`).
4. Poussez vos modifications (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une pull request.
