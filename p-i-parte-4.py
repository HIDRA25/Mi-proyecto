#importo las librerias necearias para mi proyecto en este caso: os y readchar
import os 
import readchar

#mapa laberinto
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

#Esta funcion recibe el mapa del laberinto en forma de cadena y lo convierte a matriz 
def laberinto_a_matriz(laberinto):
    filas = laberinto.split('\n') # dividir el laberinto en filas
    matriz =[list(fila) for fila in filas] #convertir en lista de caracteres
    return matriz

#llamo la funcion guardandola en la variable map
mapa = laberinto_a_matriz (laberinto)

#defino las coordenadas de punto de inicio y final 
inicio = (0, 0) #coordenadas punto inical 
fin =  (len(mapa)-1, len(mapa[0])-1) # coordenadas punto final 

#funciones para limpiar y mostrar el mapa 
def limpiar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')

def mostrar_mapa(mapa):
    for fila in mapa:
        print(''.join(fila))

 #llamo a las funciones para tener una vision clara y actualizada del mapa 
limpiar_pantalla()
mostrar_mapa(mapa)
#funcion main loop
def main_loop(mapa: list[list[str]], inicio: tuple[int, int], fin: tuple[int, int]):
    px, py = inicio #variables que inicia como los valores de la posicion inicial
    while (px, py) != fin:
        mapa [px][py] = 'p' #asigno el caracter 'p' a las coordenadas px, py´
        #llamo a las funciones para tener una vision clara y actualizada del mapa 
        limpiar_pantalla()
        mostrar_mapa(mapa)

        key = readchar.readkey() #leer del teclado las teclas ↑ ↓ ← →
        #implemento el resto del bucle para leer las teclas ↑ ↓ ← → verificando que no atraviese las paredes y que no se salga del mapa 
        if key ==readchar.key.UP and mapa[px-1][py] != '#':
            new_px, new_py = px -1, py
        elif key == readchar.key.DOWN and mapa[px+1][py] != '#':
            new_px, new_py = px +1, py
        elif key == readchar.key.LEFT and mapa[px][py-1] != '#':
            new_px, new_py = px, py -1
        elif key == readchar.key.RIGHT and mapa[px][py+1] != '#':
            new_px, new_py = px, py +1
        else:
            continue #si la tecla oprimida no es valida continuara la siguiente iteracion 

        #verifico si la nueva posicion es valida y actualizo el mapa 
        if 0 <= new_px < len(mapa) and 0 <= new_py < len(mapa[0]):
            mapa[px][py] = '.'#restaura la posicion anterior 
            px, py = new_px, new_py #actualiza px, py con las nuevas coordenadas 
            mapa [px][py] = 'p' #asignar 'p' en la nueva coordenada 
    print("¡Felicidades! ¡Ayudaste al preso a conseguir su libertad!")      

main_loop(mapa,inicio,fin)   #llamo la funcion main_loop para inicializar el bucle principal del juego         


               

