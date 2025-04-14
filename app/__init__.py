# app/__init__.py
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_session'
    
# No importes las rutas aquí para evitar importaciones circulares
from app import routes