from flask import Blueprint, render_template, redirect, request, url_for
from .FormularioAlumnos import FormularioAlumnos
from .AlumnosModelo import Alumno
from ModuloPrincipal.config import db

alumnos_modulo = Blueprint('alumno_bp', __name__, template_folder='templates')

@alumnos_modulo.route('/')
def index():
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)

@alumnos_modulo.route('/registro/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        
        formulario = FormularioAlumnos(request.form)

        alumno = Alumno(
            nombre = formulario.nombre.data,
            calificacion=formulario.calificacion.data,
            email=formulario.email.data,
        )

        db.session.add(alumno)
        db.session.commit()

        return redirect(url_for('alumno_bp.index'))
    else:
        formulario = FormularioAlumnos()
    return render_template('registro_alumno.html', formulario=formulario)
