CREATE TABLE IF NOT EXISTS local(
id INTEGER primary key AUTOINCREMENT, 
latitude INTEGER NOT NULL,
longitude INTEGER NOT NULL,
descricao local varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS amostra (
id INTEGER PRIMARY KEY AUTOINCREMENT,
data INTEGER NOT NULL,
descricao VARCHAR(250) NOT NULL,
temperatura INTEGER,
ph REAL,
condutividade REAL,
turbidez REAL,
acidez REAL,
alcalinidade_parcial VARCHAR(300),
alcalinidade_total REAL,
);

SELECT * FROM amostra;

