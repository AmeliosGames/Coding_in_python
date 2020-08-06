from io import open

texto = open("documento_de_prueba.txt", "r+")
frase = texto.read()
texto.seek(0)
texto.write(frase.replace(".", "\n"))














