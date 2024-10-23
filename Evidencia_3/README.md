# Evidencia 3

Trabajamos de forma conjunta donde debido a los tiempos realizamos una division de tareas donde uno trabajo enfocado a la base de   datos mientras que otro trabajo dandole funcionalidad POO y aplicando la interaccion con archivos

El programa se ejecuta desde el archivo menu.py, en el cual aparece por consola un menu interactivo que nos permite hacer un CRUD e ingresar al sistema.

Dicho CRUD no almacena informacion en la BDD sino que lo hacer de forma persistente en un archivo binario de extension .ispc

A continuacion detallaremos su operacion:

Al ejecutar el archivo menu.py nos figura por consola 7 opciones:

1. Crear usuario
2. Ingresar (al sistema)
3. Modificar Usuario
4. Eliminar Usuario
5. Buscar Usuario
6. Mostrar todos los usuarios
7. Salir

### Crear usuario

Al ejecutar esta opcion nos permitira crear un usuario solicitandonos un ID, un nombre de usuario, una contraseña y un email

A futuro la idea es que el ID se genere de forma automatica y que los demas datos tengan verificaciones

### Ingresar al sistema

Nos permitira ingresar a el software solicitandonos un usuario y contraseña

### Modificar Usuario

Nos permite modificar un usuario existente almacenado en el archivo usuarios.ispc

### Eliminar usuario

Nos permite Eliminar un usuario existente almacenado en el archivo usuarios.ispc

### Buscar Usuario

Nos permite buscar un usuario existente almacenado en el archivo usuarios.ispc

- *\*Búsqueda secuencial:\*\* Si los usuarios no han sido ordenados previamente.

-  *\*Búsqueda binaria:\*\* Si los usuarios se han ordenado previamente usando alguna de las opciones de ordenamiento disponibles.

### Mostrar todos los usuarios

Nos muestra por consolas todos los usuarios existentes almacenados en el archivo usuarios.ispc


### Opciones de ordenamiento de usuarios

Esta opción permite ordenar los usuarios almacenados en el archivo \`usuarios.ispc\` según su \`username\`, utilizando dos métodos diferentes:

- **Técnicas propias**: Permite elegir entre diferentes algoritmos de ordenamiento como Bubble Sort, Selection Sort, Insertion Sort y Quick Sort. Los usuarios se ordenarán y se guardarán en el archivo si se selecciona esta opción.
- **Ordenamiento con Python:** Usa el método \`sort()\` de Python, utilizando \`key\` por \`username\`. Los usuarios se guardarán ordenados en el archivo \`usuarios.ispc\`.


### Cargar registros pluviales de un año

Permite gestionar registros pluviales anuales


### Salir

Por ultimo esta opcion nos permite salir del programa

## Inconvenientes a la hora de cumplimentar la evidencia

Debido a que estamos en proceso de mudanza contamos con una sola PC instalada actualmente, por lo que los commit los realizamos desde el mismo usuario, aunque en la practica trabajamos alternadamente para intentar cumplimentar las actividades.

Con respecto a los algoritmos de ordenamiento nos ayudamos con algoritmos de referencia de la catedra de introduccion a la informatica de la FCEFyN de la UNC
