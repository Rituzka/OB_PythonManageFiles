def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        f.write(linea)

    f.close()


escribe('Fichero.txt', 'Hola, nuevo fichero')
