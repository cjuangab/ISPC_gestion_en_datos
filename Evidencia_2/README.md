# **Evidencia 2**

Trabajamos de forma conjunta donde debido a los tiempos realizamos una division de tareas donde uno trabajo enfocado a la base de datos mientras que otro trabajo dandole funcionalidad POO y aplicando la interaccion con archivos

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

#### Crear usuario

Al ejecutar esta opcion nos permitira crear un usuario solicitandonos un ID, un nombre de usuario, una contraseña y un email

A futuro la idea es que el ID se genere de forma automatica y que los demas datos tengan verificaciones


#### Ingresar al sistema

Nos permitira ingresar a el software solicitandonos un usuario y contraseña


#### Modificar Usuario

Nos permite modificar un usuario existente almacenado en el archivo usuarios.ispc


#### Eliminar usuario

Nos permite Eliminar un usuario existente almacenado en el archivo usuarios.ispc


#### Buscar Usuario

Nos permite buscar un usuario existente almacenado en el archivo usuarios.ispc


#### Mostrar todos los usuarios

Nos muestra por consolas todos los usuarios existentes almacenados en el archivo usuarios.ispc


#### Salir

Por ultimo esta opcion nos permite salir del programa



#### Inconvenientes a la hora de cumplimentar la evidencia

Principalmente tuvimos complicaciones con hacer funcionar la coneccion con la lectura de los archivos, mas precisamente en la escritura de nuevos elementos, ya que se sobreescribia el archivo existente y perdiamos la informacion previamente guardada, logramos subsanar este contrapie leyendo el archivo y almacenandolo en una lista a la cual le realizabamos las modificaciones pertinentes y luegamente esta lista que contenia la informacion existente en el archivo mas la nueva informacion era cargado en el archivo y al sobre escribir no perdiamos informacion ya que estaba ya integrada en la lista que cargabamos
