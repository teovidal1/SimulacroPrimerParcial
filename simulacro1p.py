from funciones1p import *
inventario=[]

bandera = True
while bandera:

    print_menu()
    cantidad_productos= len(inventario)
    opcion = int(input("Ingrese la opción: "))

    while opcion<1 or opcion>6:
        opcion = int(input("Ingrese la opción: "))

    while cantidad_productos==0 and opcion!=1 and opcion!=6:
        print ("No hay suficientes productos") 
        opcion = int(input("Ingrese la opción: "))
        
    match opcion:
        case 1:
            cargar_producto(inventario)
        case 2:
            buscar_producto(inventario)
        case 3:
            ordenar_inventario(inventario)
        case 4:
            mostrar_mas_caro_y_barato(inventario)
        case 5:
            mostrar_mayor_a_15000(inventario)
        case 6: 
            break

print (inventario)