import os
import random
import readchar

class Juego:
    def __init__(self, laberinto, inicio, fin):
        self.mapa = self.laberinto_a_matriz(laberinto)
        self.inicio = inicio
        self.fin = fin
        self.px, self.py = self.inicio
    
    def laberinto_a_matriz(self, laberinto):
        filas = laberinto.split('\n')  # dividir el laberinto en filas
        matriz = [list(fila) for fila in filas]  # convertir en lista de caracteres
        return matriz
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_mapa(self):
        for fila in self.mapa:
            print(''.join(fila))
    
    def main_loop(self):
        while (self.px, self.py) != self.fin:
            self.mapa[self.px][self.py] = 'p'  # asigno el caracter 'p' a las coordenadas px, py
            # llamar a las funciones para tener una visión clara y actualizada del mapa
            self.limpiar_pantalla()
            self.mostrar_mapa()
            
            key = readchar.readkey()  # leer del teclado las teclas ↑ ↓ ← →
            # implemento el resto del bucle para leer las teclas ↑ ↓ ← → verificando que no atraviese las paredes y que no se salga del mapa 
            if key == readchar.key.UP and self.mapa[self.px-1][self.py] != '#':
                new_px, new_py = self.px - 1, self.py
            elif key == readchar.key.DOWN and self.mapa[self.px+1][self.py] != '#':
                new_px, new_py = self.px + 1, self.py
            elif key == readchar.key.LEFT and self.mapa[self.px][self.py-1] != '#':
                new_px, new_py = self.px, self.py - 1
            elif key == readchar.key.RIGHT and self.mapa[self.px][self.py+1] != '#':
                new_px, new_py = self.px, self.py + 1
            else:
                continue  # si la tecla oprimida no es válida, continuará la siguiente iteración
            
            # verifico si la nueva posición es válida y actualizo el mapa
            if 0 <= new_px < len(self.mapa) and 0 <= new_py < len(self.mapa[0]):
                self.mapa[self.px][self.py] = '.'  # restaura la posición anterior
                self.px, self.py = new_px, new_py  # actualiza px, py con las nuevas coordenadas
                self.mapa[self.px][self.py] = 'p'  # asignar 'p' en la nueva coordenada
        print("¡Felicidades! ¡Ayudaste al preso a conseguir su libertad!")


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        archivo_mapa = self.elegir_archivo_aleatorio(path_a_mapas)
        laberinto, inicio, fin = self.leer_mapa(f"{path_a_mapas}/{archivo_mapa}")
        super().__init__(laberinto, inicio, fin)

    def elegir_archivo_aleatorio(self, path):
        archivos = os.listdir(path)
        return random.choice(archivos)

    def leer_mapa(self, path_completo):
        with open(path_completo, 'r') as file:
            contenido = file.readlines()
        
        # Remove any empty lines and strip whitespace
        contenido = [line.strip() for line in contenido if line.strip()]
        
        if len(contenido) < 3:
            raise ValueError("El archivo de mapa no contiene suficiente información.")

        # Read the dimensions and coordinates
        try:
            coordenadas = contenido[0].split()
            inicio = tuple(map(int, coordenadas[0:2]))
            fin = tuple(map(int, coordenadas[2:4]))
        except ValueError as e:
            raise ValueError(f"Error al leer las coordenadas del mapa: {e}")

        # leer el mapa
        laberinto = '\n'.join(contenido[1:])

        return laberinto, inicio, fin

# Definir el path a la carpeta con los mapas
path_a_mapas = "mapas"

# Instanciar el juego desde archivos y ejecutarlo
juego_archivo = JuegoArchivo(path_a_mapas)
juego_archivo.main_loop()
