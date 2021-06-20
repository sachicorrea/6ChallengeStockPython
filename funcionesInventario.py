#---------------- Zona librerias------------
import matplotlib.pyplot as plt
import numpy as np
from typing import NamedTuple

#----Namedtuple for Product class----------
class Product(NamedTuple):
  item: str
  quantity: int
  location: str
  unitValue: int

  def print_productsByCity(self):
    print(f'{self.item} : {self.unitValue}  cantidad : {self.quantity}')

def get_products():
  return {
    Product('arroz', 180, 'BOGOTA', 1700),
    Product('arroz', 205, 'CALI', 1700),
    Product('arroz', 271, 'PASTO', 1700),
    Product('arroz', 403, 'TULUA', 1700),
    Product('huevo', 755, 'BOGOTA', 7000),
    Product('huevo', 105, 'CALI', 7000),
    Product('huevo', 351, 'PASTO', 7000),
    Product('huevo', 804, 'TULUA', 7000),
    Product('leche', 305, 'BOGOTA', 3500),
    Product('leche', 545, 'CALI', 3500),
    Product('leche', 361, 'PASTO', 3500),
    Product('leche', 744, 'TULUA', 3500),
    Product('panela', 110, 'BOGOTA', 2000),
    Product('panela', 277, 'CALI', 2000),
    Product('panela', 388, 'PASTO', 2000),
    Product('panela', 493, 'TULUA', 2000),
    Product('queso', 980, 'BOGOTA', 4000),
    Product('queso', 805, 'CALI', 4000),
    Product('queso', 741, 'PASTO', 4000),
    Product('queso', 969, 'TULUA', 4000),
    Product('pasta', 650, 'BOGOTA', 1200),
    Product('pasta', 448, 'CALI', 1200),
    Product('pasta', 681, 'PASTO', 1200),
    Product('pasta', 249, 'TULUA', 1200),
  }       

products = get_products()

#---------------- Zona matrices------------

matriz_inventario=[[180,205,271,403], [755,105,351,804], [305,545,361,744], [110,277,388,493],[980,805,741,969], [650,448,681,249]]

lista_nombres_sucursales=["BOGOTA", "CALI", "PASTO", "TULUA"]

lista_nombres_productos=["arroz", "huevo", "leche", "panela", "queso", "pasta"]

diccionario_precios_productos={"arroz":0, "huevo":0,"leche":0, "panela":0, "queso":0, "pasta":0 }

# ---------------- Complementary functions zone ------------
# cities function
def cities_position(nombre_sucursal):
  if nombre_sucursal == "BOGO" or nombre_sucursal == "BOGOTA" or nombre_sucursal == "BOGOTÁ":
    column = 0
  elif nombre_sucursal == "CALI":
    column = 1
  elif nombre_sucursal == "PASTO":
    column = 2
  elif nombre_sucursal == "TULUA" or nombre_sucursal == "TULUÁ":
    column = 3
  return column

# prodcuts function
def product_position(nombre_producto):
  if nombre_producto == "arroz":
    row = 0
  elif nombre_producto == "huevo":
    row = 1
  elif nombre_producto == "leche":
    row = 2
  elif nombre_producto == "panela":
    row = 3
  elif nombre_producto == "queso":
    row = 4
  elif nombre_producto == "pasta":
    row = 5
  return row

# Function to load precios.txt
def loadFile():
  file = open("precios.txt", "r")

  for row in file:
    price = row.split("=")
    key = price[0]
    value = price[1].split("\n")
    products_dict.update({key:float(value[0])})

  file.close()

# Function to save purchases
def savePurchase(nombre_sucursal):
  try:
    file_products = open('pedido.txt', 'a')
    file_products.write("\n Pedido para la sucursal: " + nombre_sucursal + "\n" + str(my_list))
    file_products.close()
    print("Pedido creado")
  
  except:
    print("No se puede indexar a un archivo")

#---------------- Zona diccionarios -----------
products_dict = {}
purchases_dict = {}

#---------------- Graphs -----------
def graph_line():
  xpoints = np.array([0,200])
  ypoints = np.array([0,1000])
  plt.plot(xpoints, ypoints)
  plt.xlabel = ("Ciudades")
  plt.ylabel = ("Cantidad")
  plt.show()

#---------------- Zona funciones------------
# 1st Acivity
def mostrar_inventario():
  """
  TODO 
  Mostrar la cantidad de productos en el inventario para todas las sedes
  """
  for cities in lista_nombres_sucursales:
    print(cities, end="\t")

  for r in range(0,6):
    print("")
    print(lista_nombres_productos[r], end="\t")

    for c in range(0,4):
      print(matriz_inventario[r][c], end="\t\t")
    print("")

# 2nd Activity
def mostrar_inventario_sucursal(nombre_sucursal):
  """
  TODO 
  Mostrar la cantidad de productos en el inventario para el nombre de la sede ingresado por parametro
  """
  if nombre_sucursal in lista_nombres_sucursales:
    column_city = cities_position(nombre_sucursal)

    for r in range(0,6):
      print(lista_nombres_productos[r], end=" : ")

      for c in range(0,1):
        print(matriz_inventario[r][column_city])
      print("")
  else:
    print("Ciudad no encontrada")

# 3rd activity
def mostrar_inventario_producto(nombre_producto):
  """
  TODO 
  Mostrar la cantidad de productos en el inventario para el tipo de producto ingresado por parametro
  """
  if nombre_producto in lista_nombres_productos:
    row_product = product_position(nombre_producto)

    for cities in lista_nombres_sucursales:
      print(cities, end="\t")

    for r in range(0,1):
      print("")
      for c in range(0,4):
        print(matriz_inventario[row_product][c], end="\t\t")
    print("")
  
  else:
    print("Producto no encontrado")

# 4th activity
def calcular_cantidad_productos_totales():
  """
  TODO 
  Retorna la cantidad total de productos
  """
  sum = 0

  for r in range(0,6):
    for c in range(0,4):
      sum += matriz_inventario[r][c]
  return sum

# 5th activity
def calcular_cantidad_productos_sucursal(nombre_sucursal):
  """
  TODO
  Retorna la cantidad total de productos de la sucursal ingresada por parametro
  """
  if nombre_sucursal in lista_nombres_sucursales:
    column_city1 = cities_position(nombre_sucursal)
    sum = 0

    for r in range(0, len(matriz_inventario)):
      sum += matriz_inventario[r][column_city1]
    return sum

  else:
    print("Ciudad no encontrada")

# 6th Activity
def calcular_cantidad_productos_tipo(nombre_producto):
  """
  TODO 
  Retorna la cantidad de productos en el inventario para el tipo de producto ingresado por parametro
  """
  if nombre_producto in lista_nombres_productos:
    row_product1 = product_position(nombre_producto)
    sum = 0

    for r in range(0, len(lista_nombres_productos)):
      print("")
      for c in range(0,len(lista_nombres_sucursales)):
        sum += matriz_inventario[row_product1][c]
      return sum
  else:
    print("Producto no encontrado")

#7th Activity
def cargar_precios_productos():
  """
  TODO
  Carga del archivo precios.txt los precios de los productos
  """
  for keys, values in products_dict.items():
    print("\n", keys, " : ", values)

# 8th activity
def mostrar_precios_productos(nombre_sucursal):
  """
  TODO
  Muestra los precios de los productos
  """
  # List of filtering products by cities 
  
  #filter a list of tuples - from Product class
  filter_by_cities = filter(lambda c: c[2] == nombre_sucursal, products)
  filter_productsCities_list = list(filter_by_cities)
  
  filter_productsCities_list.sort(key=lambda e: e.item)

  # Print products and quantities by city
  for x in filter_productsCities_list:
    x.print_productsByCity()

def calcular_valor_inventario_sucursal(nombre_sucursal):
  """
  TODO
  Retorna el total de inventario según la cantidad de productos y precio de cada producto, en la sucursal indicada por parametro
  """
  # List of filtering products by cities 
  
  #filter a list of tuples - from Product class
  filter_by_cities = filter(lambda c: c[2] == nombre_sucursal, products)
  filter_productsCities_list = list(filter_by_cities)
  
  filter_productsCities_list.sort(key=lambda e: e.item)

  # List of products' quantities by location
  products_quantity_list = [quantity for (name, quantity, location, unitValue) in filter_productsCities_list if location == nombre_sucursal]

  # Matrixes multiplication to get stock's total cost
  a = np.array(products_quantity_list)
  b = np.array([[1700],
                [7000], 
                [3500],
                [2000],
                [1200], 
                [4000]])
  
  c = np.matmul(a,b)
  print(c)
  #return 0

# 9th activity
my_list = {}
def crear_pedido_sucursal(nombre_sucursal):
  """
  TODO
  Crea el pedido de productos para la sucursal recibida por parametro. La cantidad de productos es ingresada por el usuario. El pedido creado se almacena en el archivo pedido.txt. Se retorna un mensaje "Pedido creado"
  """
  for i in lista_nombres_productos:
    print("Enter value for {}: ". format(i))
    elm = int(input())
    my_list[i] = elm

# 10th activity
def graficar_productos_tipo(nombre_producto):
  """
  TODO
  Grafica la cantidad de productos del inventario por sucursal, se especifica el nombre del producto
  """

  # Filter products. Create products list
  filter_by_products = filter(lambda c: c[0] == nombre_producto, products)
  filter_products_list = list(filter_by_products)

  # filter() a list of tuples - from Product class
  # List of products
  products_list_quantity = [quantity for (item, quantity, location, unitValue) in filter_products_list if item == nombre_producto]
 
  # Locations list
  products_list_location = [location for (item, quantity, location, unitValue) in filter_products_list if item == nombre_producto]

  # Products chart
  def graph_bar():
    x = np.array(products_list_location)
    y = np.array(products_list_quantity)

    plt.xlabel("city")
    plt.ylabel("quantity")
    plt.bar(x,y)
    plt.show()
  
  graph_bar()