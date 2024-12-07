import sqlite3


conn = sqlite3.connect('gestao_tarefas.db')

conn.execute('PRAGMA foreign_keys = ON')

cursor = conn.cursor()

cursor.execute('''
INSERT INTO usuario (id_usuario, nome_usuario)
VALUES (?, ?)
''', (3, 'João Almeida'))

cursor.execute('''
INSERT INTO tarefa (id_tarefa, nome_tarefa, id_usuario)
VALUES (?, ?, ?)
''', (3, 'Trabalho Banco de Dados', 3))

conn.commit()


conn.close()