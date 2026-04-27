import json

numeros = [1,2,3,4,5,6]
# Meter información
with open("lista.json", "w") as f: # w de escribir en inglés
    json.dump(numeros, f)

# Leer información de JSON
with open("lista.json") as f: # ahora esta en read-mode
    print(json.load(f))

# Mezcla del trabajo:

archivo = "hola.json"
try:
    with open(archivo) as f:
        a = json.load(f)
except FileNotFoundError:
    texto = "Hola"
    with open(archivo, "w") as f: # Modo escritura
        json.dump(texto, f)
else: 
    print(a)