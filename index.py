# 4Geeks intro to python.  
# comparison against JS

print("hello world")
nombre = "Max" # string
age = 35 # integer
average = 9.5 #float
booleans = True # booleans
frutas = ["Apple", "Organge"] #list
persona = { #dictionary 
    "nombre": "Diego"
    } 
nombre.upper

if age % 2 == 0: 
    print ('el numero es par')
else: 
    print ('el numero no es par')

#ejercicio_1
niño1 = True
niño2 = True
if niño1 and niño2 == True: 
    print ('pueden salir a jugar')
else:
    print ('castigados')

# ejercicio_2
hay_coca = True
hay_fanta = False
if hay_coca == True:
    print ('traje coca amá')


nombres = ["Diego", "Franco"]
# for 
for nombre in nombres: 
    print(nombre)
for numero in range(10, 14):
    print(numero)

suma = 0
for num in range(1, 6):
    suma += num 

print("la suma de los primeros 5 números naturales es:", suma) 

# while
numero = 1

while numero <= 5:
    print(numero)
    numero +=1 

# funciones
def suma(n1, n2):
    return n1 + n2 
print (suma(1, 2))

# while rerun
numero = 1

while numero <= 5:
    print(numero)
    numero +=1 
