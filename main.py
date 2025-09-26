"""Module palindrome"""
import unicodedata


#### Fonction secondaire


def ispalindrome(p):
    """Verifie si la chaine p est un palindrome"""

    # Mettre en minuscules
    p = p.lower()
    # Enlever les accents
    p = ''.join(
        c for c in unicodedata.normalize('NFD', p)
        if unicodedata.category(c) != 'Mn'
    )
    # Garder uniquement lettres et chiffres
    p = ''.join(c for c in p if c.isalnum())
    return p == p[::-1]
#### Fonction principale


def main():
    """Fonction principale 
    Appelle la fonction secondaire ispalindrome()"""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
