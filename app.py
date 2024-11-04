from flask import Flask,request,session,redirect,render_template,jsonify
import sqlite3

app =Flask(__name__)

@app.route("/")
def menu():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Platos")
    platos = cursor.fetchall()
    conn.close()
    return render_template('index.html', platos = platos)

@app.route('/pedidos')
def pedidos():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor = conn.execute('''
    SELECT Pedidos.id, Platos.nombre AS nombre,Platos.precio AS precio,Platos.imagen AS imagen,Mesas.numero AS mesa,cantidad,cliente,fecha 
    FROM pedidos
    JOIN Platos ON Pedidos.plato_id = Platos.id 
    JOIN Mesas ON mesa_id = Mesas.id
    ''')
    pedido = cursor.fetchall()
    conn.close()
    return render_template('pedidos.html', pedido = pedido)



if __name__ == '__main__':
    app.run(debug=True)