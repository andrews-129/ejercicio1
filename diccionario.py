
#Escriba una función en python que pida un número entero positivo y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

n = int(input("Ingrese un número entero positivo: "))
diccionario = {i: i**2 for i in range(1, n + 1)}
print("Diccionario creado:", diccionario)


#Escribe una función que reciba como parámetro una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena

def contar_caracteres(cadena):
    diccionario = {}
    for caracter in cadena:
        diccionario[caracter] = diccionario.get(caracter, 0) + 1
    return diccionario

texto = input("Ingresa una cadena de texto: ")
resultado = contar_caracteres(texto)
print("Diccionario creado:", resultado)

#Crear un programa en python donde se va a declarar un diccionario para guardar los precios de distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

frutas = {
    "manzana" : 2500,
    "pera" : 1500,
    "naranja": 2800,
    "fresa": 5000,
    "guineo" : 500
}
fruta = input("ingresa el nombre de la fruta: ").lower()
if fruta in frutas:
    try:
        cantidad = int(input("ingresa la cantidad vendida: "))
        precio = frutas[fruta] * cantidad
        print(f"el precio final de la fruta {fruta} es: ${precio}")
    except ValueError:
        print("Error: la cantidad debe ser un numero")
else:
    print("error: la fruta no existe en el registro, se acabaron rey :(")
 






    


