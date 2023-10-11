# Serie: Mi primer Web App con Flask

El contenido de este repositorio, es de la serie "Mi primer Web App con Flask" escrita por mi.
En esta serie abarcamos lo basico de Flask, desde su instalacion hasta el desarrollo final de esta app.

Si estas interesado en leerla, te dejo el [link](https://dev.to/gareisdev/series/11860)

## Correr el proyecto

Mi recomendacion, es que crees un entorno virtual usando virtualenv o petry (el que mas te guste). Si no conoces ninguno, te dejo los links para que le des una leida (creeme que es de mucha utilidad):

+ [virtualenv](https://virtualenv.pypa.io/en/latest/)
+ [poetry](https://python-poetry.org/docs/)

### Instalar dependencias con virtualenv

```bash
virtualenv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```python
pip install -r requirements.txt
```

### Instalar dependencias con poetry

```bash
cat requirements.txt | xargs poetry add
```

### Iniciar el servidor

Elige una de las "partes" de la serie de tu interes y muevete dentro de ella.
Finalmente corre el siguiente comando:

```bash
python app.py
```
