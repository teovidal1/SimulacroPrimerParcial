def print_menu ():
    print ("""
                OPCIONES:
        
        1:CARGAR PRODUCTO/S
        2:BUSCAR PRODUCTO/S
        3:ORDENAR INVENTARIO
        4:MOSTRAR PRODUCTO MÁS CARO Y MÁS BARATO
        5:MOSTRAR PRODUCTOS CON PRECIO MAYOR A 1500
        6:SALIR
        """)
    
def cargar_producto(inventario : list[list]):
    cantidad_a_ingresar = input("¿Cuántos productos desea ingresar?: ")
    while cantidad_a_ingresar.isdigit()==False:
            cantidad_a_ingresar = input ("¿Cuántos productos desea ingresar?: ")
    cantidad_a_ingresar = int(cantidad_a_ingresar)
    for _ in range(cantidad_a_ingresar):

        nombre = input ("Ingrese el nombre del nuevo producto: ")
        precio = input ("Ingrese el precio del nuevo producto: ")
        while precio.isdigit()==False:
            precio = input ("Ingrese el precio del nuevo producto: ")

        stock = input ("Ingrese el stock del nuevo producto: ")
        while stock.isdigit()==False:
            stock = input ("Ingrese el precio del nuevo producto: ")
        precio = int(precio)
        stock = int (stock)
        inventario.append([nombre,precio,stock])

def buscar_producto(inventario : list[list]):
    encontrado = False
    producto_buscado = input("Ingrese el producto que desea buscar: ")
    for i in range (len(inventario)):
        if inventario[i][0]==producto_buscado:
            print (f"El precio del producto {inventario[i][0]}  es ${inventario[i][1]} y tiene {inventario[i][2]} unidades en stock")
            encontrado = True
    if not encontrado:
        print("El producto no se encuentra disponible")

def ordenar_inventario(inventario : list[list]):
    cantidad_productos=len(inventario)
    for i in range (cantidad_productos-1):
        for j in range (cantidad_productos-1-i):
            if (inventario[j][1])>(inventario[j+1][1]):
                temp = inventario[j+1]
                inventario[j+1] = inventario[j]
                inventario[j] = temp         

def mostrar_mas_caro_y_barato(inventario : list[list]):
    precio_max=float("-inf")
    precio_min=float("inf")
    nombre_precio_max = ""
    nombre_precio_min = " "

    for i in range (len(inventario)):
        precio_producto=inventario[i][1]
        nombre_producto=inventario[i][0]

        if precio_producto>precio_max:
            precio_max = precio_producto
            nombre_precio_max = nombre_producto

        if precio_producto<precio_min:
            precio_min = precio_producto
            nombre_precio_min = nombre_producto
    print (f"""El producto más barato es {nombre_precio_min}, cuesta {precio_min}. 
        El producto más caro es {nombre_precio_max}, cuesta {precio_max}""")
    
def mostrar_mayor_a_15000(inventario : list[list]):
    mayores_15000 = []
    for i in range (len(inventario)):
        precio = inventario[i][1]
        nombre = inventario [i][0]
        if precio>15000:
            mayores_15000.append(nombre)
    
    for i in range (len(mayores_15000)):
        print (mayores_15000[i])