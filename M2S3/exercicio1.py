import sqlite3

conexao = sqlite3.connect("m2s3_ex1.sqlite3")
cursor = conexao.cursor()

sql = """
CREATE TABLE fornecedor (
    id INT,
    nome VARCHAR(150) NOT NULL,
    endereco VARCHAR(150),
    produtos VARCHAR(20)
);"""
cursor.execute(sql)

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (1, 'Empresa de Leite ParmaLeite', 'Rua dos Leites, 23', 'leite');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (2, 'Peixaria Abril', 'Rua dos Leites, 25', 'peixe');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Açougue Legal', 'Rua dos Leites, 30', 'carnes');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Açougue Novo', 'Rua dos Leites, 35', 'carnes');

sql = "INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (?, ?, ?, ?);"
cursor.execute(sql, [3, "Padaria do Pão", "Rua dos Pães", "Pães"])
cursor.execute(sql, [4, "Marcenaria Martelo", "Rua dos Martelos", "Ferramentas"])

sql = """UPDATE fornecedor SET endereco = "Rua dos Peixes, 26" WHERE id = 2;"""
cursor.execute(sql)

sql = """SELECT * FROM fornecedor"""
data = cursor.execute(sql)

sql = """SELECT * FROM fornecedor WHERE produtos="Carnes";"""
data = cursor.execute(sql)

print("ANTES DO DELETE")
sql = """SELECT * FROM fornecedor"""
data = cursor.execute(sql)
for info in data:
    print(info)

sql = """DELETE FROM fornecedor WHERE id = 1;"""
cursor.execute(sql)

conexao.commit()
conexao.close()