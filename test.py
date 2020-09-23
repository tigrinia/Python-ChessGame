
# 1) On émet une variable 'running' qui est vraie pour faire rouler la boucle indéfiniment.
running = True

# 2) Tant que cette variable est vraie, on va continuer à demander l'input de l'utilisateur.
while running:
    userInput = input('Entrez un nombre entier positif (0 pour terminer): ')

    # 3) Afin d'éviter une erreure de conversion causée par int() on va vérifier si la valeur
    # peut être convertie en nombre entier. Si c'est le cas, on transforme le 'string' en 'int'.
    if userInput.isnumeric():
        number = int(userInput)

        # 4) Dans le vif du sujet, on vérifie si le nombre est positif.
        if number > 0:
            # 4.1) Si c'est 1, on redonne les facteurs de 1 (cas special).
            if number == 1:
                print('La décomposition en facteurs premiers est: 1')            

            # 4.2) Ceci est le programme principal
            else:
                # 4.3 ) On enregistre quelques variables dont 'smallestDivisors' qui est l'initialisation
                # de la SÉQUENCE  
                smallestDivisors = ()
                a = 0
                multiplication = 1
                storedNumber = number
                
                while multiplication != number:
                    multiplication = 1
                    a = 0
                    # 4.4) Dans cette boucle, on va aller chercher le premier nombre premier qui divise 
                    # le nombre que l'utilisateur donne.
                    for i in range(2, storedNumber + 1):
                        # 4.4.1) Une fois qu'on a ce 'premier nombre premier', on va l'ajouter dans notre 
                        # SÉQUENCE, on va le mettre dans 'storedNumber' et on va rendre la variable 
                        # 'a' = 1 pour ne pas en cherche d'autres.
                        if storedNumber % i == 0 and a < 1:
                            smallestDivisors = smallestDivisors + (i,)
                            storedNumber = int(storedNumber / i)
                            a = a + 1
                    # 4.4.2) Ceci est notre condition pour sortir de la boucle 'while'. En gros, on va prendre
                    # tout les nombres dans la liste, et les multiplier ensembles. Si le produit de la multiplication
                    # est egal au nombre transmis par l'utilisateur, on sors de la boucle. Dans le cas inverse,
                    # on réinitialise 'multiplication' à 1, 'a' à 0 et la boulce repart pour trouver le premier
                    # nombre premier qui peut diviser notre reste.
                    for j in smallestDivisors:
                        multiplication = multiplication * j
                
                # 4.3) On imprime sur la console la décomposition de notre nombre en facteur premiers.
                print('La décomposition en facteurs premiers est: ', end='')
                print(*smallestDivisors, sep=' * ')

        # 5) Dans le cas où le nombre n'est pas égal à un nombre positif on ferme le programme en 
        # rendant 'running' faux, ce qui arrête la boucle principale (PS : seulement 0 va rendre 
        # 'running' faux).
        else:
            print('Le programme va maintenant se fermer. Merci et au revoir!')
            running = False
    
    # 6) Dans le cas ou on entre un caractere qui ne rend pas 'isnumeric()' vrai (incluant les nombres négatifs)
    # on va dire à l'utilisateur qu'il à fait une entrée non valide.
    else:
        print('Erreur, entrée non valide.')