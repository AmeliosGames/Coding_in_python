
respuesta = input("¿Te apetece crear un animal?: ")

while respuesta.upper() != "SI" and respuesta.upper() != "NO":
    print("No entiendo lo que me has dicho")
    respuesta = input("¿Te apetece crear un animal?: ")
respuesta_final = ""
while respuesta_final.upper() != "NO":
    class animal:
        def __init__(self,nombre=None,patas=None,color=None,aspecto=None):
            self.nombre = print(nombre)
            self.patas = print(patas)
            self.color = print(color)
            self.aspecto = print(aspecto)

    nombre_animal = input("¿Cómo quieres que se llama el animal?: ")
    patas_animal = input("¿Cuántas patas quieres que tenga el animal?: ")
    color_animal = input("¿De qué color quieres que sea el animal?: ")
    aspecto_animal = input("¿Quieres que el animal sea feo o guapo?")

    x = animal(nombre_animal, patas_animal, color_animal, aspecto_animal)
    callable(x.nombre)
    callable(x.patas)
    callable(x.color)
    callable(x.aspecto)
    respuesta_final = input("¿Quieres crear otro animal: ?")
