# 9. Filtrar pares
def filtrar_pares(lista):
    return [n for n in lista if n % 2 == 0]

# 10. Palíndromo
def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

# 11. Factorial
def factorial(n):
    if n < 0:
        return "Número no válido"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# 12. Eliminar duplicados
def eliminar_duplicados(lista):
    return list(set(lista))

# 13. FizzBuzz
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    return str(numero)

# 14. Contar vocales
def contar_vocales(texto):
    return sum(1 for c in texto.lower() if c in 'aeiou')

# 15. Invertir texto
def invertir_texto(texto):
    return texto[::-1]
