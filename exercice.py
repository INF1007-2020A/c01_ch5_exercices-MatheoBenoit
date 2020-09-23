#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math

def convert_to_absolute() -> float:
    x = float(input("Veuillez entrer un nombre:"))
    return abs(x)


def use_prefixes() -> List[str]:
 prefixes, suffixes = 'JKLMNOPQ', 'ack'

 result = []
 for r in prefixes:
     result.append(r + suffixes)
    
 return result


def prime_integer_summation() -> int:
    liste = []
    i = 2
    while len(liste) < 100:
        prime = True
        for divider in range(2, int(math.sqrt((i))+ 1)):
            if i % divider == 0:
               prime = False

        if prime:
           liste.append(i)

        i += 1   
    
    return sum(liste)


def factorial(number: int) -> int:
    valeur = 1
    while (number > 0):
        valeur = number*valeur

        number -= 1

    return valeur

    #ou math.factorial(number)


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue 
        else:
            print(i)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
