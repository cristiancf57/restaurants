import sqlite3
conn = sqlite3.connect('restaurante.db')

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

print('\nPEDIDOS DETALLADOS')
cursor = conn.execute('''
    SELECT Pedidos.id, Platos.nombre AS nombre,Platos.precio AS precio,Platos.imagen AS imagen,Mesas.numero AS mesa,cantidad,cliente,fecha 
    FROM pedidos
    JOIN Platos ON Pedidos.plato_id = Platos.id 
    JOIN Mesas ON mesa_id = Mesas.id
    ''')
for row in cursor:
    print(row)
