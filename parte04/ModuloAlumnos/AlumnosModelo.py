from ModuloPrincipal.config import db

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    calificacion = db.Column(db.Integer)

    def __repr__(self):
        return '<Alumno %r>' % self.nombre
