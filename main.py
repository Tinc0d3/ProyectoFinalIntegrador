# from colorama import init, Fore, Back, Style

# init()

# Importamos funciones
# from funciones_menu import *  # Importa todas las fx del archivo funciones_menu.py
from funciones_DB import (
    db_crear_tabla_productos,
    db_crear_tabla_usuarios,
)  # Importa la fx db_crear_tabla_productos del archivo funciones_DB.py


import sqlite3

from funciones_menu import *

from funciones_DB import (
    db_login,
    #     menu_mostrar_productos,
    db_agregar_producto,
    #     menu_modificar_producto,
    #     menu_eliminar_producto,
    #     menu_buscar_producto_por_id,
    #     menu_bajo_stock,
    #     db_agregar_usuario,
    #     db_modificar_usuario,
    #     db_eliminar_usuario,
)


# Declaramos la función principal main
def main():
    # Inicializamos la BD y creamos la tabla (si no existe)
    db_crear_tabla_productos()
    db_crear_tabla_usuarios()

    usuario_logueado = db_login()
    if not usuario_logueado:
        return  # Salir si no se loguea correctamente

    # Mostrar título de bienvenida
    print(Fore.RED + "\n" + "*" * 50 + Style.RESET_ALL)
    print(
        Fore.WHITE + f"¡Bienvenido, {usuario_logueado[1]}!".center(50) + Style.RESET_ALL
    )
    print(Fore.WHITE + "Sistema de Gestión de Productos".center(50) + Style.RESET_ALL)
    print(Fore.RED + "*" * 50 + "\n" + Style.RESET_ALL)

    # Menú principal según el rol
    while True:
        if usuario_logueado[3] == "administrador":
            menu_mostrar_menu_admin()
        else:
            menu_mostrar_menu()

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_agregar_producto()
        elif opcion == "2":
            db_mostrar_productos()
        elif opcion == "3":
            db_modificar_producto()
        elif opcion == "4":
            db_eliminar_producto()
        elif opcion == "5":
            menu_buscar_producto()
        elif opcion == "6":
            db_bajo_stock()
        elif opcion == "7":
            db_agregar_usuario()
        elif opcion == "8":
            db_modificar_usuario()
        elif opcion == "9":
            db_eliminar_usuario()
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
        input("\nPresione Enter para continuar...")


# *********************************
# INVOCAMOS A LA FUNCIÓN PRINCIPAL
# *********************************
main()
