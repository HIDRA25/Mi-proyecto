import os # primero importo la libreria os
import readchar  #importo la libreria readchar para leer la tecla 'n'

def limpiar_e_imrpimir(): #defino mi funcion 
    numero = 0
    while numero <= 50: # uso el bucle while para imprimir los numeros de 0 a 50
        print(numero)
        tecla = readchar.readkey() # esta linea me permite leer una sola tecla, en este caso la 'n'
        if tecla == "n":
            os.system('cls' if os.name=='nt' else 'clear') # esta instruccion borra la terminal antes de imprimir el nuevo numero
        numero += 1


limpiar_e_imrpimir () #llamo la funcion para ejecutar el proceso 

