from flask import Blueprint, app, render_template

from spotify import db


bp = Blueprint('cantantes',__name__,url_prefix='/cantantes') 

@app.route('/')
def cantantes():
    base_de_datos = db.get_db()
    consulta = """
         SELECT Name FROM artists
         ORDER BY Name ASC
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_de_cantantes = res.fetchall()
    pagina = render_template('cantantes.html', cantantes=lista_de_cantantes)

    return render_template("cantantes.html", cantantes=lista_de_cantantes) 

@app.route('<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
            SELECT name FROM artists WHERE ArtistId = ?
"""
    consulta2 = """
    SELECT al.Title FROM artists a JOIN albums al ON a.ArtistId = al.ArtistId
    WHERE a.ArtistId = ?;
"""

    res = con.execute(consulta1,(id,))
    cantantes = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_de_cantantes = res.fetchall()

    pagina = render_template('detalle_cantantes.html',
                             cantantes=cantantes,
                             cantantes = lista_de_cantantes)
    return pagina