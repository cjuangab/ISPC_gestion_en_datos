#CRUD

SELECT idlaboratorio FROM inventario_ipet251.laboratorio;
SELECT idlaboratorio, nombre, cantidad_alumnos, metros_cuadrados FROM inventario_ipet251.laboratorio;
INSERT INTO laboratorio (idlaboratorio, nombre, cantidad_alumnos, metros_cuadrados) VALUES
('6', 'termodinamica', '40','38'),
('7','carpinteria','23','19'),
('8','metalurgica','18','20');

UPDATE laboratorio SET nombre = 'quimca' WHERE idlaboratorio=8;
UPDATE laboratorio SET nombre='instrumental' WHERE idlaboratorio=6;

DELETE FROM laboratorio WHERE idlaboratorio=6;
DELETE FROM laboratorio WHERE idlaboratorio=7;
DELETE FROM laboratorio WHERE idlaboratorio=8;

