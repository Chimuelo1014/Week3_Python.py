import random
import string

# 16. Validar contraseña segura
def validar_contrasena(contra):
    tiene_mayus = any(c.isupper() for c in contra)
    tiene_minus = any(c.islower() for c in contra)
    tiene_num = any(c.isdigit() for c in contra)
    tiene_simbolo = any(c in string.punctuation for c in contra)
    return tiene_mayus and tiene_minus and tiene_num and tiene_simbolo

# 17. Simular dado
def lanzar_dado():
    return random.randint(1, 6)

# 18. Suma de elementos únicos
def suma_unicos(lista):
    return sum(n for n in set(lista))

# 19. Generador de contraseñas
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# 20. Composición de funciones
def aplicar_composicion(f1, f2, valor):
    return f1(f2(valor))
