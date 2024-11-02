# ISPC_gestion_en_datos

Trabajamos creando un inventario para el IPET 251 en donde lo que se busca es que solucionar el problema de  la falta de trazabilidad de los elementos y materiales empleados en las actividades educativas. 

En el programa van a encontrar que cuando se ejecuta se va a visualiar un menu con las siguientes opciones: Ingresar (al sistema), crear usuario, modificar usuario, eliminar usuario,buscar usuario, mostrar todos los usuarios, salir. 

El programa se ejecuta desde el archivo menu.py, en el cual aparece por consola un menu interactivo que nos permite hacer un CRUD e ingresar al sistema.
Dicho CRUD de usuarios no almacena informacion en la BDD sino que lo hace de forma persistente en un archivo binario de extension .ispc

A continuacion detallaremos su operacion:
Al ejecutar el archivo menu.py nos figura por consola 7 opciones:
Crear usuario
Ingresar (al sistema)
Modificar Usuario
Eliminar Usuario
Buscar Usuario
Mostrar todos los usuarios
Salir

Crear usuario
Al ejecutar esta opcion nos permitira crear un usuario solicitandonos un ID, un nombre de usuario, una contraseña y un email

Ingresar al sistema
Nos permitira ingresar a el software solicitandonos un usuario y contraseña

Modificar Usuario
Nos permite modificar un usuario existente almacenado en el archivo usuarios.ispc

Eliminar usuario
Nos permite Eliminar un usuario existente almacenado en el archivo usuarios.ispc

Buscar Usuario
Nos permite buscar un usuario existente almacenado en el archivo usuarios.ispc

**Búsqueda secuencial:** Si los usuarios no han sido ordenados previamente.

**Búsqueda binaria:** Si los usuarios se han ordenado previamente usando alguna de las opciones de ordenamiento disponibles.

Mostrar todos los usuarios
Nos muestra por consolas todos los usuarios existentes almacenados en el archivo usuarios.ispc

Opciones de ordenamiento de usuarios
Esta opción permite ordenar los usuarios almacenados en el archivo `usuarios.ispc` según su `username`, utilizando dos métodos diferentes:

Salir
Por ultimo esta opcion nos permite salir del programa 

En primera instancia el usuario (docente de cada laboratorio) podra acceder a un menu en donde podra:

Visualizar los elementos disponibles
Agregar un recurso nuevo
Modificar un recurso existente
A su vez estas opciones le permitiran al usuario Elegir entre:

Informaticos
Equipamiento
Herramental
Insumos
Al visualizar solamente podra obtener informacion de todos los elementos o de algun elemento en particular, como su estado, su asignacion, su cantidad, etc.

Al agregar le permitira al usuario agregar un elemento nuevo a la base de datos

Y al modificar le permitira modificar alguno de los elementos existentes e incluso eliminarlos (para esto ultimo la intencion es crear usuarios con mayores credenciales que podrian ser un director o jefe de taller, para que solos ellos puedan dar de baja un elemento de la base de datos, para evitar las perdidas de los registros de los mismos)

MODULOS QUE LO INTEGRAN
index: Modulo principal o index nucleo del programa
Bienvenida: Modulo que integra las funciones de bienvenida y despedida del programa
Menus: Modulo que integra la funcionalidad del menu principal
Visualizacion: Modulo que integra las funciones correspondiente a visualisar elementos de la Base de datos
Agregar: Modulo que integra las funciones correspondietes al agregado de elementos a la Base de datos
Login: Modulo que integra las funciones correspondientes a el login de usuarios
Modificar: Modulo que integra las funciones correspondientes a la modificacion de los elementos de la Base de Datos
Inventario_IPET.py
Conector: modulo que conecta python con la base de datos
Users: maneja la clase usuario y la conexion con los archivos binarios

Se importan los modulos de Menus.py Bienvenida.py y modulos propios de Python como lo son os.py y time.py

Importamos la funcion sleep(tiempo_en_segundos) para hacer un standby en la ejecucion lo suficiente como para leer mensajes importantes

Y a la funcion system("cls") la utilizamos para limpiar la consola y dar una imagen mas limpia.

Estas dos funciones integradas las utilizamos a lo largo de todos los modulos

Bienvenida.py
Este modulo integra tres modulos que son sustancialmente similares entre ellas

bienvenida()
bienvenida_prof(prof)
cierre(prof)
bienvenida()
Esta funcion integra una serie de print() para dar un mensaje de bienvenida, con el nombre de la institucion

bienvenida_prof(prof)
Esta funcion integra una serie de print() para dar un mensaje de bienvenida, solicita por parametro el ingreso de un string para dar un mensaje de bienvenida personalizado al profesor

cierre(prof)
Esta funcion integra una serie de print() para dar un mensaje de despedida, solicita por parametro el ingreso de un string para dar un mensaje de despedida personalizado al profesor

Menus.py
Defina una sola funcion

menu_principal():

Esta funcion no retorna ni requiere ningun parametro para ejecutarse, simplemente integra informacion de opciones que el usuario puede tomar las cuales son:

Visualizar Elementos de Su laboratorio.
Agregar Elementos a su laboratorio.
Modificar Elementos de su laboratorio.
Salir
Seguido a esto se le pide al usuario que elija una opcion por consola y un condicional match-case toma diferentes acciones en base a la opcion elegida

Se llama a la funcion importada visualizar_elementos()
Se llama a la funcion importada agregado()
Se muestra por consola un mensaje (por ahora)
Cierra el programa
En caso de que se seleccione alguna opcion no correcta (numerica) el programa hará un manejo de excepciones, para  asi evitar que se detenga el programa en caso de colocar una opcion incorrecta

visualizacion.py
En este modulo estan definidas las funciones

visualizar_elementounico()
visualizar_info(tipo)
listado_completo(tipo)
delay()
Dentro del modulo importamos el modulo Menus.py y de los modulos random.py a randint() y de os.py a system("cls")

visualizar_elementos()
Funcion que no requiere parametros en el argumento, esta funcion cumple la tarea de un sub menu dedicada a mostrar elementos almacenados en la base de datos.

Su operacion es similar a la funcion menu_principal del modulo Menus.py

Se le muestran opciones al usuario y un match-case toma desiciones en base a esta opcion:
Recursos Informaticos
Herramental
Equipamiento
Insumos
Menu Principal (esta opcion es la 0)
Para los cuatro primeros casos llama a la funcion visualizar_info() ingresando por argumento un string con el tipo de recurso a visualizar, para la quinta opcion retorna a el menu principal a traves de la funcion menu_principal(), en el caso que no se ingrese ningun valor numerico coincidente muestra mensaje de "opcion incorrecta" y retorna a inicio de la funcion (aun se trabaja para el caso de ingresar un caracter de otro tipo)

visualizar_info(tipo)
Esta funcion requiere un string como argumento, nos presenta un sub menu con tres opciones las cuales son:
Listado completo
Elemento unico
Volver atras
En listado completo llama a la funcion listado_completo() y le pasa por argumento el tipo que le pasamos por agumento a la funcion visualizar_info(), terminada esta llama a la funcion delay() que espera al usuario hasta que aprieta la tecla ENTER
En la segunda opcion de Elemento unico la funcion le pide al usuario el id del elemento a mostar. Por ultimo le permite al usuario volver al menu anterior a travez de la funcion visualizar_elementos()

Agregar.py
Este modulo es un modulo ligado a la Base de datos el cual debe tener como principal funcion el agregado o alta de recursos en esta (instancias de las entidades)
Define 5 funciones
agregado()
ag_info()
ag_herr()
ag_eq()
ag_ins()
agregado()
Funcion que no requiere parametros en el argumento, esta funcion cumple la tarea de un sub menu dedicada a agregar elementos a la base de datos.

Su operacion es similar a la funcion menu_principal del modulo Menus.py. Se le muestran opciones al usuario y un match-case toma desiciones en base a esta opcion:
Recursos Informaticos
Herramental
Equipamiento
Insumos
Menu Principal (esta opcion es la 0)
Para cada caso la funcion llama a las funciones ag_info() ag_herr() ag_eq() ag_ins() las cuales son las encargadas de agregar los elementos correspondientes a la Base de datos

Para el ultimo caso retona al menu principal a partir de la funcion Menus.menu_principal

Para cualquier otro caso numerico la funcion repite la funcion agregado() junto con un mensaje de opcion invalida (aun en desarrollo en caso que el usuario ingrese letra o algun otro)

ag_info() ag_herr() ag_eq() ag_ins()
Estas funciones, trabajan de manera similiar, solamente que cada una especificamente para cada tipo de elemento a agregar, dado que unos tiene atributos diferentes a los demas, son funciones vinculativas a la Base de datos.

Modificar.py
Este modulo estaria ligado a la base de datos y nos permitiria modificar o eliminar recursos del inventario de la base de datos.

Integra dos funciones:
modificacion()
consulta()
Funcion que no requiere parametros en el argumento, esta funcion cumple la tarea de un sub menu dedicada a agregar elementos a la base de datos.

Su operacion es similar a la funcion menu_principal del modulo Menus.py

Se le muestran opciones al usuario y un match-case toma desiciones en base a esta opcion:

Recursos Informaticos
Herramental
Equipamiento
Insumos
Menu Principal (esta opcion es la 0)
Para los cuatro primeros casos llama a la funcion consulta() ingresando por argumento un string con el tipo de recurso a visualizar, para la quinta opcion retorna a el menu principal a traves de la funcion menu_principal(), en el caso que no se ingrese ningun valor numerico coincidente muestra mensaje de "opcion incorrecta" y retorna a inicio de la funcion 
consulta(tipo)

Funcion asociada a la base de datos, estaria encargada de modificar o eliminar, actualmente esta integrada por un match-case con tres opciones

Modificiar
Eliminar
Volver atras





