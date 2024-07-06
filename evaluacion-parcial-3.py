import json

# Definición de menús disponibles
menus_disponibles = {
    1: "Comida Italiana",
    2: "Comida Japonesa",
    3: "BBQ"
}

# Lista para almacenar los pedidos
pedidos = []

# Función para registrar un nuevo pedido
def registrar_pedido():
    print("\n--- Registro de Pedido ---")
    pedido = {}
    pedido['cliente'] = input("Nombre del cliente: ")
    pedido['contacto'] = input("Nombre del contacto: ")
    pedido['evento'] = input("Detalle del evento (tipo, fecha, dirección): ")

# Mostrar menús disponibles
    print("Menus disponibles:")
    for key, menu in menus_disponibles.items():
        print(f"{key}. {menu}")

    opcion_menu = int(input("Seleccione el número del menú: "))
    while opcion_menu not in menus_disponibles:
        print("Opción no válida. Intente de nuevo.")
        opcion_menu = int(input("Seleccione el número del menú: "))

    pedido['menu'] = menus_disponibles[opcion_menu]
    pedido['comensales'] = int(input("Numero de comensales: "))

# Añadir pedido a la lista de pedidos
    pedidos.append(pedido)
    
    print("Pedido registrado exitosamente.\n")
    
# Función para listar todos los pedidos registrados
def listar_pedidos():
    print("\n--- Lista de Pedidos ---")
    for index, pedido in enumerate(pedidos, start=1):
        print(f"Pedido {index}:")
        print(f"Cliente: {pedido['cliente']}")
        print(f"Contacto: {pedido['contacto']}")
        print(f"Evento: {pedido['evento']}")
        print(f"Menú: {pedido['menu']}")
        print(f"Comensales: {pedido['comensales']}")
        print()

# Función para imprimir el detalle de pedidos filtrados por menú
def imprimir_detalle_por_menu():
    print("\n--- Impresión de Detalle por Menú ---")
    print("Menús disponibles:")
    for key, menu in menus_disponibles.items():
        print(f"{key}. {menu}")

    opcion_menu = int(input("Seleccione el número del menú para imprimir el detalle: "))
    while opcion_menu not in menus_disponibles:
        print("Opción no válida. Intente de nuevo.")
        opcion_menu = int(input("Seleccione el número del menú: "))
    
    menu_seleccionado = menus_disponibles[opcion_menu]

# Filtrar pedidos por el menú seleccionado
    pedidos_menu = [pedido for pedido in pedidos if pedido['menu'] == menu_seleccionado]

# Guardar en archivo .txt
    with open(f"detalle_{menu_seleccionado.lower().replace(' ', '_')}.txt", 'w') as txt_file:
        for pedido in pedidos_menu:
            txt_file.write(f"Cliente: {pedido['cliente']}\n")
            txt_file.write(f"Contacto: {pedido['contacto']}\n")
            txt_file.write(f"Evento: {pedido['evento']}\n")
            txt_file.write(f"Menú: {pedido['menu']}\n")
            txt_file.write(f"Comensales: {pedido['comensales']}\n")
            txt_file.write("\n")
    
# Guardar en archivo .json
    with open(f"detalle_{menu_seleccionado.lower().replace(' ', '_')}.json", 'w') as json_file:
        json.dump(pedidos_menu, json_file, indent=4)
    
    print(f"Detalle de pedidos con menú {menu_seleccionado} guardado en archivos.\n")

# Ejecutar el programa
while True:
    print("----- MENÚ -----") # Menú principal del programa
    print("1. Registrar Pedido")
    print("2. Listar Pedidos")
    print("3. Imprimir Detalle de Pedidos por Menú")
    print("4. Salir del Programa")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_pedido()
    elif opcion == '2':
        listar_pedidos()
    elif opcion == '3':
        imprimir_detalle_por_menu()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.\n")