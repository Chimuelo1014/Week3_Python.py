###### Añadir productos:
# Cada producto debe estar definido por su nombre, precio y cantidad disponible
# Esta isnformación será almacenada de modo que el inventario pueda crecer dinámicamente
##### Consultar productos:
# Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
# Si el producto no está en el inventario, se debe notificar adecuadamente
###### Actualizar precios:
# El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario
####### Eliminar productos:
# El programa debe permitir al usuario eliminar productos del inventario de manera segura
####### Calcular el valor total del inventario:
# El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
# Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.

def add_products(inventary,name,price,amount): 
    if name in inventary : 
        print("El producto ya se encuentra en el inventario")
    else :
        inventary[name] = (price,amount)
        print("el producto se añadio al inventario")

def counsult_products(inventary,name):
    values = inventary.get(name)
    if name in inventary :
        print(f"Nombre: {name} | Precio: {values[0]} | Cantidad: {values[1]}")
    else :
        print("Producto no encontrado.")

def update_prices(inventary,name,new_price):
    if name in inventary:
        amount = inventary[name][1]
        inventary[name] = (new_price,amount)
    else :
        print("El procutos no se encuentra en el inventario")

def delete_product(inventary,name):
    if name in inventary:
        del inventary[name]
        print("El producto fue eliminado con exito")
    else :
        print("El producto no se encuentra en el inventario")

def total_inventary(inventary): 

    calculate = lambda i: i[0] * i[1]  # precio * cantidad
    total = sum(calculate(producto) for producto in inventary.values())
    print(f"Valor total del inventario: ${total:.2f}")


def conv_float(mensaje):
    
    entrada = input(mensaje)
    if entrada.isnumeric():
        value = float(entrada)
        return value
    else: 
            print("Por favor, ingresa un precio válido.")
            conv_float(mensaje)

            return None



# def conv_float(mensaje):
    
    

#     entrada     = input(mensaje)
#     if entrada.replace('.', ',', 1).isdigit():
    
#         return float(entrada)
    

       
#     else: 
#             print("Por favor, ingresa un número válido.")
#             conv_float(mensaje)

#             return None

def conv_int(mensaje):
    entrada = input(mensaje)
    if entrada.isdigit():
        return int(entrada)
    else:
        print("Por favor, ingresa una cantidad valida.")
        conv_int(mensaje)
        return None
    

def mostrar_menu():
    print("\n--- Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")
    return input("Seleccione una opción: ")






inventary = {}

while True:
    opcion = mostrar_menu()
    if opcion == "1":
        name = input("Nombre del producto: ").strip().lower()       
        price = conv_float("Precio: ")
        amount = conv_int("Cantidad: ")
        if price is not None and amount is not None:
            add_products(inventary, name, price, amount)
    elif opcion == "2":
        name = input("Nombre del producto a buscar: ").strip()
        counsult_products(inventary, name)
    elif opcion == "3":
        name = input("Nombre del producto a actualizar: ").strip()
        new_price = conv_float("Nuevo precio: ")
        if new_price is not None:
            update_prices(inventary, name, new_price)
    elif opcion == "4":
        name = input("Nombre del producto a eliminar: ").strip()
        delete_product(inventary, name)
    elif opcion == "5":
        total_inventary(inventary)
    elif opcion == "6":
        print("¡Gracias por usar el sistema de inventario!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

        