import sqlite3

conexao = sqlite3.connect("m2s2_ex2.sqlite3")
cursor = conexao.cursor()

cursor.execute(f"CREATE TABLE Organizador( id INT NOT NULL, nome VARCHAR(50), email VARCHAR(50), cpf VARCHAR(50), PRIMARY KEY (id));")
cursor.execute(f"CREATE TABLE Evento(id INT NOT NULL, titulo VARCHAR(100), data VARCHAR(100), local VARCHAR(100), PRIMARY KEY (id));")
cursor.execute(f"CREATE TABLE organizador_evento(organizador_id INT NOT NULL, evento_id INT NOT NULL, FOREIGN KEY (organizador_id) REFERENCES Organizador(id), FOREIGN KEY (evento_id) REFERENCES Evento(id), CONSTRAINT pk_org_event PRIMARY KEY (organizador_id, evento_id));")

conexao.commit()
conexao.close()