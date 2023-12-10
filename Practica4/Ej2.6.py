# main.py
import random
from pyfiglet import Figlet

# Agrega tus importaciones necesarias (por ejemplo, para SQLAlchemy y requests)

# Definir una lista de productos como ejemplo
productos = [
    {"nombre": "Producto1", "precio": 10.0, "stock": 50},
    {"nombre": "Producto2", "precio": 20.0, "stock": 30},
    {"nombre": "Producto3", "precio": 15.0, "stock": 40},
]

clientes = []

def mostrar_menu():
    print("----- Menú -----")
    print("1. Opción 1")
    print("2. Opción 2")
    print("2.1. Cambiar título con pyfiglet")
    print("2.2. Crear tablas tipo_cambio y cliente")
    print("2.3. Actualizar tipo de cambio desde API")
    print("2.4. Editar Precio")
    print("2.5. Editar Stock")
    print("2.6. Buscar Producto por Nombre")
    print("2.7. Agregar Cliente")
    print("2.8. Listar Clientes")
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

# Agrega tus funciones de configuración y actualización de tipo de cambio aquí

def editar_precio():
    # Lógica para editar el precio de un producto
    print("Editando Precio")

def editar_stock():
    # Lógica para editar el stock de un producto
    print("Editando Stock")

def buscar_producto_por_nombre():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    resultado = [producto for producto in productos if producto["nombre"].lower() == nombre_buscar.lower()]

    if resultado:
        print("Producto(s) encontrado(s):")
        for producto in resultado:
            print(producto)
    else:
        print("Producto no encontrado.")

def agregar_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    clientes.append({"nombre": nombre_cliente})
    print("Cliente agregado exitosamente.")

def listar_clientes():
    print("Clientes:")
    for cliente in clientes:
        print(cliente["nombre"])

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

        elif opcion == "2.2":
            # Lógica para crear tablas tipo_cambio y cliente
            print("Creando tablas tipo_cambio y cliente")

        elif opcion == "2.3":
            # Lógica para actualizar tipo de cambio desde API
            print("Actualizando tipo de cambio desde API")

        elif opcion == "2.4":
            editar_precio()

        elif opcion == "2.5":
            editar_stock()

        elif opcion == "2.6":
            buscar_producto_por_nombre()

        elif opcion == "2.7":
            agregar_cliente()

        elif opcion == "2.8":
            listar_clientes()

        elif opcion == "3":
            print("Realizando la Opción 3")

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
