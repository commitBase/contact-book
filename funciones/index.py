def saludo():
    print("Hola")

saludo()



def calculo(a,b):
    c = int(a) + int(b)
    print(c)

calculo(2,4)


# Funciones Scope -> accede a variables externas
num = 5
resultado = 0
def suma(x,y,z):
    resultado = x + y + z
    print(num)
    return resultado

resultado = suma(2,4,5)
print(resultado)