# application/sesion/routes.py

from flask import render_template
from database import mysql
from . import sesion

@sesion.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()

    #print(data)

    return render_template('index.html')