use bdpagina;

CREATE TABLE Material
(
idMaterial int primary key not null,
Material varchar (50),
Waterproof boolean,
Heatproof boolean

);

CREATE TABLE Cliente
(IdCliente int primary key,
Nombres varchar(50) not null,
Email varchar(50),
Telefono int(16),
Direccion varchar(50)
);
