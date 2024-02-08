import readchar


nombre = input("¡jugador! ¡ingresa tu nickname!: ")
print("¡Bienveid@ a esta travesía! ",nombre," ¡toma las desiciones correctas!")




while True:
    char = readchar.readkey()
    if char == readchar.key.UP:
        print("Fin del programa")
        break
    else:
        print("Tecla presionada:", char)