from flask import Blueprint, request, render_template, redirect, url_for, flash, app, Flask

import numpy as np
from scipy.stats import chi2_contingency
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
app = Flask(__name__)
# Mysql Settings
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'sql9624432'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'BNMN2TSHZL'
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'sql9.freemysqlhosting.net'
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'sql9624432'
app.config['MYSQL_PORT'] = os.getenv('PORT') or 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)
# Application initializations


# settings
app.secret_key = "mysecretkey"



pacientes = Blueprint('pacientes', __name__,template_folder='app/templates')


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientes')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', pacientes=data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
