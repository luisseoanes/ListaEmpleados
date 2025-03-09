# Sistema de Gestión de Empleados.

## Descripción Proyecto.
Este proyecto permite la fácil gestión de los empleados de la empresa "TechSolutions Inc." por medio de las listas doblemente ligadas. 

El proyecto fue creado y diseñado bajo el lenguaje de programación "Python". La decisión de haberlo hecho en Python fue por la simplicidad y legibilidad de la sintaxis, por su estructura lógica y fácil manejo de listas doblemente ligadas. Por último, en caso de ser necesario escalar el proyecto, Python permite modificarlo fácilmente sin tanto cambio ni recompilación.

En cambio, Java nos habría hecho el proyecto mucho más largo y con muchas más reglas.

## Funciones.
- Agregar empleados con nombre, identificador y salario a una lista.
- Buscar y eliminar un empleado en especifico de la lista.
- Ordenar los empleados de la lista, por nombre o salario, de forma ascendente o descendente.
- Calcular estadísticas básicas (como el promedio, máximo y mínimo...) sobre el salario.
- Imprimir la lista con los cambios realizados sobre ella.

## Instrucciones de Uso.
1. Requisitos Previos: antes de ejecutar el programa, has de tener descargado Python 3 en tu sistema. Ejecuta este comando en consola para asegurarte de que Python está instalado:
    python3 --version
Si no tienes Python descargado, puedes ir a descargarlo desde la página oficial: Python.org

2. Descargar el Proyecto: para obtener el código, puedes descargar el archivo ZIP y extraerlo en tu computadora.

3. Ejecución del Programa: encuentra la carpeta del proyecto y ejecuta el archivo "*main.py*":

4. Uso del Menú Principal: una vez que el programa se ejecuta, habrá un menú con opciones para administrar empleados. El menú cuenta con sus opciones y números correspondientes, ingresa el número y presiona "Enter".
    - Opciones del menú:
    1. Insertar empleado: debes ingresar el nombre, identificador y salario del empleado. El nombre debe ser una cadena alfabética, el identificador un número entero único y el salario un número entero.
    2. Buscar empleado por identificador: ingresa un identificador y el programa te mostrará los datos del empleado, si es que este existe.
    3. Eliminar empleado por identificador: ingresa un identificador y el programa eliminará al empleado de la lista, si es que este existe.
    4. Ordenar empleados por nombre: puedes elegir un orden ascendente o descendente.
    5. Ordenar empleados por salario: puedes elegir un orden ascendente o descendente.
    6. Calculas estadísticas básicas del salario: muestra el promedio del salario, el salario máximo y mínimo y la mediana de todos los salarios.
    7. Mostrar lista de empleados: muestra todos los empleados registrados por el momento.
    8. Salir del programa: cortas la ejecución del programa.

5. Consideraciones:
    - Si ingresas un dato incorrecto, el programa mostrará un mensaje de error y te pedirá que ingreses la información nuevamente.
    - El programa usa una lista doblemente enlazada para gestionar los empleados, esto lo hace mucho más eficiente.
    - Puedes modificar el código en "*PruebasIniciales.py*" para agregar nuevas funcionalidades.
    - El programa no detecta identificadores duplicados: ¡TENER CUIDADO CON ELLO!

## Tecnologías Utilizadas.
* Lenguaje: Python.
* Editor recomendado: Visual Studio Code.

## Estructura del Proyecto.
Actividad empresa/
|--- documentacion.txt
|--- PruebasIniciales.py
|--- main.py
|--- README.md

## Desarrollado Por:
- Julian Amariles.
- Natalya Contreras.