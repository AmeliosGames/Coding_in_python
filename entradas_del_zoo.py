str = "¡Bien benido a Terra Natura!"
print(str)
print("." * len(str))
agua = 10
comida= 10
dinero = int(input("¿Cuanto dinero tienes?"))

while dinero < 20:
    print("Lo siento. Con esa cantidad no puedes entrar a Terra Natura")
    dinero = int(input("¿Cuanto dinero tienes?"))

class animal:
    def __init__(self, comida, agua, nombre):
        self.nombre = nombre
        self.comida = comida
        self.agua = agua
        print("Tenemos", agua, "de agua y", comida, "Kg de comida")
    def comer(self):
       if self.comida > 0:
            self.comida -= 1
            print("El", self.nombre, " ha comido 1 Kg de comida")
       else:
           print("No hay comida para comer")
    def beber(self):
        if self.agua > 0:
            self.agua -= 1
            print("El", self.nombre, "a bebido 1l de agua")
        else:
            print("No hay agua para beber")

class cocodrilo(animal):
    pass
class buho(animal):
    pass
class perro(animal):
    pass

animal_ver = input("¿Qué animal te gustaría ver entre un cocodrilo, un búho o un perro?")

while comida or agua > 10:
    while animal_ver.upper() != "COCODRILO" and animal_ver.upper() != "BUHO" and animal_ver.upper() != "PERRO":
        print("No tenemos esos animales en Terra Natura")
        animal_ver = input("¿Qué animal te gustaría ver entre un cocodrilo, un búho o un perro?")
    print("Has escogido el", animal_ver, "para ver.")
    animal.nombre = animal_ver
    accion = input("¿Quieres darle de comer o de beber?")

    while accion.upper() != "COMER":
        print("No entiendo lo que quieres decirme puedes escribir bien cenutrio")
        accion = input("¿Quieres darle de comer?")
    animal.comer(10)

    while accion.upper() != "BEBER":
        print("No entiendo lo que quieres decirme puedes escribir bien cenutrio")
        accion_beber = input("¿Quieres darle de beber?")
    animal.beber(cocodrilo)















































