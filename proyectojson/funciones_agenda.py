# Variables
contactos = {}
flag = True

def menu():
    while flag != False:
        print("\nAGENDA VIRTUAL")
        print("1. Agregar contactos")
        print("2. Ver contactos")
        print("3. Buscar contactos")
        print("4. Eliminar contactos")
        print("5. Salir")

        select = input("Seleccione opcion 1-5.\n")

        if select == "1":
            agregar()
        elif select == "2":
            ver()
        elif select == "3":
            find()

def agregar():
    print("\nUsted ha seleccionado agregar usuario: \n")
    name = input("Nombre: ")
    number = int(input("Teléfono: "))
    email = input("Email: ")

    contactos[name] = {"Teléfono": number, "Email": email} # Crea una llave {name} que a su vez tiene {number,email}
    # Por lo tanto: { 'name':    {Teléfono : number, Email : email }} 
    print(contactos)

def ver():
    print("\nTus contactos son: \n")
    try:
        for i, (nombre,datos) in enumerate(contactos.items(), start=1):
            # Básicamente se enumera cada item dentro del diccionario contactos mediante contacto.items(), es decir:
            # La key original (name), y los datos (email, teléfono), lo anterior lo deglosa del diccionario y se almacena en variables nombre, datos: (key, value).
            # Para acceder a la key, que en este caso es el nombre, basta con colocar {nombre}
            # Para acceder a los datos se debe {datos} y además especificar que valor quiero, en este caso se incluye ente [] la key: {datos['Teléfono']}
            # Este método se llama Iteración sobre pares Llave-Valor
            print(f"{i}. Nombre: {nombre}")
            print(f"Number: {datos['Teléfono']}")
            print(f"Email: {datos['Email']}")
    except NameError:
        print("No cuentas con contactos creados")

def find():
    print("\nIngresa el nombre para buscar: \n")
    try:
        nameInput = input()
        print(f"Tu contacto {nameInput} lo guardaste como: \n{contactos[nameInput]}")
    except NameError:
        print("La persona no existe en los datos guardados")