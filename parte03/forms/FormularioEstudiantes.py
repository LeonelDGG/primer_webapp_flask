from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import IntegerField, EmailField
from wtforms.widgets.html5 import NumberInput 

class FormularioEstudiantes(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    calificacion = IntegerField('Calificacion', validators=[DataRequired()], widget=NumberInput(min=0, max=10, step=1))
    email = EmailField('Direccion de correo electronico', validators=[DataRequired()])
    submit = SubmitField('Registrar')