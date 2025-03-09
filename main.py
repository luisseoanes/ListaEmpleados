from PruebasIniciales import ListaDobleEmpleados, Empleado # Herencia de objetos contenidos en el archivo "Pruebas Iniciales".
import re # Librería para poder ingresar expresiones regulares. 

def menu(): # Crearemos una interfaz más "amigable" para el usuario:
    print("\n Menú Para La Gestión de Empleados: TechSolutions Inc.")
    print("1. Insertar empleado")
    print("2. Buscar empleado por identificador")
    print("3. Eliminar empleado por identificador")
    print("4. Ordenar empleados por nombre")
    print("5. Ordenar empleados por salario")
    print("6. Calculas estadísticas básicas del salario")
    print("7. Mostrar lista de empleados")
    print("8. Salir del programa")
    
def ascendente_descendente(): # Método para que el usuario elija si ordenar de forma ascendente o descendente.
    print("\n Seleccione el orden en el que desea ordenar: ") # "Mini menú".
    print("1. Ascendente")
    print("2. Descendente")
    while True: # Ciclo para asegurarnos de que elija una entrada válida.
        try:
            opcion = int(input("Ingrese 1 para ascendente o 2 para descendente: ")) # Especificaciones.
            if opcion in [1, 2]: # Validación de la opción que eligió el usuario.
                return opcion == 1 # Verdadero para "Ascendente" y Falso para "Descendente".
            else:
                print("Error: Ingrese 1 para ascendente o 2 para descendente")
        except ValueError: # Error tipo de valor incorrecto.
            print("Error: Ingrese una opción válida.")
    
def validar_entrada_enteros(instruccion): # Método para validar la entrada de números enteros positivos.
    while True:
        try:
            valor = int(input(instruccion))
            if valor <= 0: # Si el número es igual o menor a "0":
                print("Error: Ingrese un número entero positivo.")
            else:
                return valor
        except ValueError: # Error de tipo valor incorrecto.
            print("Error: Ingrese un número válido.")
            
def validar_entrada_salario(instruccion): # Método para validar la entrada de salarios.
    while True:
        try:
            valor = float(input(instruccion))
            if valor < 0: # Si el número es menor a "0":
                print("Error: Ingrese un salario válido.")
            else:
                return valor
        except ValueError: # Error tipo de valor incorrecto.
            print("Error: Ingrese un número válido.")
            
def validar_entrada_nombre(instruccion): # Método para validar carácteres en la entrada de "nombre".
    while True:
        nombre = input(instruccion).strip() # Limpiamos espacios al inicio y al final de la entrada.
        nombre = re.sub(r'\s+', '', nombre) # Si hay más de un espacio en medio, se reemplaza por uno solo.
        if not nombre.replace(" ", "").isalpha(): # Verificación de que solo tenga carácteres alfanuméricos.
            print("Error: El nombre solo puede contener letras y espacios.")
        else:
            return nombre
    
def main(): # Función que ejecutará el programa.
    lista = ListaDobleEmpleados() # Instanciamos la clase "ListaDobleEmpleados"
    while True:
        menu() # Mostramos menú al usuario encargado de administrar la interfaz.
        try:
            opcion_menu = int(input("Seleccione una opción del menú: "))
            if opcion_menu == 1: # Si la opción es "1":
                decision = True # Instanciamos para controlar el ciclo.
                while decision: # Ciclo para que el usuario no se tenga que salir al menú principal en caso de querer agregar otro empleado.
                    nombre = validar_entrada_nombre("Ingrese el nombre del empleado: ") # Se pide el nombre y se valida que la entrada sea correcta.
                    id = validar_entrada_enteros("Ingrese el identificador del empleado: ") # Se pide el identificador del empleado y se valida que la entrada sea correcta.
                    salario = validar_entrada_salario("Ingrese el salario del empleado: ") # Se pide el salario del empleado y se valida que la entrada sea correcta.
                    lista.insertar_empleado(Empleado(nombre, id, salario)) # Creamos un "objeto" con las características de la clase "Empleado". Luego lo mandamos para la variable "lista".
                    print("El empleado ha sido agregado correctamente.")
                    while True: # Preguntaremos al usuario sobre qué desea hacer.
                        try:
                            respuesta = int(input("¿Desea agregar otro empleado? (1. Sí, 2. No): ")) # Instanciamos su decisión en una variable.
                            if respuesta == 1: # Si la respuesta es "Sí".
                                break # Volvemos al ciclo principal.
                            elif respuesta == 2: # Si la respuesta es "No".
                                decision = False # Salimos del ciclo.
                                break
                            else: # Si la respuesta no es "1" o "2". 
                                print("Error: Ingrese 1 para Sí o 2 para No.")
                        except ValueError: # Error de tipo valor incorrecto.
                            print("Error: Ingrese un número entre las opciones.")
            elif opcion_menu == 2: # Si la opción es "2":
                id = validar_entrada_enteros("Ingrese el identificador del empleado a buscar: ") # Se pide el identificador del empleado a buscar y se valida que la entrada sea correcta.
                lista.buscar_empleado(id) # Pasamos el identificador del empleado al método "buscar_empleado()".
            elif opcion_menu == 3: # Si la opción es "3":
                id = validar_entrada_enteros("Ingrese el identificador del empleado a eliminar: ") # Se pide el identificador del empleado a eliminar y se valida que la entrada sea correcta.
                lista.eliminar_empleado(id) # Pasamos el identificador del empleado al método "eliminar_empleado()".
            elif opcion_menu == 4: # Si la opción es "4":
                orden = ascendente_descendente() # Llamamos al método "ascendente_descendente()".
                lista.ordenar_por_nombre(orden) # Llamamos al método "ordenar_por_nombre()".
                print("La lista de empleados ha sido ordenada por nombre.")
            elif opcion_menu == 5: # Si la opción es "5":
                orden = ascendente_descendente() # Llamamos al método "ascendente_descendente()".
                lista.ordenar_por_salario(orden) # Llamamos al método "ordenar_por_salario()".
                print("La lista de empleados ha sido ordenada por salario.")
            elif opcion_menu == 6: # Si la opción es "6":
                # Obtenemos análisis estadísticos sobre los salarios de los empleados:
                lista.calcular_promedio_salario()
                lista.obtener_mediana_salario()
                lista.encontrar_salario_maximo()
                lista.encontrar_salario_minimo()
            elif opcion_menu == 7: # Si la opción es "7":
                lista.imprimir_lista() # Llamamos al método "imprimir_lista()".
            elif opcion_menu == 8: # Si la opción es "8":
                # Rompemos el bucle y le damos un mensaje amigable de despedida a nuestro usuario.
                print("Gracias por utilizar nuestro sistema de gestión de empleados para la empresa TechSolutions Inc. Regresa prontoo ;)!")
                break
            else: # Por si el usuario ingresa un número diferente de los del menú.
                print("Opción inválida. Intente de nuevo.")
        except ValueError: # Error de tipo valor incorrecto.
            print("Error: Ingrese un número válido.")
            
if __name__ == "__main__": # Si la clase main se está ejecutando en el mismo archivo correspondiente:
    main() # Ejecutamos.