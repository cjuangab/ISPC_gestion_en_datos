CREATE DATABASE IF NOT EXISTS `inventario_ipet251`;

-- -----------------------------------------------------
-- Table `inventario_ipet251`.`Laboratorio`
-- -----------------------------------------------------
USE `inventario_ipet251`;
CREATE TABLE IF NOT EXISTS `Laboratorio` (
  `idlaboratorio` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad_alumnos` INT NOT NULL,
  `metros_cuadrados` INT NOT NULL,
  PRIMARY KEY (`idlaboratorio`)
);

-- -----------------------------------------------------
-- Table `inventario_ipet251`.`Profesor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Profesor` (
  `dni` INT(9) NOT NULL,
  `nombre` VARCHAR(30) NOT NULL,
  `apellido` VARCHAR(30) NOT NULL,
  `mail` VARCHAR(45) NOT NULL,
  `Laboratorio_idlaboratorio` INT NOT NULL,
  PRIMARY KEY (`dni`),
  INDEX `fk_Profesor_Laboratorio1_idx` (`Laboratorio_idlaboratorio` ASC) VISIBLE,
  CONSTRAINT `fk_Profesor_Laboratorio1`
    FOREIGN KEY (`Laboratorio_idlaboratorio`)
    REFERENCES `Laboratorio` (`idlaboratorio`)
);

-- -----------------------------------------------------
-- Table `inventario_ipet251`.`Materia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Materia` (
  `idmateria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `programa` VARCHAR(45),
  `Profesor_dni` INT(9) NOT NULL,
  PRIMARY KEY (`idmateria`),
  INDEX `fk_Materia_Profesor_idx` (`Profesor_dni` ASC) VISIBLE,
  CONSTRAINT `fk_Materia_Profesor`
    FOREIGN KEY (`Profesor_dni`)
    REFERENCES `Profesor` (`dni`)
);

-- -----------------------------------------------------
-- Table `inventario_ipet251`.`Informaticos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Informaticos` (
  `idinformaticos` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45),
  `marca` VARCHAR(15),
  `modelo` VARCHAR(15),
  `n_serie` VARCHAR(25),
  `n_serie_sec` VARCHAR(25),
  `origen` VARCHAR(10),
  `estado` VARCHAR(10),
  `Laboratorio_idlaboratorio` INT NOT NULL,
  PRIMARY KEY (`idinformaticos`),
  INDEX `fk_Informaticos_Laboratorio1_idx` (`Laboratorio_idlaboratorio` ASC) VISIBLE,
  CONSTRAINT `fk_Informaticos_Laboratorio1`
    FOREIGN KEY (`Laboratorio_idlaboratorio`)
    REFERENCES `Laboratorio` (`idlaboratorio`)
);

-- -----------------------------------------------------
-- Table `inventario_ipet251`.`Equipamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Equipamiento` (
  `idEquipamiento` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45),
  `uso` VARCHAR(10),
  `marca` VARCHAR(10),
  `modelo` VARCHAR(15),
  `num_serie` VARCHAR(25),
  `descripcion` VARCHAR(45),
  `fecha_calibracion` DATETIME,
  `Laboratorio_idlaboratorio` INT NOT NULL,
  PRIMARY KEY (`idEquipamiento`),
  INDEX `fk_Equipamiento_Laboratorio1_idx` (`Laboratorio_idlaboratorio` ASC) VISIBLE,
  CONSTRAINT `fk_Equipamiento_Laboratorio1`
    FOREIGN KEY (`Laboratorio_idlaboratorio`)
    REFERENCES `Laboratorio` (`idlaboratorio`)
);

-- -----------------------------------------------------
-- Table `inventario_ipet251`.`Herramental`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Herramental` (
  `idHerramental` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45),
  `marca` VARCHAR(10),
  `modelo` VARCHAR(15),
  `num_serie` VARCHAR(25),
  `uso` VARCHAR(10),
  `estado` VARCHAR(10),
  `Laboratorio_idlaboratorio` INT NOT NULL,
  PRIMARY KEY (`idHerramental`),
  INDEX `fk_Herramental_Laboratorio1_idx` (`Laboratorio_idlaboratorio` ASC) VISIBLE,
  CONSTRAINT `fk_Herramental_Laboratorio1`
    FOREIGN KEY (`Laboratorio_idlaboratorio`)
    REFERENCES `Laboratorio` (`idlaboratorio`)
);

-- -----------------------------------------------------
-- Table `inventario_ipet251`.`Insumos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Insumos` (
  `idInsumos` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45),
  `marca` VARCHAR(15),
  `modelo` VARCHAR(15),
  `cantidad` INT,
  `unidad` VARCHAR(5),
  `origen` VARCHAR(15),
  `vencimiento` DATETIME,
  `estado` VARCHAR(15),
  `Laboratorio_idlaboratorio` INT NOT NULL,
  PRIMARY KEY (`idInsumos`),
  INDEX `fk_Insumos_Laboratorio1_idx` (`Laboratorio_idlaboratorio` ASC) VISIBLE,
  CONSTRAINT `fk_Insumos_Laboratorio1`
    FOREIGN KEY (`Laboratorio_idlaboratorio`)
    REFERENCES `Laboratorio` (`idlaboratorio`)
);

INSERT INTO laboratorio VALUES
('1','electronica', '30', '25'),
('2','mecanica', '24', '30'),
('3', 'estructuras', '10', '30'),
('4', 'tecnologia de los materiales', '18', '40'),
('5', 'fisica', '38', '42');

SELECT * FROM inventario_ipet251.profesor;
INSERT INTO profesor VALUES
('123456','Agustin', 'Bracamonte', 'agustinbracamonte@gmail.com','4'),
('234567','Maria', 'Serrezuela', 'mariaserrezuela','3'),
('345678', 'Gustavo', 'Berni', 'gustavoberni@gail.com','2'),
('456789', 'Teresa', 'Calo', 'teresacalo@gmail.com', '5'),
('567890', 'Gaston', 'Bermudes', 'gastonbermudes@gmail.com','1');

SELECT * FROM inventario_ipet251.materia;
INSERT INTO materia (idmateria, nombre, profesor_dni) VALUES
('1','electronica','567890'),
('2','mecanica','345678'),
('3', 'estructuras','234567'),
('4', 'tecnologia de los materiales','123456'),
('5', 'fisica','456789');

INSERT INTO insumos (idinsumos, tipo, marca, cantidad, unidad, vencimiento, laboratorio_idlaboratorio) VALUES
('1','cable','cab','5','m','2050-10-8','1'),
('2','estaño','generico','12','kg','2035-1-3','3'),
('3', 'filamentos','hellbot','25','kg','2026-5-9','4'),
('4', 'caños de pvc','generico','34','m','2047-2-7','5'),
('5', 'lijas','xc','19','m','2028-9-6','2');

INSERT INTO informaticos (idinformaticos, tipo, marca, n_serie,laboratorio_idlaboratorio) VALUES
('1','notebook','dell','1234','1'),
('2','impresora 3d','hellbot','2345','3'),
('3', 'impresora resina 3d','hellbot','2567','4'),
('4', 'notebook','dell','3478','5'),
('5', 'proyector','xc','6591','2');

INSERT INTO herramental (idHerramental, tipo, marca, num_serie, uso, estado, laboratorio_idlaboratorio) VALUES
('1','destornillador','des','1234','manual','e_s','1'),
('2','calibre','ibre','2345','manual','e_s','3'),
('3', 'torquimetro','toq','2567','manual','e_s','4'),
('4', 'amperimetro','amp','3478','manual','f_d_s','5'),
('5', 'moladora','mdl','6591','electrico','e_s','2');

INSERT INTO equipamiento (idEquipamiento, tipo, uso, marca, laboratorio_idlaboratorio) VALUES
('1','multimetro','manual','mlt','1'),
('2','fuente de alimentacion v','manual','ftv','3'),
('3', 'multimetro','manual','eot','4'),
('4', 'termometro laser','manual','tls','5'),
('5', 'estacion de soldadura','electrico','sde','2');






