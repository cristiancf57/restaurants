import sqlite3
conn = sqlite3.connect('restaurante.db')

conn.execute( '''
CREATE TABLE IF NOT EXISTS Platos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    imagen TEXT NOT NULL
)
''' )

conn.execute( '''
CREATE TABLE IF NOT EXISTS Mesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero INTEGER NOT NULL,
    nombre TEXT NOT NULL
)
''' )

conn.execute( '''
CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    cliente TEXT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY(plato_id) REFERENCES Platos(id),
    FOREIGN KEY(mesa_id) REFERENCES Mesas(id)
)
''' )

platos = [
    ('Fricase', 25.50, 'Fricase.jpg'),
    ('Picana navideña', 30.00, 'picana.jpg'),
    ('Fritanga', 25.50, 'fritanga.jpg'),
    ('Pique macho', 35.0, 'pique.jpg'),
    ('Silpancho', 22.50, 'silpancho.jpg')
]
conn.executemany('INSERT INTO Platos (nombre, precio, imagen) VALUES (?, ?, ?)', platos)

mesas = [
    (1,'Uno'),
    (2,'Dos'),
    (3,'Tres'),
    (4,'Cuatro'),
    (5,'Cinco')
]
conn.executemany('INSERT INTO Mesas (numero, nombre) VALUES (?, ?)', mesas)

pedidos = [
    (1, 1, 7, 'Medina', '2024-11-01'),
    (2, 2, 1, 'Castro', '2024-11-01'),
    (3, 3, 3, 'Quispe', '2024-11-02'),
    (4, 4, 5, 'Mendoza', '2024-11-02'),
    (1, 3, 2, 'Churata', '2024-11-02'),
    (3, 1, 2, 'Flores', '2024-11-02'),
    (3, 4, 6, 'Rojas', '2024-11-02'),
    (5, 3, 1, 'Alanoca', '2024-11-03'),
    (1, 5, 2, 'Torrez', '2024-11-03')
]
conn.executemany('INSERT INTO Pedidos (plato_id, mesa_id, cantidad, cliente, fecha) VALUES (?, ?, ?, ?, ?)', pedidos)

conn.commit()

print('\nPLATOS')
cursor = conn.execute('SELECT * FROM platos')
for row in cursor:
    print(row)

print('\nMESAS')
cursor = conn.execute('SELECT * FROM mesas')
for row in cursor:
    print(row)

print('\nPEDIDOS')
cursor = conn.execute('SELECT * FROM pedidos')
for row in cursor:
    print(row)