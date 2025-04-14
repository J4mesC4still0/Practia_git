# app/routes.py
from flask import render_template, request, redirect, url_for, session
from app import app

# Datos de ejemplo para cursos (almacenamiento en memoria por ahora)
cursos = [
    {
        'id': 1,
        'titulo': 'Introducción a Python',
        'descripcion': 'Aprende los fundamentos del lenguaje de programación Python',
        'instructor': 'Gunar Castro Iñigo',
        'duracion': '8 semanas',
        'imagen': 'https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python.png',
        'categoria': 'programacion'
    },
    {
        'id': 2,
        'titulo': 'Desarrollo Web con Flask',
        'descripcion': 'Construye aplicaciones web utilizando el framework Flask',
        'instructor': 'Gunar Castro Iñigo',
        'duracion': '10 semanas',
        'imagen': 'https://cdn.jsdelivr.net/npm/programming-languages-logos/src/html/html.png',
        'categoria': 'programacion'
    },
    {
        'id': 3,
        'titulo': 'JavaScript Avanzado',
        'descripcion': 'Domina JavaScript para el desarrollo front-end',
        'instructor': 'Gunar Castro Iñigo',
        'duracion': '6 semanas',
        'imagen': 'https://cdn.jsdelivr.net/npm/programming-languages-logos/src/javascript/javascript.png',
        'categoria': 'programacion'
    },
    {
        'id': 4,
        'titulo': 'Adobe Photoshop: Nivel Principiante',
        'descripcion': 'Aprende a utilizar las herramientas básicas de Photoshop',
        'instructor': 'Gunar Castro Iñigo',
        'duracion': '4 semanas',
        'imagen': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-plain.svg',
        'categoria': 'diseno'
    },
    {
        'id': 5,
        'titulo': 'Diseño de Logotipos con Illustrator',
        'descripcion': 'Crea logotipos profesionales con Adobe Illustrator',
        'instructor': 'Gunar Castro Iñigo',
        'duracion': '5 semanas',
        'imagen': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/illustrator/illustrator-plain.svg',
        'categoria': 'diseno'
    },
    {
        'id': 6,
        'titulo': 'Fundamentos de UX/UI Design',
        'descripcion': 'Aprende los principios de diseño de experiencia e interfaz de usuario',
        'instructor': 'Gunar Castro Iñigo',
        'duracion': '7 semanas',
        'imagen': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg',
        'categoria': 'diseno'
    }
]

# Usuarios de ejemplo (solo para demostración)
usuarios = {
    'admin@ejemplo.com': {'password': 'admin123', 'rol': 'admin'},
    'estudiante@ejemplo.com': {'password': 'estudiante123', 'rol': 'estudiante'}
}

@app.route('/')
def inicio():
    return render_template('index.html', cursos=cursos[:3])

@app.route('/cursos')
def ver_cursos():
    categoria = request.args.get('categoria', '')
    if categoria:
        cursos_filtrados = [c for c in cursos if c['categoria'] == categoria]
    else:
        cursos_filtrados = cursos
    return render_template('cursos.html', cursos=cursos_filtrados, categoria=categoria)

@app.route('/curso/<int:curso_id>')
def detalle_curso(curso_id):
    curso = next((c for c in cursos if c['id'] == curso_id), None)
    if curso:
        return render_template('detalle_curso.html', curso=curso)
    return redirect(url_for('ver_cursos'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email in usuarios and usuarios[email]['password'] == password:
            session['conectado'] = True
            session['email_usuario'] = email
            session['rol'] = usuarios[email]['rol']
            return redirect(url_for('inicio'))
        else:
            error = 'Credenciales inválidas. Por favor, inténtelo de nuevo.'
    
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('conectado', None)
    session.pop('email_usuario', None)
    session.pop('rol', None)
    return redirect(url_for('inicio'))