from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

alumnos = []

@app.route('/')
def index():
    return render_template('index.html', alumnos=alumnos)

@app.route('/registro/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        email = request.form["email"]

        alumnos.append({"nombre":nombre, "email": email})

        return redirect(url_for('index'))

    return render_template('registro_alumno.html')

app.run(port=3000, debug=True)