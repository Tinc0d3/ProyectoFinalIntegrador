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
    db_agregar_producto,
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
            menu_mostrar_productos()
        elif opcion == "3":
            menu_modificar_producto_no_admin()
        elif opcion == "4":
            menu_eliminar_producto()
        elif opcion == "5":
            menu_buscar_producto()
        elif opcion == "6":
            menu_reporte_bajo_stock()
        elif opcion == "7":
            menu_agregar_usuario()
        elif opcion == "8":
            db_modificar_usuario()
        elif opcion == "9":
            db_eliminar_usuario()
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

        continuar = input(
            "\nIngrese 's' para salir o cualquier tecla para conitnuar: "
        ).lower()  # pausa para que el usuario pueda ver
        if continuar == "s":
            print("\nGracias por usar nuestra App")
            break


# *********************************
# INVOCAMOS A LA FUNCIÓN PRINCIPAL
# *********************************
main()
