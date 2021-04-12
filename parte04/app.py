from ModuloPrincipal.config import app, db
from ModuloAlumnos.Alumnos import alumnos_modulo


app.register_blueprint(alumnos_modulo)

if __name__ == '__main__':
    db.create_all()
    app.run(port=3000, debug=True)