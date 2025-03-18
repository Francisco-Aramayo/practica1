import sys
import os


def agregar_producto(lista):
    limpiar_pantalla()
    nombre = input('Ingrese nombre: ')
    cantidad = int(input('Ingrese cantidad: '))
    for producto in lista:
        if producto['Nombre'].lower() == nombre.lower():
            producto['Cantidad'] += cantidad
            print('Se actualizo la cantidad del producto')
            return

    lista.append({'Nombre': nombre, 'Cantidad': cantidad})
    print('Producto agregado correctamente\n')


def eliminar_producto(lista):
    limpiar_pantalla()
    nombre = input('Ingrese el nombre del producto a eliminar: ')
    for producto in lista:
        if producto['Nombre'] == nombre:
            lista.remove(producto)
            print('Producto eliminado correctamente\n')
            return
    print('El producto no existe en el inventario\n')


def mostrar_inventario(lista):
    limpiar_pantalla()
    if not lista:
        print('El inventario esta vacio\n')
        return
    print('Inventario actual: ')
    for i, producto in enumerate(lista, 1):
        print(f'[{i}]. {producto['Nombre']} - Cantidad: {producto['Cantidad']}')
    print()


def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')


lista_productos = []

menu = ["[1] Agregar producto",
        "[2] Eliminar producto existente",
        "[3] Mostrar inventario",
        "[4] Salir del programa"]

while True:
    limpiar_pantalla()
    for item in menu:
        print(item)

    entrada = input('Opción:  ')
    if not entrada.isdigit():
        print('Por favor introducir un valor entre 1 y 4')
        input('Presionar enter para continuar ...')
        continue
    else:
        entrada = int(entrada)

    match entrada:
        case 1:
            agregar_producto(lista_productos)
        case 2:
            eliminar_producto(lista_productos)
        case 3:
            mostrar_inventario(lista_productos)
        case 4:
            print('Adios!')
            sys.exit(0)
    print()
    input('Presione Enter para continuar...')
