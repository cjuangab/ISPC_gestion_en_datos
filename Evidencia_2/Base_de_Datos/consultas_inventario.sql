#INNER JOIN 

SELECT laboratorio.idlaboratorio, laboratorio.nombre,profesor.nombre, profesor.apellido
FROM laboratorio 
INNER JOIN profesor
ON laboratorio.idlaboratorio = profesor.Laboratorio_idlaboratorio;


SELECT laboratorio.idlaboratorio, laboratorio.nombre, herramental.tipo, herramental.uso
FROM laboratorio 
INNER JOIN herramental
ON laboratorio.idlaboratorio = herramental.Laboratorio_idlaboratorio;

SELECT laboratorio.idlaboratorio, laboratorio.nombre, herramental.tipo, herramental.uso
FROM laboratorio 
RIGHT JOIN herramental
ON laboratorio.idlaboratorio = herramental.Laboratorio_idlaboratorio;
