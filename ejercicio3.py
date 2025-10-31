#Integrantes: Julio Ahumada - Andrews Rivera - Jhon Alvarez - Galenis wilches

#rea una lista llamada frutas con los elementos: "manzana", "banano", "pera", "uva", "naranja". Muestra el primer y el último elemento. Agrega la fruta "mango" al final.Elimina "pera" de la lista. Imprime la lista final.

frutas = ["manzana", "banano", "pera", "uva", "naranja"]
 
print("Primer elemento:", frutas[0])
print("Último elemento:", frutas[-1])
 
frutas.append("mango")
 
frutas.remove("pera")
 
print("Lista final:", frutas)

#Crea una lista llamada numeros con los números del 1 al 10. Muestra la suma total de los elementos. Muestra el número más grande y el más pequeño. Calcula el promedio de la lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_total = sum(numeros)
print("La suma total de los elementos es:", suma_total)

mayor = max(numeros)
print("El número más grande es:", mayor)

menor = min(numeros)
print("El número más pequeño es:", menor)

promedio = sum(numeros) / len(numeros)
print("El promedio de la lista es:", promedio)

#Dada la lista nombres = ["Ana", "Luis", "Sofía", "Pedro", "Carla"]: Usa un ciclo for para imprimir cada nombre en una línea. Usa un ciclo for para mostrar solo los nombres con más de 4 letras.

nmbres = ["Ana", "Luis", "Sofía", "Pedro", "Carla"]
for nombre in nmbres:
    print(nombre)

for nombre in nmbres:
    if len(nombre) > 4:
        print(nombre)

#Dada la lista edades = [12, 17, 18, 20, 15, 22, 13]: Crea una nueva lista llamada mayores que contenga solo las edades mayores o iguales a 18. Imprime la cantidad de personas mayores de edad y muestra la lista resultante.

edades = [12, 17, 18, 20, 15, 22, 13]
mayores = [edad for edad in edades if edad >= 18]
print("Cantidad de personas mayores de edad:", len(mayores))
print("Lista de personas mayores de edad:", mayores)

#Crea una lista con 5 notas de estudiantes. Calcula el promedio. Indica si el promedio es aprobado (≥3.0) o reprobado (<3.0). Muestra las notas ordenadas de menor a mayor.

notas = [3.5, 2.8, 4.0, 3.2, 2.5]
 
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio:.2f}")
 
if promedio >= 3.0:
    print("El promedio es aprobado.")
else:
    print("El promedio es reprobado.")
 
notas_ordenadas = sorted(notas)
print("Las notas ordenadas de menor a mayor son:", notas_ordenadas)

#Diseña un programa que: Permita al usuario ingresar los nombres de 5 productos y sus precios (en dos listas). Calcule el precio total de todos los productos. muestre el nombre del producto más caro y el más barato.

productos = []
precios = []
 
for i in range(5):
    nom = input(f"ingresa el nombre del producto #{i+1}: ")
    precio = float(input(f"ingrese el precio del producto {nom}:"))
    productos.append(nom)
    precios.append(precio)
   
total = sum(precios)
 
pro_caro = precios.index(max(precios))
pro_barato = precios.index(min(precios))
 
 
print(f"precio total ${total:.2f}")
print(f"Producto mas caro: {productos[pro_caro]} (${precios[pro_caro]:.2f})")
print(f"Producto mas barato: {productos[pro_barato]} (${precios[pro_barato]:.2f})")
 
