import random
import pickle

# Función para generar una lista de números aleatorios
def generar_lista_aleatoria(longitud):
    lista = [random.randint(1, 100) for _ in range(longitud)]
    return lista

# Función para guardar el estado de la lista en un archivo
def guardar_estado(lista, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(lista, f)

# Función para cargar el estado de la lista desde un archivo
def cargar_estado(archivo):
    with open(archivo, 'rb') as f:
        lista = pickle.load(f)
    return lista

# Pregunta al usuario si desea generar una nueva lista o cargar una existente
opcion = input("¿Deseas generar una nueva lista (S/N)? ").strip().lower()

if opcion == 's':
    longitud = int(input("Ingrese la longitud de la lista: "))
    lista_aleatoria = generar_lista_aleatoria(longitud)
    archivo_estado = "estado_lista.pkl"
    guardar_estado(lista_aleatoria, archivo_estado)
    print(f"Lista generada: {lista_aleatoria}")
    print(f"Estado guardado en '{archivo_estado}'")
elif opcion == 'n':
    archivo_estado = "estado_lista.pkl"
    try:
        lista_cargada = cargar_estado(archivo_estado)
        print(f"Lista cargada desde '{archivo_estado}': {lista_cargada}")
    except FileNotFoundError:
        print(f"El archivo '{archivo_estado}' no existe.")
else:
    print("Opción no válida. Por favor, ingrese 'S' para generar una nueva lista o 'N' para cargar una existente.")