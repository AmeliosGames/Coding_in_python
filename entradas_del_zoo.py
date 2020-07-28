str = "¡Bienvenido a Terra Natura!"
print(str)
print("." * len(str))
dinero = int(input("¿Cuanto dinero tienes?: "))

while dinero < 20:
    print("Lo siento. Con esa cantidad no puedes entrar a Terra Natura")
    dinero = int(input("¿Cuanto dinero tienes?: "))


class animal:
    def __init__(self, comida= None, agua=None, nombre=None):
        self.nombre = nombre
        self.comida = comida
        self.agua = agua

    def comer(self):
       if self.comida > 0:
            self.comida -= 1
            print("El", self.nombre, " ha comido 1 Kg de comida")
            print("Quedan", self.comida,"Kg de comida")
       else:
           print("No hay comida para comer")

    def beber(self):
        if self.agua > 0:
            self.agua -= 1
            print("El", self.nombre, "a bebido 1l de agua")
            print("Quedan", self.agua, "l de agua")
        else:
            print("No hay agua para beber")


animal_ver = input("¿Qué animal te gustaría ver entre un cocodrilo, un búho o un perro?: ")
while animal_ver.upper() != "PERRO" and animal_ver.upper() != "COCODRILO" and animal_ver.upper() != "BUHO":
    print("No tenemos esos animales")
    animal_ver = input("¿Qué animal te gustaría ver entre un cocodrilo, un búho o un perro?: ")


cuanta_agua = int(input("¿Cuanta agua le quieres echar? (No más de 9)"))
if cuanta_agua < 10:
    print("Vale")
elif cuanta_agua > 10:
    print("Eso es mucho")
    cuanta_agua = int(input("¿Cuanta agua le quieres echar? (No más de 9)"))

cuanta_comida = int(input("¿Cuanta comida le quieres echar? (No más de 9)"))
if cuanta_comida < 10:
    print("Vale")
elif cuanta_comida > 10:
    print("Eso es mucho")
    cuanta_comida = int(input("¿Cuanta comida le quieres echar? (No más de 9)"))
x = animal(nombre=animal_ver, comida=cuanta_comida, agua=cuanta_agua)
respuesta = ""
while respuesta != "SI":
    dar_de_comer = input("¿Quieres darle de comer: ?")
    while dar_de_comer.upper() != "SI" and dar_de_comer.upper() != "NO":
        print("No te entiendo")
        dar_de_comer = input("¿Quieres darle de comer: ?")
    if dar_de_comer.upper() == "SI":
        x.comer()
    elif dar_de_comer.upper() == "NO":
        print("Es una pena")
    dar_de_beber = input("¿Quieres darle de beber: ?")

    while dar_de_beber.upper() != "SI" and dar_de_beber.upper() != "NO":
        print("No te entiendo")
        dar_de_comer = input("¿Quieres darle de comer: ?")
    if dar_de_beber.upper() == "SI":
        x.beber()
    elif dar_de_beber.upper() == "NO":
        print("Es una pena")
    respuesta = input("¿Quieres salir: ?")























































