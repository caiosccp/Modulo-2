import sqlite3

conexao = sqlite3.connect("m2s2_ex1")
cursor = conexao.cursor()

cursor.execute(f"CREATE TABLE Categoria(id INT NOT NULL, nome VARCHAR(50), PRIMARY KEY (id) );")
cursor.execute(f"CREATE TABLE Tarefa(id INT NOT NULL, nome VARCHAR(100), data VARCHAR(100), status BOOL, categoria_id INT NOT NULL, PRIMARY KEY (id), FOREIGN KEY (categoria_id) REFERENCES Categoria(id));")

conexao.commit()
                
conexao.close()