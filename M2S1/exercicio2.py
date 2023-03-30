CREATE TABLE cliente(
	ID int NOT NULL,
	NOME varchar(80),
	CPF varchar(11),
	DATA_CADASTRO text DEFAULT CURRENT_TIMESTAMP,
	ENDERECO varchar(80),
	PRIMARY KEY(Id)
);

insert into cliente values(1, "Caio", "12345678910", "30/08/2020", "PARQUE TIETÊ");

select * from cliente;