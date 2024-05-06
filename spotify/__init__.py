from flask import Flask, render_template, send_file

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/cantantes')
def cantantes():
    base_de_datos = db.get_db
    consulta = """
         SELECT Name FROM artists
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("cantantes.html", cantantes=lista_de_resultados) 