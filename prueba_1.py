def menu():
    lista_alumnos = []
    while True:
        try:
            eleccion = int(input("\n1) Agregar alumnos a la lista. \n2) Mostrar todos los alumnos.\n3) Eliminar alumno. \n4) Salir.\nElige una opcion: "))
            if eleccion == 1:
                alumno = input("Ingrese el nombre del alumno: ").lower()
                lista_alumnos.append(alumno)
            elif eleccion == 2:
                print (f"Los nombres en la lista son: {lista_alumnos}")
            elif eleccion ==3:
                alumno_eliminado = input("Escribe el nombre del alumno a eliminar: ").lower()
                if alumno_eliminado.isalpha():
                    for i in lista_alumnos:
                        if i == alumno_eliminado:
                            lista_alumnos.remove(alumno_eliminado)
                            print(f"Eliminando a {alumno_eliminado} de la lista.")
                        else:
                            print(f"No hay un alumno llamado {alumno_eliminado} en la lista.")
                else:
                    print("El nombre solo puede estar en letras.")
            elif eleccion == 4:
                print ("Adiós.")
                break
            else:
                print ("El número ingresado no estáen la lista de opciones.")
        except:
            print ("Solo puedes ingresar números.")
menu()