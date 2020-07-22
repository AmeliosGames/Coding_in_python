

lista_de_nombres = ["Maria", "Jose", "Pepa"]
cosas_de_personas = {"Maria": "María es charcutera", "Jose": "Es un panadero","Pepa": "Pepa es una enfermera que trabaja en Almería"}
print("Tengo nombres de ", lista_de_nombres[0], "de", lista_de_nombres[1], "y de", lista_de_nombres[2])

pregunta = "¡Hola! ¿Quieres iniciar sesión?"
print(pregunta)
respuesta = str(input("SI / NO: "))

while respuesta != "SI":
    print("Pues vale :C ")
    print(pregunta)
    respuesta = input("SI / NO: ")
print("¿Quieres ver algunos documentos de diferentes personas?")
respuesta2 = input("SI / NO: ")

while respuesta2 != "SI":
    respuesta3 = input("¿Quieres salir (SI / NO): ?")
    if respuesta3 == "NO":
        print("Eres tonto")
        respuesta2 = input("Quieres saber cosas de la gente (SI / NO): ")


conocer = input("Quieres saber algo de Maria de Jose o de Pepa")

if conocer == lista_de_nombres[0]:
    print(cosas_de_personas["Maria"])
elif conocer == lista_de_nombres[1]:
    print(cosas_de_personas["Jose"])
elif conocer == lista_de_nombres[2]:
    print(cosas_de_personas["Pepa"])
else:
    conocer = input("No te entiendo. ¿Quieres conocer a Maria, Jose o Pepa?: ")
salir = ""
algo_mas = input("¿Algo más: (SI / NO)?: ")
while salir != "SI":
    if algo_mas == "SI":
        conocer = input("¿Quieres conocer algo mas de Maria, Jose o Pepa?: ")
        print(cosas_de_personas[conocer])
        salir = input("¿Quieres salir: ?")
    elif algo_mas == "NO":
        salir = input("¿Quieres salir: ?")










