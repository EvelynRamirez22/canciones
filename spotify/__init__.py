from flask import Flask, render_template, send_file

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

from . import cantante
app.register_blueprint(cantante.bp)

@app.route('/canciones')
def canciones():
    base_de_datos = db.get_db()
    consulta = """
         SELECT name FROM tracks
         ORDER BY name ASC
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("canciones.html", canciones=lista_de_resultados) 
