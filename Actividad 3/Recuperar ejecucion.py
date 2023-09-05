import tkinter as tk
from tkinter import messagebox
import pickle

def imprimir_tablero():
    for i in range(3):
        for j in range(3):
            btn = tk.Button(frame, text=tablero[i][j], width=10, height=3,
                            command=lambda row=i, col=j: hacer_movimiento(row, col))
            btn.grid(row=i, column=j)

def hacer_movimiento(row, col):
    global turno
    if tablero[row][col] == " ":
        tablero[row][col] = turno
        imprimir_tablero()
        if verificar_ganador(turno):
            messagebox.showinfo("Ganador", f"¡Jugador {turno} ha ganado!")
            reiniciar_juego()
        elif all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("Empate", "¡Es un empate!")
            reiniciar_juego()
        turno = "O" if turno == "X" else "X"
        guardar_tablero()
        
def verificar_ganador(jugador):
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)):
            return True
        if all(tablero[j][i] == jugador for j in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def guardar_tablero():
    with open("checkpoint.txt", "wb") as f:
        pickle.dump(tablero, f)

def cargar_tablero():
    try:
        with open("checkpoint.txt", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return [[" " for _ in range(3)] for _ in range(3)]

def reiniciar_juego():
    global tablero, turno
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "X"
    guardar_tablero()
    imprimir_tablero()

def juego_nuevo():
    global tablero, turno
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "X"
    guardar_tablero()
    imprimir_tablero()

def continuar_juego():
    global tablero, turno
    tablero = cargar_tablero()
    imprimir_tablero()

tablero = cargar_tablero()
turno = "X"

root = tk.Tk()
root.title("Juego de Gato")

frame = tk.Frame(root)
frame.pack()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nuevo Juego", command=juego_nuevo)
file_menu.add_command(label="Continuar Juego", command=continuar_juego)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

imprimir_tablero()

root.mainloop() 