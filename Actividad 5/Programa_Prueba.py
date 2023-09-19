import os
import threading
import multiprocessing
import time

# Función para escribir en un archivo de texto
def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

# Función para crear un archivo de texto en un hilo
def create_file_thread(file_num):
    filename = f'file{file_num}.txt'
    text = f'Este es el archivo {file_num}\n'
    write_to_file(filename, text)

# Función para crear un archivo de texto en un proceso
def create_file_process(file_num):
    filename = f'file{file_num}.txt'
    text = f'Este es el archivo {file_num}\n'
    write_to_file(filename, text)

if __name__ == "__main__":
    # Usar hilos para crear archivos de texto
    threads = []
    for i in range(1, 5):
        thread = threading.Thread(target=create_file_thread, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Archivos de texto creados en hilos")

    # Usar procesos para crear archivos de texto
    processes = []
    for i in range(1, 5):
        process = multiprocessing.Process(target=create_file_process, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Archivos de texto creados en procesos")

    # Crea un demonio para esperar un tiempo antes de que el programa termine
    def daemon_function():
        time.sleep(5)
        print("El demonio ha terminado")

    daemon_thread = threading.Thread(target=daemon_function, daemon=True)
    daemon_thread.start()

    # El programa principal continúa mientras el demonio se ejecuta en segundo plano
    while daemon_thread.is_alive():
        pass

    print("Programa principal ha terminado")
