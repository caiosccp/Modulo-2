create table categoria(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	descricao varchar(25)
);

Create Table TODO(
	id INTEGER NOT NULL PRIMARY KEY,
	descricao varchar(150),
	categoria_id NOT NULL,
	dataEvento TEXT,
	isConcluido INTEGER,
	CONSTRAINT todo_fk FOREIGN KEY (categoria_id) references categoria(id)
);