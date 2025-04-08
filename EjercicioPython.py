tareas = []

def mostrar_menu():
    print("--- Menú ---")
    print("1. Agregar una tarea")
    print("2. Ver lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar una tarea")
    print("5. Salir")

def agregar_tarea():
    titulo = input("Introduce el título de la tarea: ")
    if titulo:
        tareas.append({"titulo": titulo, "completada": False})
        print("Tarea agregada")
    else:
        print("El título no puede estar vacío")

def ver_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("--- Lista de Tareas ---")
          
        for tarea in tareas:
            i = 1
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(str(i) + ". " + tarea['titulo'] + " - " + estado)
            i += 1
def marcar_completada():
    ver_tareas()
    if tareas:
        numero = int(input("Introduce el número de la tarea a marcar como completada: "))
        tareas[numero - 1]["completada"] = True
        print("Tarea marcada como completada")
    else:
        print("Número no válido, selecciona una tarea existente")

def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar")
    else:
        print("--- Selecciona la tarea a eliminar ---")
        i = 1
        for tarea in tareas:
            print(str(i) + ". " + tarea['titulo'])
            i += 1
        numero = int(input("Número de la tarea a eliminar: "))
        tarea_eliminada = tareas[numero - 1]
        tareas.remove(tarea_eliminada)
        print("Tarea " + tarea_eliminada['titulo'] + " eliminada")



while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción del menú.")
