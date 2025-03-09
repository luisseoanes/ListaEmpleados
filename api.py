# Importamos Flask para crear la API RESTful
from flask import Flask, request, jsonify
import re # Librería para poder ingresar expresiones regulares.

# Primero creamos y definimos la clase Empleado, el NodoEmpleado y la Lista.

class Empleado:
    def __init__(self, nombre: str, id: int, salario: float): # Instanciamos la clase con el constructor "init" para evitar problemas adelante, y procedemos a darle atributos.
        self.nombre = nombre # Nombre empleado
        self.id = id # Identificador del empleado
        self.salario = salario # Salario empleado
    
    def __str__(self): # Definimos cómo queremos que se imprima el objeto "Empleado".
        return f"ID: {self.id} | Nombre: {self.nombre} | Salario: ${self.salario:.1f}"
    
    def to_dict(self): # Método para convertir el objeto a diccionario para la API
        return {
            "id": self.id,
            "nombre": self.nombre,
            "salario": self.salario
        }
    
class NodoEmpleado:
    def __init__(self, empleado: Empleado): # Guardamos el objeto "Empleado" en el nodo.
        self.empleado = empleado
        self.siguiente = None # Definimos qué direcciones tiene, sin embargo aún no está conectado con otros nodos.
        self.anterior = None

class ListaDobleEmpleados:
    def __init__(self): # Definimos los atributos de la lista doblemente ligada.
        self.cabeza = None # Aún no posee nodos dentro de ella; esto también se hace necesario especificarlo.
        self.cola = None
        
    def insertar_empleado(self, empleado: Empleado): # Función que inserta un empleado al final de la lista. Contiene el objeto "Empleado".
        nuevo_nodo = NodoEmpleado(empleado) # Creamos un nodo con las características de el objeto "Empleado".
        if not self.cabeza: # Si la lista no contiene ningún nodo:
            self.cabeza = self.cola = nuevo_nodo # La cola y la cabeza son el nuevo nodo.
        else: # Si la lista ya contiene nodos:
            nuevo_nodo.anterior = self.cola # Tomamos como referencia, de espacio/lugar, el atributo "anterior" de "nuevo_nodo", el cual va a ser la cola de la lista.
            self.cola.siguiente = nuevo_nodo # El puntero de la cola de la lista, va a dirigirse hacia el nuevo nodo.
            self.cola = nuevo_nodo # La cola será el nuevo nodo.    
            
    def imprimir_lista(self): # Necesitamos recorrer la lista para poder mostrar los elementos dentro.
        if not self.cabeza: # Si la lista está vacía.
            return []
        actual = self.cabeza # El recorrido empieza desde el primer dato de la lista.
        empleados = []
        while actual: # Mientras "actual" contenga algún nodo:
            empleados.append(actual.empleado.to_dict()) # Añadimos el empleado a la lista como diccionario
            actual = actual.siguiente # Por cada impresión, pasamos al siguiente nodo hasta llegar al nulo.
        return empleados
            
    def buscar_empleado(self, id: int): # Función para buscar algún empleado por identificador. Necesita el parámetro "id" de cada nodo.
        actual = self.cabeza
        while actual: # Mientras "actual" contenga algún nodo:
            if actual.empleado.id == id: # Si el identificador del empleado es igual al buscado:
                return actual.empleado # Devuelve el empleado encontrado.
            actual = actual.siguiente # Por cada búsqueda, pasamos al siguiente nodo hasta llegar al nulo.
        return None
    
    def eliminar_empleado(self, id: int): # Función para eliminar algún empleado por identificador. Necesita el parámetro "id" de cada nodo.
            actual = self.cabeza
            while actual: # Mientras haya un nodo en la lista
                if actual.empleado.id == id: # Si el identificador del empleado es igual al buscado:
                    if actual.anterior: # Si el nodo tiene un nodo anterior:
                        actual.anterior.siguiente = actual.siguiente # El anterior nodo, ahora apunta al siguiente nodo.
                    else: # Si el nodo es la cabeza de la lista:
                        self.cabeza = actual.siguiente # La cabeza ahora apunta al siguiente nodo.
                    if actual.siguiente: # Si el nodo tiene un nodo siguiente:
                        actual.siguiente.anterior = actual.anterior # El siguiente nodo, ahora apunta al anterior nodo.
                    else: # Si el nodo es la cola de la lista:
                        self.cola = actual.anterior # La cola ahora apunta al anterior nodo.    
                    return True
                actual = actual.siguiente
            return False
                
    def ordenar_por_nombre(self, ascendente=True): # Función para ordenar lista por nombre. No crearemos otra lista.
        if not self.cabeza or not self.cabeza.siguiente: # Si la lista está vacía o si solo tiene un nodo:
            return # No hay cambios que aplicar.
        
        condicion = True # Instanciamos para poder crear un ciclo.
        while condicion:
            condicion = False # Se establece condición en "False".
            actual = self.cabeza
            while actual.siguiente: # Mientras haya más de un nodo:
                if (ascendente and actual.empleado.nombre > actual.siguiente.empleado.nombre) or \
                   (not ascendente and actual.empleado.nombre < actual.siguiente.empleado.nombre):
                    # Si el nombre del actual es mayor o menor que el siguiente, intercambiamos sus posiciones.
                    actual.empleado, actual.siguiente.empleado = actual.siguiente.empleado, actual.empleado # Se intercambian los empleados entre los nodos.
                    condicion = True # Si se realiza algún cambio, la condición cambia a "True", para volver a recorrer la lista.
                actual = actual.siguiente # Vamos al siguiente nodo para seguir revisando orden.
        
    def ordenar_por_salario(self, ascendente=True): # Función para ordenar lista por salario. No crearemos otra lista.
        if not self.cabeza or not self.cabeza.siguiente: # Si la lista está vacía o si solo tiene un nodo:
            return # No hay cambios que aplicar.
        
        condicion = True # Instanciamos para poder crear un ciclo.
        while condicion:
            condicion = False # Se establece condición en "False".
            actual = self.cabeza
            while actual.siguiente: # Mientras haya más de un nodo:
                if (ascendente and actual.empleado.salario > actual.siguiente.empleado.salario) or \
                   (not ascendente and actual.empleado.salario < actual.siguiente.empleado.salario):
                    # Si el salario del actual es mayor o menor que el siguiente, intercambiamos sus posiciones.
                    actual.empleado, actual.siguiente.empleado = actual.siguiente.empleado, actual.empleado # Se intercambian los empleados entre los nodos.
                    condicion = True # Si se realiza algún cambio, la condición cambia a "True", para volver a recorrer la lista.
                actual = actual.siguiente # Vamos al siguiente nodo para seguir revisando orden.
            
    def calcular_promedio_salario(self): # Método para sacar el promedio de los salarios: total de la suma salarial sobre número de empleados.
        if not self.cabeza: # Si la lista está vacía:
            return None
        total = 0 # Instanciamos una variable que contenga la suma salarial.
        contador = 0 # Instanciamos una variable que haga de contador.
        actual = self.cabeza # Empezamos desde la cabeza de la lista.
        while actual:
            total += actual.empleado.salario # Se envía el salario a la variable "total" para irlo sumando.
            contador += 1 # Por cada empleado encontrado, se suma 1 al contador.
            actual = actual.siguiente # Pasar al siguiente empleado.
        promedio = total / contador # Calcular el promedio salarial: total de la suma salarial sobre el número de empleados.
        return promedio
    
    def encontrar_salario_maximo(self): # Método para encontrar el empleado con el salario máximo: recorrer e ir actualizando la variable que contiene al empleado con el máximo salario.
        if not self.cabeza: # Si la lista está vacía:
            return None
        salario_maximo = self.cabeza.empleado # Instanciamos la variable "salario_maximo" con el salario del primer empleado.
        actual = self.cabeza.siguiente # Empezamos desde el segundo empleado.
        while actual:
            if actual.empleado.salario > salario_maximo.salario: # Si el salario del actual es mayor que el salario máximo:
                salario_maximo = actual.empleado # Se reemplaza el salario máximo con el salario del actual.
            actual = actual.siguiente # Pasamos al siguiente empleado.
        return salario_maximo
    
    def encontrar_salario_minimo(self):
        if not self.cabeza: # Si la lista está vacía:
            return None
        salario_minimo = self.cabeza.empleado # Instanciamos la variable "salario_minimo" con el salario del primer empleado.
        actual = self.cabeza.siguiente # Empezamos desde el segundo empleado.
        while actual:
            if actual.empleado.salario < salario_minimo.salario: # Si el salario del actual es menor que el salario mínimo:
                salario_minimo = actual.empleado # Se reemplaza el salario mínimo con el salario del actual.
            actual = actual.siguiente # Pasamos al siguiente empleado.
        return salario_minimo
    
    def obtener_mediana_salario(self):
        if not self.cabeza: # Si la lista está vacía:
            return None
        salarios = [] # Necesitamos almacenar todos los salarios en una lista.
        actual = self.cabeza
        while actual:
            salarios.append(actual.empleado.salario) # Que se vaya agregando a la lista el salario del empleado actual en cada recorrido.
            actual = actual.siguiente # Pasamos al siguiente empleado.
        salarios.sort() # Ordenamos la lista de salarios de menor a mayor.
        cantidad_salarios = len(salarios) # Instanciamos una variable que contenga el número de salarios agregados a la lista "Salarios".
        if cantidad_salarios % 2 == 0: # Si la cantidad de salarios es par:
            mediana = (salarios[cantidad_salarios // 2 - 1] + salarios[cantidad_salarios // 2]) / 2 # De la lista "Salarios", ya ordenada de menor a mayor, se toma el promedio de los dos salarios en el centro de la lista.
        else: # Si la cantidad de salarios es impar:
            mediana = salarios[cantidad_salarios // 2] # De la lista "Salarios", ya ordenada de menor a mayor, se dividen los índices por la mitad y se toma el de todo el medio.
        return mediana

# Configuración de la API con Flask
app = Flask(__name__)
lista_empleados = ListaDobleEmpleados()  # Instancia global de la lista de empleados

def validar_nombre(nombre):
    # Validamos que el nombre solo contiene letras y espacios
    return bool(re.match(r'^[A-Za-z\s]+$', nombre))

# Rutas de la API

@app.route('/empleados', methods=['GET'])
def obtener_empleados():
    """Obtener lista de todos los empleados"""
    empleados = lista_empleados.imprimir_lista()
    return jsonify({"empleados": empleados})

@app.route('/empleados', methods=['POST'])
def crear_empleado():
    """Crear un nuevo empleado"""
    datos = request.json
    
    # Verificamos que los datos requeridos estén presentes
    if not all(key in datos for key in ['nombre', 'id', 'salario']):
        return jsonify({"error": "Faltan datos obligatorios (nombre, id, salario)"}), 400
    
    # Validamos los tipos de datos y formatos
    try:
        id = int(datos['id'])
        if id <= 0:
            return jsonify({"error": "El ID debe ser un número entero positivo"}), 400
    except ValueError:
        return jsonify({"error": "El ID debe ser un número entero"}), 400
    
    # Verificamos que no exista ya un empleado con ese ID
    if lista_empleados.buscar_empleado(id):
        return jsonify({"error": f"Ya existe un empleado con el ID {id}"}), 400
    
    try:
        salario = float(datos['salario'])
        if salario < 0:
            return jsonify({"error": "El salario debe ser un número positivo"}), 400
    except ValueError:
        return jsonify({"error": "El salario debe ser un número"}), 400
        
    nombre = datos['nombre'].strip()
    if not validar_nombre(nombre):
        return jsonify({"error": "El nombre solo puede contener letras y espacios"}), 400
    
    # Creamos e insertamos el nuevo empleado
    nuevo_empleado = Empleado(nombre, id, salario)
    lista_empleados.insertar_empleado(nuevo_empleado)
    
    return jsonify({"mensaje": "Empleado agregado correctamente", "empleado": nuevo_empleado.to_dict()}), 201

@app.route('/empleados/<int:id>', methods=['GET'])
def buscar_empleado(id):
    """Buscar un empleado por su ID"""
    empleado = lista_empleados.buscar_empleado(id)
    if empleado:
        return jsonify({"empleado": empleado.to_dict()})
    else:
        return jsonify({"error": f"No se encontró un empleado con el ID {id}"}), 404

@app.route('/empleados/<int:id>', methods=['DELETE'])
def eliminar_empleado(id):
    """Eliminar un empleado por su ID"""
    resultado = lista_empleados.eliminar_empleado(id)
    if resultado:
        return jsonify({"mensaje": f"Empleado con ID {id} eliminado correctamente"})
    else:
        return jsonify({"error": f"No se encontró un empleado con el ID {id}"}), 404

@app.route('/empleados/ordenar', methods=['GET'])
def ordenar_empleados():
    """Ordenar empleados por nombre o salario"""
    tipo = request.args.get('tipo', 'nombre')  # nombre o salario
    orden = request.args.get('orden', 'asc')   # asc o desc
    
    ascendente = orden.lower() == 'asc'
    
    if tipo.lower() == 'nombre':
        lista_empleados.ordenar_por_nombre(ascendente)
    elif tipo.lower() == 'salario':
        lista_empleados.ordenar_por_salario(ascendente)
    else:
        return jsonify({"error": "El tipo de ordenamiento debe ser 'nombre' o 'salario'"}), 400
    
    return jsonify({"mensaje": f"Lista ordenada por {tipo} en orden {'ascendente' if ascendente else 'descendente'}", 
                   "empleados": lista_empleados.imprimir_lista()})

@app.route('/empleados/estadisticas', methods=['GET'])
def obtener_estadisticas():
    """Obtener estadísticas de salarios"""
    promedio = lista_empleados.calcular_promedio_salario()
    if promedio is None:
        return jsonify({"error": "No hay empleados registrados"}), 404
    
    mediana = lista_empleados.obtener_mediana_salario()
    max_empleado = lista_empleados.encontrar_salario_maximo()
    min_empleado = lista_empleados.encontrar_salario_minimo()
    
    return jsonify({
        "promedio_salario": round(promedio, 1),
        "mediana_salario": round(mediana, 1),
        "salario_maximo": {
            "empleado": max_empleado.nombre,
            "id": max_empleado.id,
            "salario": max_empleado.salario
        },
        "salario_minimo": {
            "empleado": min_empleado.nombre,
            "id": min_empleado.id,
            "salario": min_empleado.salario
        }
    })

# Para ejecutar la API
if __name__ == "__main__":
    app.run(debug=True)