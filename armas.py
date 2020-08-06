from io import open

registro_texto = open("registro_de_disparos.txt", "w")


class Metralleta:
    def __init__(self,durabilidad=100, temperatura=15, municion=None, disparos=0):
        self.durabilidad = durabilidad
        self.temperatura = temperatura
        self.municion = municion
        self.disparos = disparos

    def disparar(self):
        while self.municion > 0 and self.durabilidad > 0:
            self.disparos += 1
            self.temperatura += 0.25
            self.municion -= 1
            registro_texto.write("\n El arma ha disparadado. Este es el disparo numero " + str(self.disparos))
            registro_texto.write(" La duarabilidad es de " + str(self.durabilidad))
            registro_texto.write(" Quedan estas balas " + str(self.municion))
            if self.temperatura > 100:
                self.durabilidad -= 0.1
            if self.durabilidad <= 0:
                print("El arma se ha roto")
                print("Han quedado", self.municion, " balas")
                print("Se han alcanzado los", self.temperatura, "grados de temperatura")
            if self.municion <= 0:
                print("El arma se ha qudado sin municion")
                print("Se han alcanzado los", self.temperatura, "grados de temperatura")


n_municion = int(input("¿Cuanta munición quieres disparar?: "))

while n_municion < 100:
    print("Eso es muy poco trae un poco más de munición")
    n_municion = input("¿Cuanta munición quieres disparar?: ")

aviso = input("¿Estás listo para disparar?: ")

while aviso.upper() != "SI":
    print("Pues aquí está todo listo así que date prisa")
    aviso = input("¿Estás listo para disparar?: ")

arma = Metralleta(municion=n_municion)
arma.disparar()
registro_texto.close()











