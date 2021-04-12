from flask import Flask, render_template, request, redirect, url_for
from forms.FormularioEstudiantes import FormularioEstudiantes
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'J5iRz4FDEJS7QnTZmadh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alumnos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    calificacion = db.Column(db.Integer)

    def __repr__(self):
        return '<Alumno %r>' % self.nombre



@app.route('/')
def index():
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)

@app.route('/registro/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        
        formulario = FormularioEstudiantes(request.form)

        alumno = Alumno(
            nombre = formulario.nombre.data,
            calificacion=formulario.calificacion.data,
            email=formulario.email.data,
        )

        db.session.add(alumno)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        formulario = FormularioEstudiantes()
    return render_template('registro_alumno.html', formulario=formulario)


if __name__ == '__main__':
    db.create_all()
    app.run(port=3000, debug=True)