import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS local(
id INTEGER primary key AUTOINCREMENT, 
latitude INTEGER NOT NULL,
longitude INTEGER NOT NULL,
descricao_local varchar(255) NOT NULL
);

              ''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS amostra (
codigo INTEGER PRIMARY KEY AUTOINCREMENT,
data INTEGER NOT NULL,
descricao VARCHAR(250) NOT NULL,
temperatura INTEGER,
ph REAL,
condutividade REAL,
turbidez REAL,
acidez REAL,
alcalinidade_parcial REAL,
alcalinidade_total REAL,
alcalinidade_bicarbonato REAL,
alcalinidade_cabonato REAL,
alcalinidade_hidroxila REAL,
local_id INTEGER NO NULL,
FOREIGN KEY(local_id) REFERENCES local(id)
);

''')
conn.commit()
conn.close()




