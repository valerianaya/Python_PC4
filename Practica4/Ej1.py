# Paso 1: Guardar el texto en un archivo
with open("texto.txt", "w", encoding="utf-8") as archivo:
    texto_inicial = "En el ámbito del desarrollo de software, la colaboración es fundamental. La colaboración eficiente impulsa la eficacia y mejora la calidad del código. La calidad del código, a su vez, es esencial para la mantenibilidad del sistema. Mantener un sistema sin problemas es esencial para la satisfacción del cliente. La satisfacción del cliente, por supuesto, es un objetivo clave para cualquier equipo de desarrollo. Desarrollar estrategias para fomentar la colaboración continua y mejorar la calidad del código es una práctica que beneficia a todos los miembros del equipo y contribuye al éxito general del proyecto"
    archivo.write(texto_inicial)

# Paso 2: Leer el archivo y contar la palabra "la"
with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    cantidad_la = contenido.lower().split().count("la")

print(f"La palabra 'la' aparece {cantidad_la} veces en el texto.")

# Paso 3: Ingresar un nuevo texto y añadirlo al final del archivo
nuevo_texto = input("Ingrese un nuevo texto para añadir al final del archivo: ")
with open("texto.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\n" + nuevo_texto + "\n")

print("Texto añadido al final del archivo.")
