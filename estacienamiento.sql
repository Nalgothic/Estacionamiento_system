create database estacionamiento;
use estacionamiento;
create table vehiculos(
    n_operacion int not null auto_increment,
    cochera int not null,
    patente varchar (15) not null,
    hora_ingreso float not null,
    fecha_ingreso date not null,
    hora_egreso float (15) not null,
    fecha_egreso date not null,
    medio_pago varchar(15)not null,
    primary key (n_operacion));
    