from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from config import Config
from models import db, Tarea

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap5(app)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_tarea():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        
        nueva_tarea = Tarea(nombre=nombre, descripcion=descripcion)
        db.session.add(nueva_tarea)
        db.session.commit()
        
        return redirect(url_for('index'))
    return render_template('agregar_tarea.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    if request.method == 'POST':
        tarea.nombre = request.form['nombre']
        tarea.descripcion = request.form['descripcion']
        
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_tarea.html', tarea=tarea)

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)