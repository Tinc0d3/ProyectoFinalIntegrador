# Instalamos el módulo colorama
# pip install colorama

from funciones_DB import *

# Importamos init y otros médotos de colorama
from colorama import init, Fore, Back, Style

# Inicializamos colorama ya que prepara el entorno
# para usar colores y estilos en la consola
init()

# Para que el estilo no se propague
init(autoreset=True)


"""
*** TUTO COLORAMA ***

# Para cambiar el color del texto
print(Fore.RED + "Este texto es rojo")
print(Fore.GREEN + "Este texto es verde")

# Para cambiar el color del fondo
print(Back.YELLOW + "Aviso: el stock de este producto es muy bajo")

# Para cambiar el estilo del texto
print(Style.BRIGHT + Fore.BLUE + "Bienvenido a la gestión de inventario")
print(Style.DIM + "Nota: ASEGÚRATE DE INGRESAR UN ID válido")
print(
    Back.YELLOW
    + Fore.RED
    + Style.BRIGHT
    + "Alerta: el stock de este producto es crítico. Se recomienda reponer."
)
"""


# Mostrar menú (estandar)
def menu_mostrar_menu():
    print(Back.RED + Fore.WHITE + Style.BRIGHT + " MENÚ PRINCIPAL " + Style.RESET_ALL)
    print("1  --> Agregar productos")
    print("2  --> Mostrar productos")
    print("3  --> Actualizar cantidad de producto")
    print("4  --> Eliminar producto")
    print("5  --> Buscar producto")
    print("6  --> Reporte bajo stock")
    print("7  --> Salir")
    opcion = input("Seleccione una opción: ")


"""
menu_mostrar_menu_admin()
1. Muestra en consola las opciones disponibles
2. Captura y retorna la opcion seleccionada
3. Respecto al menú común, tiene el agregado de la gestión de usuarios
"""


# Mostrar menú  (administrador)
def menu_mostrar_menu_admin():
    print(Back.RED + Fore.WHITE + Style.BRIGHT + " MENÚ PRINCIPAL " + Style.RESET_ALL)
    print("1  --> Agregar productos")
    print("2  --> Mostrar productos")
    print("3  --> Actualizar cantidad de producto")
    print("4  --> Eliminar producto")
    print("5  --> Buscar producto")
    print("6  --> Reporte bajo stock")
    print("7  --> Agregar usuario")
    print("8  --> Modificar usuario")
    print("9  --> Eliminar usuario")
    print("10 --> Salir")

    # opcion = input("Seleccione una opción: ")
    # return opcion


"""
menu_agregar_producto()
1. captura todos los datos
2. valida los datos y los almacena en un diccionario
3. llama a db_agregar_producto(producto) y le pasa el diccionario producto para que lo inserte en la base de datos
"""


def menu_agregar_producto():
    print("\nIngrese los siguientes datos del producto:")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

    # Validar valores y tipos de datos
    # (Nos aseguramos que: primero que no quede vacío los input
    # y luego que coincida el tipo de dato con la tabla de la BD)

    # Creamos un diccionario temporal
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    # PERSISTIR LOS DATOS EN LA TABLA PRODUCTOS
    # Llamamos a la función de agregar un producto y
    # y recibe como argumento el diccionario temporal 'productos'
    db_agregar_producto(producto)
    print("¡Producto agregado correctamente!")


"""
menu_mostrar_productos()
1. no recibe ningún argumento
2. llama a db_get_productos() que retorna una lista de tuplas con el contenido de la tabla
3. usamos un bucle for para mostrar en consola
"""


def menu_mostrar_productos():
    lista_productos = db_mostrar_productos()

    if not lista_productos:
        print("No hay productos que mostrar")


"""
menu_buscar_producto()
1. Solicita al usuario que ingrese el id del producto a buscar
2. Llamar a db_buscar_producto_por_id(id) 
"""


def menu_buscar_producto():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_buscar_producto_por_id(
        id
    )  # en get_producto almacenas lo que retorna
    if not get_producto:  # si está vacío, imprime el Error de abajo
        print("ERROR: no se ha encontrado ningún producton con el id {id}")
    else:  # y si va por el negativo (o sea que sí encontró, ahí lo imprimis)
        print(get_producto)


"""
menu_modificar_producto()
1. Solicita al usuario que ingrese el id del producto a modificar
2. Buscamos el producto en la tabla (si no existe informamos)
3. Mostramos cantidad actual y pedimos que ingrese la nueva cantidad
4. Llamar a db_modificar_producto(id, producto)

"""


def menu_modificar_producto_no_admin():
    id = int(input("\nIngrese el id del producto a actualizar: "))
    get_producto = db_buscar_producto_por_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        nueva_cantidad = int(
            input(f"Cantidad actual {get_producto[4]} - Nueva cantidad: ")
        )
        db_actualizar_producto_no_admin(id, nueva_cantidad)
        print("Registro actualizado exitosamente!")


"""
menu_eliminar_producto()
1. solicita al usuario que ingrese el id del producto a eliminar
2. buscamos el producto en la tabla (si no existe informamos)
3. mostramos el producto y solicitamos confirmación
4. llamar a db_eliminar_producto(id)
"""


def menu_eliminar_producto():
    id = int(input("\nIngrese el id del producto a eliminar: "))
    get_producto = db_buscar_producto_por_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        # Encabezados de la tabla
        encabezados = ["ID", "Nombre", "Descripción", "Categoría", "Cantidad", "Precio"]

        print("\nATENCION: se eliminará el siguiente registro:")
        print(get_producto)
        confirmacion = input(
            "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            db_eliminar_producto(id)
            print("Registro eliminado exitosamente!")
        else:
            print("Operación cancelada.")


"""
menu_reporte_bajo_stock()
1. Solicita al usuario que ingrese la cantidad mínima para el reporte
2. Llamar a db_productos_por_condicion(condicion) que retorna una lista_productos 
"""


def menu_reporte_bajo_stock():
    minimo_stock = int(input("\nIngrese el unmbral de mínimo stock:"))
    lista_productos = db_mostrar_productos_by_condicion(minimo_stock)
    if not lista_productos:
        print("No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(producto)


"""
menu_agregar_usuario()
1. Captura todos los datos
2. Valida los datos y los almacena en un diccionario
3. Llama a ddb_agregar_usuario(cursor, conexion) y le pasa el diccionario usuario para que lo inserte en la base de datos
"""


def menu_agregar_usuario():
    print("\nIngrese los siguientes datos del usuario:")
    username = input("Username: ")
    password = input("Password: ")
    rol = input("Rol: ")

    # Validar valores y tipos de datos
    # (Nos aseguramos que: primero que no quede vacío los input
    # y luego que coincida el tipo de dato con la tabla de la BD)

    # Creamos un diccionario temporal
    usuario = {
        "username": username,
        "password": password,
        "rol": rol,
    }
    # PERSISTIR LOS DATOS EN LA TABLA USUARIOS
    # Llamamos a la función de agregar un usuario y
    # y recibe como argumento el diccionario temporal 'usuario'
    db_agregar_usuario()


def db_modificar_usuario(cursor, conexion):
    id = int(input("\nIngrese el id del usuario a modificar"))
    get_usuario = db_buscar_usuario_por_id(id)
    if not get_usuario:
        print("ERROR: no se ha encontrado ningún usuario con el id {id}")
    else:
        nueva_cantidad = int(
            input(f"Cantidad actual {get_usuario[4]} - Nueva cantidad: ")
        )
        db_actualizar_producto_no_admin(id, nueva_cantidad)
        print("Registro actualizado exitosamente!")
