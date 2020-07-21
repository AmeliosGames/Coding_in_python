numeros_introducidos = []
numeros_pares = []
numeros_inpares = []

print("Escoge dos números que sean iguales o mayores que cero con la condición de que uno sea mayor que otro")

numero_menor = int(input("Escribe el número menor: "))
numero_mayor = int(input("Escribe el numero mayor: "))
if numero_mayor == numero_menor or numero_menor > numero_mayor or numero_mayor < 0 or numero_menor < 0:
    print("Lo siento esos números no son válidos introduce otros")
else:
    numeros_introducidos = range(numero_menor, numero_mayor + 1)
    for numeros in numeros_introducidos:
        if numeros % 2 == 0:
            numeros_pares.append(numeros)
        else:
            numeros_inpares.append(numeros)

    print("Los números pares son ", numeros_pares)
    print("Los números inmpares son", numeros_inpares)












