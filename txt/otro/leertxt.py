with open("saludo.txt") as file_object: # Busca el archivo en la misma carpeta
    leer = file_object.read()
    print(leer)    

# buscador en otra carpeta
# File path
with open("otro/hola.txt") as file_object: # Busca el archivo en la misma carpeta
    leer = file_object.read()
    print(leer)  

# absolute: busca el objetivo de forma específica, se usa cuando file path no sirve
absolute = "/Users/marce/OneDrive/Desktop/ProyectosPy/jsonpractice"
with open("saludo.txt") as file_object: 
    leer = file_object.read()
    print(leer)    

# Leer como lista
with open("saludo.txt") as file_object: 
    leer = file_object.readlines()
    print(leer)    