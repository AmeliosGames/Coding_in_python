import random
vida = 84
consecuencias = {"terremoto": "Ha habido un terremoto y has perdido 5 años de vida", "tornado":"Ha habido un tornado has perdido 7 años de vida","acidente_de_coche": "Has perdido 20 años de vida", "accidente_de_avion": " Has sufido un accidente de avión has perdido la vida", "accidente_de_tren" : "Has sufrido un accidente de tren has perdido 50 años de vida", "enfermedad_severa" : "Has pasado un enfermedad severa has perdido 3 años de vida"}
anos_vividos = 0
que_te_ha_pasado =[]
while vida > 0:
    vida -= 1
    posibilidades = int(random.randrange(100))
    if posibilidades == 1:
        print(consecuencias["terremoto"])
        vida -= 5
        que_te_ha_pasado.append("Has sufrido un terremoto")
    elif posibilidades == 50:
        print(consecuencias["tornado"])
        vida -= 7
        que_te_ha_pasado.append("Has sufrido un tornado")
    elif posibilidades == 100:
        print(consecuencias["acidente_de_coche"])
        vida -= 10
        que_te_ha_pasado.append("Has sufrido un accidente de coche")
    elif posibilidades == 25:
        print(consecuencias["accidente_de_avion"])
        vida = 0
        que_te_ha_pasado.append("Has sufrido un accidente de avión")
    elif posibilidades == 75:
        print(consecuencias["accidente_de_tren"])
        vida -= 50
        que_te_ha_pasado.append("Has sufrido un accidente de tren")
    elif posibilidades == 15:
        print(consecuencias["enfermedad_severa"])
        vida -= 3
        que_te_ha_pasado.append("Has sufrido una enfermedad severa")
    anos_vividos += 1
    if vida >= 0:
        print("Te quedan", vida,"años")


print("En esta vida has vivido " + str(anos_vividos), "y has sufrido estas cosas: " +str(que_te_ha_pasado))




















