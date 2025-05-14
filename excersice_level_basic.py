# 1. Saludo personalizado
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

# 2. Suma de dos números
def sumar(a, b):
    return a + b

# 3. Número par o impar
def es_par(numero):
    return "Par" if numero % 2 == 0 else "Impar"

# 4. Mayoría de edad
def es_mayor_de_edad(edad):
    return "Mayor de edad" if edad >= 18 else "Menor de edad"

# 5. Conversor de temperatura
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# 6. Área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# 7. Mayor de una lista
def mayor_lista(lista):
    return max(lista)

# 8. Contar letras
def contar_letra(palabra, letra):
    return palabra.lower().count(letra.lower())
