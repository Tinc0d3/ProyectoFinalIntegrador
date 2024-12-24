# 1. Importamos el módulo sqlite3 para manejar la BD
import sqlite3


# DECLARACIÓN DE CONSTANTES
ruta_BD = r"D:\- {Programación}\- Mis cursos\Talento Tech_Python inicial\ProyectoFinal\Final\inventario.db"
# Otra alternativa: sin la 'r' pero todo con '\\' en la ruta)

"""
db_crear_tabla_productos()

Esta fx utiliza sqlite3 para crear/conectarse con la BD "inventario.db" y crea la tabla productos
"""


def db_crear_tabla_productos():
    try:  # El bloque try sirve para validar
        conexion = sqlite3.connect(ruta_BD)
        cursor = conexion.cursor()  # Crear un cursor/puntero p/interacturar con la BD
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT, 
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
            )

            """
        )
        conexion.commit()
    except sqlite3.Error as e:  # bloque try
        print(f"Error al crear la tabla: {e}")
    finally:  # bloque try
        conexion.close()


def db_crear_tabla_usuarios():
    conexion = sqlite3.connect(ruta_BD)
    cursor = conexion.cursor()  # Crear un cursor/puntero para interacturar con la base
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL, 
        rol TEXT NOT NULL 
        )

        """
    )
    conexion.commit()
    conexion.close()


def db_crear_tabla_usuarios():
    conexion = sqlite3.connect(ruta_BD)
    cursor = conexion.cursor()  # Crear un cursor/puntero para interacturar con la base
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL, 
        rol TEXT NOT NULL 
        )

        """
    )
    conexion.commit()
    conexion.close()


# Función de login
def db_login():
    for i in range(3):
        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa la contraseña: ")

        # Consulta para verificar credenciales
        conexion = sqlite3.connect(ruta_BD)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE username = ? AND password = ?",
            (username, password),
        )
        usuario = cursor.fetchone()

        if usuario:
            print(f"¡Bienvenido, {username}!")
            return usuario  # Retorna el usuario como una tupla
        else:
            print("¡USUARIO NO AUTORIZADO!")
    print("Lo siento, superaste el número de intentos.")
    return None


# GESTIÓN DE USUARIOS


# Agregar usuario
def db_agregar_usuario(cursor, conexion):
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    cursor.execute(
        "INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password)
    )
    conexion.commit()
    print("¡Usuario agregado correctamente!")


# Modificar usuario
def db_modificar_usuario(cursor, conexion):
    user_id = int(input("Ingrese el ID del usuario que desea modificar: "))
    new_username = input("Ingrese el nuevo nombre de usuario: ")
    new_password = input("Ingrese la nueva contraseña: ")

    cursor.execute(
        "UPDATE usuarios SET username = ?, password = ? WHERE id_usuario = ?",
        (new_username, new_password, user_id),
    )
    if cursor.rowcount > 0:
        conexion.commit()
        print("¡Usuario modificado correctamente!")
    else:
        print("No se encontró el usuario con el ID especificado.")


# Eliminar usuario
def db_eliminar_usuario(cursor, conexion):
    user_id = int(input("Ingrese el ID del usuario que desea eliminar: "))

    cursor.execute("DELETE FROM usuarios WHERE id_usuario = ?", (user_id,))
    if cursor.rowcount > 0:
        conexion.commit()
        print("¡Usuario eliminado correctamente!")
    else:
        print("No se encontró el usuario con el ID especificado.")


""" db_agregar_producto(producto)
1. Recibe como argumento un diccionario con las clave/valor de cada campo de la tabla
2. Inserta los datos en la tabla productos
"""


def db_agregar_producto(producto):
    try:
        conexion = sqlite3.connect(ruta_BD)  # Nos conectamos a la BD
        cursor = (
            conexion.cursor()
        )  # Creamos un cursor/puntero para interactuar con la BD

        # Creamos una variable para la consulta
        query = "INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria) VALUES (?, ?, ?, ?, ?)"

        # Y esta variable serían los valores
        placeholder = (
            producto["nombre"],  # Este coincide con el primero de los ?, y así c/u
            producto["descripcion"],
            producto["precio"],
            producto["cantidad"],
            producto["categoria"],
        )

        cursor.execute(query, placeholder)
        conexion.commit()  # Concretamos el INSERT
        state = True
    except Exception as error:
        print(f"Error: {error}")
        conexion.close()  # Cerramos la conexión de la BD
        state = False
    finally:
        conexion.close()
        return state


""" db_mostrar_productos()
1. Lee todos los datos de la tabla productos
2. Retorna una lista de tuplas con los datos de la tabla
"""


def db_mostrar_productos():
    try:
        conexion = sqlite3.connect(ruta_BD)
        cursor = conexion.cursor()
        query = "SELECT * FROM productos;"
        cursor.execute(query)
        lista_productos = cursor.fetchall()  # Retorna una lista de tuplas
        # cursor.fetchone() retorna solo una tupla
        conexion.close()
        return lista_productos
    except sqlite3.Error as e:
        print(f"Error al obtener productos: {e}")
        return []
    finally:
        conexion.close()


""" db_buscar_producto_por_id(id)
1. Busco y retorno el registro según el id
2. Retorno una tupla con el resultado
"""


def db_buscar_producto_por_id(id):
    try:
        conexion = sqlite3.connect(ruta_BD)
        cursor = conexion.cursor()
        query = "SELECT * FROM productos WHERE id_producto = ?;"
        placeholders = (id,)
        cursor.execute(query, placeholders)
        producto = cursor.fetchone()  # Retorna una tupla o None
        return producto
    except sqlite3.Error as e:
        print(f"Error al buscar producto: {e}")
        return None
    finally:
        conexion.close()


"""
db_modificar_producto(id, nueva_cantidad)
Actualiza la cantidad del producto según el id
"""


def db_modificar_producto(id, producto):
    try:
        conexion = sqlite3.connect(ruta_BD)
        cursor = conexion.cursor()
        query = """UPDATE productos SET 
        nombre = ?, 
        descripción = ?, 
        precio = ?, 
        cantidad = ?, 
        categoria = ?
        WHERE id = ?;
        """
        placeholder = (
            producto["nombre"],
            producto["descripcion"],
            producto["precio"],
            producto["cantidad"],
            producto["categoria"],
        )

        cursor.execute(query, placeholder)
        conexion.commit()
        print("¡Producto actualizado correctamente!")
    except sqlite3.Error as e:
        print(f"Error al actualizar producto: {e}")
    finally:
        conexion.close()


"""
db_eliminar_producto(id)
Eliminar de la tabla el producto con el id que recibo como argumento
"""


def db_eliminar_producto(id):
    try:
        conexion = sqlite3.connect(ruta_BD)
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = ?;"
        placeholders = (id,)
        cursor.execute(query, placeholders)
        conexion.commit()
        print("¡Producto eliminado correctamente!")
    except sqlite3.Error as e:
        print(f"Error al eliminar producto: {e}")
    finally:
        conexion.close()


"""
db_get_productos_by_condicion(minimo_stock)

1. retornar una lista_producto con aquellos registros cuya cantidad < minimo_stock
"""


def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect(ruta_BD)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = (minimo_stock,)
    cursor.execute(query, placeholders)
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos


# Reporte bajo stock
def db_reporte_bajo_stock():
    try:
        limite = int(
            input("Ingresa el límite de cantidad para el reporte de bajo stock: ")
        )
        productos = db_mostrar_productos()
        bajo_stock = [producto for producto in productos if producto[4] <= limite]

        if not bajo_stock:
            print("No hay productos con bajo stock.")
        else:
            print("Productos con bajo stock:")
            print(
                "---------------------------------------------------------------------------"
            )
            print("| ID   | Producto   | Cantidad |")
            print(
                "---------------------------------------------------------------------------"
            )
            for producto in bajo_stock:
                print(f"| {producto[0]:5} | {producto[1]:10} | {producto[4]:8} |")
    except ValueError:
        print("Por favor, ingresa un número válido para el límite.")


# Esto nos permite transformar la tupla en un diccionario
# conexion.row_factory = sqlite3.Row
# for registro_obj in resultados:
#    registro = dict(registro_obj)
#    for key, value in registro.items():
#        print(f"{key}  :   {value}")
