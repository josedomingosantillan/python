create database libreria;

use libreria;

create table cat_idioma(
id int primary key auto_increment,
nombre varchar(50),
descripcion text
);

insert into cat_idioma values(null,'Español','Idioma nacional'),(null, 'Ingles','Idioma de Estados Unidos');

create table cat_genero(
id int primary key auto_increment,
nombre varchar(50),
descripcion text,
clasificacion varchar(5)
);

insert into cat_genero values (null,'Educativo','Libro institucional','A'),
(null,'Terror','Libro de Terror','C'),
(null,'Romantico','Libro de Amor','A'),
(null,'Ficción','Libro Ciencia Ficción','A');

create table cat_editorial(
id int primary key auto_increment,
nombre varchar(50),
direccion text,
telefono varchar(10)
);

insert into cat_editorial values (null,'Porrua', 'Ciudad de México','5930245867'),
(null,'Portalibros', 'Ciudad de México','5934565867'),(null,'Lectores', 'Ciudad de México','5930245767'),
(null,'Mas libros', 'Ciudad de México','9307655867'),(null,'Libreros', 'Ciudad de México','1030245867');

create table libro(
id int primary key auto_increment,
nombre varchar(50),
id_idioma int,
id_genero int,
id_editorial int,
precio double not null,
existencia int not null
);

ALTER TABLE libro
ADD CONSTRAINT fk_idioma FOREIGN KEY (id_idioma) REFERENCES cat_idioma(id),
ADD CONSTRAINT fk_genero FOREIGN KEY (id_genero) REFERENCES cat_genero(id),
ADD CONSTRAINT fk_editorial FOREIGN KEY (id_editorial) REFERENCES cat_editorial(id);

INSERT INTO libro (nombre, id_idioma, id_genero, id_editorial, precio, existencia)
VALUES 
    ('Harry Potter y la piedra filosofal', 1, 4, 1, 25.99, 50),
    ('Cien años de soledad', 1, 3, 2, 30.50, 30),
    ('Drácula', 2, 2, 3, 18.75, 20),
    ('Orgullo y prejuicio', 1, 3, 4, 22.95, 45),
    ('1984', 2, 4, 5, 15.99, 60);

