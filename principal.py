from proveedores import proveedor
from productos import producto
global prov1,prod1
Opcion = ""
prov1 = proveedor()
prod1 = producto()

while(Opcion!=5):
    print("1. Agregar Proveedor")
    print("2. Crear un Producto")
    print("3. Agrgar producto a Proveedor")
    print("4. Listar Productos")
    print("5. Salir")
    print("Ingrese la opcion deseada: ")
    Opcion = int(input())

    if Opcion == 1:
        
        #Captura de Datos desde Teclado
        apellidos = input("Ingrese Apellidos:")
        nombre = input("Ingrese Nombre:")
        telefono = input("Ingrese Telefono:")
    
        #Crear el proveedor
        prov1.AgregarProveedor(apellidos,nombre,telefono)
    
    elif Opcion == 2:
    
        #Pedir ingreso de datos del producto
        codigo = int(input("Ingrese el codigo del producto"))
        nomproducto = input("Ingrese el nombre del producto")
        precio = int(input("Ingrese precio del producto"))
    
        #Crear Proveedor
        prod1.CrearProducto(codigo,nomproducto)
    elif Opcion == 3:
         prov1.AgregarProducto(prod1)
    
    elif Opcion == 4:
         prod1.ListaProductos(prod1)