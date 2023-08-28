import random
import logging

logging.basicConfig(filename='divisiones.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError as e:
        logging.error("División entre cero: %s", e)
        return None

valores = []

for _ in range(50):
    a = random.randint(1, 100)
    b = random.randint(0, 10)
    valores.append((a, b))

for a, b in valores:
    resultado = dividir(a, b)
    if resultado is not None:
        logging.info("División de %d entre %d es igual a %.2f", a, b, resultado)