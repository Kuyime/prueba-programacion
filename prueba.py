def menu():
    lista_alumnos = []
    while True:
        try:
            eleccion = int(input("\n1) Agregar alumnos a la lista. \n2) Mostrar todos los alumnos. \n3) Salir.\nElige una opcion: "))
            if eleccion == 1:
                alumno = input("Ingrese el nombre del alumno: ").lower()
                if alumno.isalpha():
                    lista_alumnos.append(alumno)
                else:
                    print ("El nombre debe ser ingresado solo con letras.")
            elif eleccion == 2:
                print (f"Los nombres en la lista son: {lista_alumnos}")
            elif eleccion == 3:
                print ("Adiós.")
                break
        except:
            print ("Solo puedes ingresar números.")
menu()