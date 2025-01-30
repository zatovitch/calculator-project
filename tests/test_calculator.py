import sys
import os

# Ajouter le chemin du répertoire parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator

def calculatrice():
    print("Bienvenue dans la calculatrice Python !")
    print("Opérations disponibles : +, -, *, /")
    
    calc = Calculator()
    
    while True:
        try:
            # Demander à l'utilisateur de saisir le premier nombre
            num1 = float(input("Entrez le premier nombre : "))
            break
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
    
    while True:
        try:
            # Demander à l'utilisateur de saisir l'opérateur
            operateur = input("Entrez l'opérateur (+, -, *, /) : ")
            if operateur in ['+', '-', '*', '/']:
                break

            else:
                print("Opérateur invalide. Veuillez utiliser +, -, *, /")  
        except ValueError:
            print("Erreur : veuillez entrer un opérateur valide.")  

    while True:
        try:
            # Demander à l'utilisateur de saisir le deuxième nombre
            num2 = float(input("Entrez le deuxième nombre : "))
            break
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
    
    # Vérifier l'opérateur et effectuer l'opération
    if operateur == "+":
        resultat = calc.add(num1, num2)
    elif operateur == "-":
        resultat = calc.subtract(num1, num2)
    elif operateur == "*":
        resultat = calc.multiply(num1, num2)
    elif operateur == "/":
        if num2 != 0:
            resultat = calc.divide(num1, num2)
        else:
            print("Erreur : division par zéro !")
            return

    # Affichage du résultat
    print(f"Résultat : {num1} {operateur} {num2} = {resultat}")

# Exécuter la calculatrice
calculatrice()