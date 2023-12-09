# main.py
import random
from pyfiglet import Figlet

def mostrar_menu():
    print("----- Menú -----")
    print("1. Opción 1")
    print("2. Opción 2")
    print("2.1. Cambiar título con pyfiglet")
    print("3. Opción 3")
    print("4. Salir")

def cambiar_titulo_con_pyfiglet():
    texto_imprimir = input("Ingrese el texto para el nuevo título: ")

    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente_seleccionada = random.choice(fuentes_disponibles)
    
    figlet.setFont(font=fuente_seleccionada)
    titulo = figlet.renderText(texto_imprimir)
    
    print(f"\nNuevo título:")
    print(titulo)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Realizando la Opción 1")

        elif opcion == "2":
            print("Realizando la Opción 2")

        elif opcion == "2.1":
            cambiar_titulo_con_pyfiglet()

        elif opcion == "3":
            print("Realizando la Opción 3")

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
