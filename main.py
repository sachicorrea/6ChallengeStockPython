""" RETO SEMANA 6
  Autor del programa
  Nombre del reto 
  Grupo
  Fecha
"""""

#---------------- Zona librerias------------
import funcionesInventario as f

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def menuOpciones():
  bandera=0
  while(bandera == 0):
    print("\n ||||---------------GESTION DE INVENTARIOS---------------|||| ")
    print("   1.Mostrar inventario total (1) ")
    print("   ...............................")
    print("   2. Mostrar inventario por sucursal (2) ")
    print("   ...............................")
    print("   3. Mostrar inventario por producto (3) ")
    print("   ...............................")
    print("   4. Calcular cantidad de productos totales (4) ")
    print("   ...............................")
    print("   5. Calcular cantidad de productos por sucursal (5) ")
    print("   ...............................")
    print("   6. Calcular cantidad de productos por tipo  (6) ")
    print("   ...............................")
    print("   7. Mostrar precios de los productos (7) ")
    print("   ...............................")
    print("   8. Calcular valor inventario por sucursal  (8) ")
    print("   ...............................")
    print("   9. Hacer pedido sucursal  (9) ")
    print("   ...............................")
    print("   10. Graficar cantidad productos por tipo (10)")
    print("   ...............................")
    print("\n 0. Salir (0)")
    print("\n .............OPCIONALES..................")
    print("....")

    opcion = int(input("\n Seleccione una opción: "))

    if opcion == 1:
      print("\n 1.Mostrar inventario:".upper())
      """
      TODO
      Implementar las funciones 
      """   
      f.mostrar_inventario()
    
    elif opcion == 2:
      print("2. Mostrar inventario por sucursal".upper())
      nombre_sucursal = input("\n Ingrese nombre de la sucursal: ").upper()
 
      f.mostrar_inventario_sucursal(nombre_sucursal)

    elif opcion == 3:
      print("3. Mostrar inventario por producto".upper())
      nombre_producto = input("\n Ingrese producto a mostrar: ").lower()
 
      f.mostrar_inventario_producto(nombre_producto)

    elif opcion == 4:
      print("4. Calcular cantidad de productos totales".upper())
      print(f.calcular_cantidad_productos_totales())

    elif opcion == 5:
      print("5. Calcular cantidad de productos por sucursal".upper())
      nombre_sucursal = input("\n Ingrese nombre de la sucursal: ").upper()
      
      print(f.calcular_cantidad_productos_sucursal(nombre_sucursal))

    elif opcion == 6:
      print("6. Calcular cantidad de productos por tipo".upper())
      nombre_producto = input("\n Ingrese el tipo de producto: ").lower()
      
      print(f.calcular_cantidad_productos_tipo(nombre_producto))

    elif opcion == 7:
      print("7. Mostrar precios producto".upper())
      f.loadFile()
      f.cargar_precios_productos()
    
    elif opcion == 8:
      print("8. Calcular valor inventario por sucursal".upper())
      
      nombre_sucursal = input("\n Ingrese nombre de la sucursal: ").upper()
      f.loadFile()
      f.mostrar_precios_productos(nombre_sucursal)
      f.calcular_valor_inventario_sucursal(nombre_sucursal)

    elif opcion == 9:
      print("9. Hacer pedido sucursal".upper())
    
      nombre_sucursal = input("\n Ingrese nombre de la sucursal: ")
      f.crear_pedido_sucursal(nombre_sucursal)
      f.savePurchase(nombre_sucursal)
    
    elif opcion == 10:
      print("10. Graficar cantidad productos por tipo".upper())
    
      nombre_producto = input("\n Ingrese nombre del producto: ")
      f.graficar_productos_tipo(nombre_producto) 

    elif opcion == 0:
      bandera=1
  
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#Recuerde comentar la siguiente instrucción para ejecutar los test
menuOpciones()