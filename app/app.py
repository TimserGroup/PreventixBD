from flask import Blueprint, request, render_template, redirect, url_for, flash, Flask, make_response, session
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import chi2, norm, binom

from scipy.special import erfc
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
from io import BytesIO
from scipy.stats import norm

load_dotenv()

app = Flask(__name__, static_folder='assets')
app.secret_key = "mysecretkey"

# Mysql Settings
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'sql9624432'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'BNMN2TSHZL'
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'sql9.freemysqlhosting.net'
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'sql9624432'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)

pacientes = Blueprint('pacientes', __name__, template_folder='app/templates')

def check_login():
    try:
        logged = session['loggedin']
        return True
    except KeyError:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if check_login():
        return redirect(url_for('index'))
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        db = mysql.connection.cursor()
        db.execute("""SELECT id, username FROM Account 
                        WHERE username=\"{}\" AND password =\"{}\" """.format(username, password))
        account = db.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return redirect(url_for('index'))
        else:
            msg = "Usuario o contraseña incorrecto"
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not check_login():
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientes')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', pacientes=data)


@app.route('/addP', methods=['GET'])
def show_add_patient_form():
    return render_template('agregarPaciente.html')

# Ruta para procesar la solicitud de agregar paciente
@app.route('/add_paciente/', methods=['POST', 'GET'])
def add_paciente():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        PREVENTIX = request.form['PREVENTIX']
        RESULTADO_NUMERICO_PREVENTIX = request.form['RESULTADO_NUMERICO_PREVENTIX']
        Resultado_PCR_VPH = request.form['Resultado_PCR_VPH']
        RESULTADO_NUMERICO_VPH = request.form['RESULTADO_NUMERICO_VPH']
        Resultado_Papanicolaou = request.form['Resultado_Papanicolaou']
        ID = request.form['ID']
        RESULTADO_NUMERICO_PAP = request.form['RESULTADO_NUMERICO_PAP']
        Resultado_de_colposcopio = request.form['Resultado_de_colposcopio']
        resultado_numerico_colposcopia = request.form['resultado_numerico_colposcopia']
        Resultado_biopsia_de_cervix = request.form['Resultado_biopsia_de_cervix']
        Resultado_num_biopsia = request.form['Resultado_num_biopsia']

        try:
            cur = mysql.connection.cursor()
            cur.execute(
                'INSERT INTO pacientesdepurada (Nombre, PREVENTIX, RESULTADO_NUMERICO_PREVENTIX, Resultado_PCR_VPH, RESULTADO_NUMERICO_VPH, Resultado_Papanicolaou, ID, RESULTADO_NUMERICO_PAP, Resultado_de_colposcopio, resultado_numerico_colposcopia, Resultado_biopsia_de_cervix, Resultado_num_biopsia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (Nombre, PREVENTIX, RESULTADO_NUMERICO_PREVENTIX, Resultado_PCR_VPH, RESULTADO_NUMERICO_VPH, Resultado_Papanicolaou, ID, RESULTADO_NUMERICO_PAP, Resultado_de_colposcopio, resultado_numerico_colposcopia, Resultado_biopsia_de_cervix, Resultado_num_biopsia)
            )
            cur.connection.commit()
            flash('Paciente añadido correctamente')
            return redirect(url_for('show_add_patient_form'))
        except Exception as e:
            flash(str(e))
            return redirect(url_for('show_add_patient_form'))

    return render_template('agregarPaciente.html')

@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_paciente(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientesdepurada WHERE ID = %s', id)
    data = cur.fetchall()
    cur.close()
    print(data[0])

    return render_template('edit-patient.html', patient=data[0])


@app.route('/update/<int:id>', methods=['POST'])
def update_paciente(id):
    if request.method == 'POST':
        IDBD = request.form['IDBD']
        Nombre = request.form['Nombre']
        PREVENTIX = request.form['PREVENTIX']
        RESULTADO_NUMERICO_PREVENTIX = request.form['RESULTADO_NUMERICO_PREVENTIX']
        Resultado_PCR_VPH = request.form['Resultado_PCR_VPH']
        RESULTADO_NUMERICO_VPH = request.form['RESULTADO_NUMERICO_VPH']
        Resultado_Papanicolaou = request.form['Resultado_Papanicolaou']
        ID = request.form['ID']
        RESULTADO_NUMERICO_PAP = request.form['RESULTADO_NUMERICO_PAP']
        Resultado_de_colposcopio = request.form['Resultado_de_colposcopio']
        resultado_numerico_colposcopia = request.form['resultado_numerico_colposcopia']
        Resultado_biopsia_de_cervix = request.form['Resultado_biopsia_de_cervix']
        Resultado_num_biopsia = request.form['Resultado_num_biopsia']

        cur = mysql.connection.cursor()
        cur.execute('''
            UPDATE pacientesdepurada
            SET 
                IDBD = %(IDBD)s,
                Nombre = %(Nombre)s,
                PREVENTIX = %(PREVENTIX)s,
                RESULTADO_NUMERICO_PREVENTIX = %(RESULTADO_NUMERICO_PREVENTIX)s,
                Resultado_PCR_VPH = %(Resultado_PCR_VPH)s,
                RESULTADO_NUMERICO_VPH = %(RESULTADO_NUMERICO_VPH)s,
                Resultado_Papanicolaou = %(Resultado_Papanicolaou)s,
                ID = %(ID)s,
                RESULTADO_NUMERICO_PAP = %(RESULTADO_NUMERICO_PAP)s,
                Resultado_de_colposcopio = %(Resultado_de_colposcopio)s,
                resultado_numerico_colposcopia = %(resultado_numerico_colposcopia)s,
                Resultado_biopsia_de_cervix = %(Resultado_biopsia_de_cervix)s,
                Resultado_num_biopsia = %(Resultado_num_biopsia)s
            WHERE IDBD = %(id)s
        ''',
                    {
                        'IDBD': IDBD,
                        'Nombre': Nombre,
                        'PREVENTIX': PREVENTIX,
                        'RESULTADO_NUMERICO_PREVENTIX': RESULTADO_NUMERICO_PREVENTIX,
                        'Resultado_PCR_VPH': Resultado_PCR_VPH,
                        'RESULTADO_NUMERICO_VPH': RESULTADO_NUMERICO_VPH,
                        'Resultado_Papanicolaou': Resultado_Papanicolaou,
                        'ID': ID,
                        'RESULTADO_NUMERICO_PAP': RESULTADO_NUMERICO_PAP,
                        'Resultado_de_colposcopio': Resultado_de_colposcopio,
                        'resultado_numerico_colposcopia': resultado_numerico_colposcopia,
                        'Resultado_biopsia_de_cervix': Resultado_biopsia_de_cervix,
                        'Resultado_num_biopsia': Resultado_num_biopsia
                    })

        flash('Paciente actualizado correctamente')
        mysql.connection.commit()
        return redirect(url_for('pacientes.Index'))



@app.route('/busquedas', methods=['GET'])
def busquedas():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT COUNT(*) 
                    FROM pacientesdepurada
                    WHERE RESULTADO_NUMERICO_PREVENTIX = '101' AND RESULTADO_NUMERICO_PREVENTIX != '102' ''')
    dataPrevBiopsia = cur.fetchall()[0]['COUNT(*)']

    cur.execute('''SELECT COUNT(*) 
                        FROM pacientesdepurada
                        WHERE RESULTADO_NUMERICO_PREVENTIX = '101' AND Resultado_num_biopsia = '102' ''')
    dataPrevBiopsiaN = cur.fetchall()[0]['COUNT(*)']

    cur.execute('''SELECT COUNT(*) 
                        FROM pacientesdepurada
                        WHERE RESULTADO_NUMERICO_PREVENTIX = '101' AND Resultado_num_biopsia != '102' ''')
    dataPrevNBiopsia = cur.fetchall()[0]['COUNT(*)']

    cur.execute('''SELECT COUNT(*) 
                            FROM pacientesdepurada
                            WHERE RESULTADO_NUMERICO_PREVENTIX = '100' AND Resultado_biopsia_de_cervix = '102' ''')
    dataPrevNBiopsiaN = cur.fetchall()[0]['COUNT(*)']

    cur.close()
    return render_template('graficas.html', dataPrevNBiopsiaN=dataPrevNBiopsiaN, dataPrevNBiopsia=dataPrevNBiopsia,
                           dataPrevBiopsiaN=dataPrevBiopsiaN, dataPrevBiopsia=dataPrevBiopsia)


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_paciente(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM pacientesdepurada WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Paciente borrado correctamente')
    return redirect(url_for('index.html'))


@app.route('/agregarPaciente', methods=['POST'])
def agregarPaciente():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientes')
    data = cur.fetchall()
    cur.close()
    return render_template('agregarPaciente.html', pacientes=data)


@app.route('/cargarArchivo', methods=['GET', 'POST'])
def cargarArchivo():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientes')
    data = cur.fetchall()
    cur.close()
    return render_template('cargarArchivo.html', pacientes=data)


@app.route('/depurado', methods=['GET', 'POST'])
def depurado():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientesdepurada')
    registros = cur.fetchall()

    # data = [[15, 18], [10, 24]]
    # print(data)
    # # Realizar la prueba de chi-cuadrado
    # chi2, p_value, dof, expected = chi2_contingency(data, correction=False)
    #
    # # Imprimir los resultados
    # print("Estadística de chi-cuadrado:", chi2)
    # print("Valor p:", p_value)

    return render_template('beforeCalc.html')


@app.route('/procesar', methods=['GET', 'POST'])
def procesar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientesdepurada')

    opcion1 = request.form['opcion1']
    opcion2 = request.form['opcion2']
    # print(opcion1)
    # print(opcion2)
    opciones = {
        'RESULTADO_NUMERICO_PREVENTIX': 'PREVENTIX',
        'RESULTADO_NUMERICO_VPH': 'VPH',
        'RESULTADO_NUMERICO_PAP': 'Citología Líquida',
        'Resultado_num_biopsia': 'Biopsia',
        'resultado_numerico_colposcopia': 'Colposcopia'
    }

    opcionr1 = opciones.get(opcion1, opcion1)
    opcionr2 = opciones.get(opcion2, opcion2)

    ####
    # Construir y ejecutar las consultas SQL
    consulta_1 = f"SELECT COUNT(*) FROM pacientesdepurada WHERE {opcion1} = '101' AND {opcion2} = '101'"
    cur.execute(consulta_1)
    consulta01 = cur.fetchall()[0]['COUNT(*)']

    consulta_2 = f"SELECT COUNT(*) FROM pacientesdepurada WHERE {opcion1} = '101' AND {opcion2} = '100'"
    cur.execute(consulta_2)
    consulta02 = cur.fetchall()[0]['COUNT(*)']

    consulta_3 = f"SELECT COUNT(*) FROM pacientesdepurada WHERE {opcion1} = '100' AND {opcion2} = '101'"
    cur.execute(consulta_3)
    consulta03 = cur.fetchall()[0]['COUNT(*)']

    consulta_4 = f"SELECT COUNT(*) FROM pacientesdepurada WHERE {opcion1} = '100' AND {opcion2} = '100'"
    cur.execute(consulta_4)
    consulta04 = cur.fetchall()[0]['COUNT(*)']

    cur.close()







    # # Valores de la tabla 2x2
    # c1 = 15  # Resultados concordantes
    # c2 = 21  # Resultados discordantes

    # Calcula el valor p y el poder de la prueba
    p_value1, power = mcnemar_test(consulta02, consulta03)
    # print(consulta02)
    # print(consulta03)

    # print("Valor p:", p_value)
    # print("Poder de la prueba:", power)
    # Example usage:
    x = np.array([[consulta01, consulta02], [consulta03, consulta04]])
    # Datos de la matriz PREVvsCOLP
    PREVvsCOLP = np.array([[consulta01, consulta03], [consulta02, consulta04]])



    # Realizar la prueba McNemar
    chi2_stat, p_value = chi2_contingency(PREVvsCOLP, correction=True)[:2]


    # Calcular el poder de la prueba McNemar usando la función pwr_mcnemar
    n = consulta04 + consulta03 + consulta02 + consulta01
    p10 = consulta02 / n
    p01 = consulta03 / n
    result = pwr_mcnemar(p10, p01, alpha=0.05, n=n)
    # print(
    #     f"Resultado: Poder de la prueba {result['power']:.4f} o {result['power'] * 100:.2f}%. Calculado con la aproximación del Dr. Greenwell.")
    # Calcular la potencia como porcentaje
    potenciadr = result['power'] * 100

    # Ahora puedes utilizar potenciadr para lo que necesites
    chimc = round(chi2_stat,5)
    pval = round(p_value, 5)




    data = [[consulta01, consulta02], [consulta03, consulta04]]
    # sensibilidad = consulta01 / (consulta01 + consulta03)
    # especificidad = consulta04 / (consulta02 + consulta04)
    # vpp = consulta01 / (consulta01 + consulta02)
    # vpn = consulta04 / (consulta03 + consulta04)
    # rpp = sensibilidad / (1 - especificidad)
    # rpn = (1 - sensibilidad) / especificidad
    if consulta01 + consulta03 != 0:
        sens = (consulta01 / (consulta01 + consulta03)) * 100
        sensibilidad = round(sens, 2)
    else:
        sensibilidad = 0.0

    if consulta02 + consulta04 != 0:
        especificidad = round(((consulta04 / (consulta02 + consulta04)) * 100), 2)
    else:
        especificidad = 0.0

    if consulta01 + consulta02 != 0:
        vpp = round(((consulta01 / (consulta01 + consulta02)) * 100), 2)
    else:
        vpp = 0.0

    if consulta03 + consulta04 != 0:
        vpn = round(((consulta04 / (consulta03 + consulta04)) * 100), 2)
    else:
        vpn = 0.0

    if 1 - especificidad != 0:
        rpp = round((sensibilidad / (1 - especificidad)), 2)
    else:
        rpp = 0.0

    if especificidad != 0:
        rpn = round(((1 - sensibilidad) / especificidad), 2)
    else:
        rpn = 0.0

    # print(data)
    # Realizar la prueba de chi-cuadrado
    chi2, p_value, dof, expected = chi2_contingency(data, correction=False)
    p_value = round(p_value, 4)

    # Realizar el cálculo para obtener el valor P_value

    return render_template('busquedaPersonalizada.html', vpp=vpp, vpn=vpn, rpp=rpp, rpn=rpn, sensibilidad=sensibilidad,
                           especificidad=especificidad, consulta01=consulta01, consulta02=consulta02,
                           consulta03=consulta03, consulta04=consulta04, chi2=chi2, p_value=p_value, opcion2=opcion2,
                           opcion1=opcion1, opcionr1=opcionr1, opcionr2=opcionr2, power=power, p_value1 = p_value1,potenciadr = potenciadr, chimc=chimc,pval=pval)



def mcnemar_test(c1, c2):
    # Calcula los valores necesarios para la prueba de McNemar
    n = c1 + c2  # Tamaño de la muestra
    b = c2 - c1  # Número de casos discordantes
    chi2_value = b ** 2 / (c1 + c2)  # Valor de chi-cuadrado
    p_value = 1 - chi2.cdf(chi2_value, 1)  # Valor p

    # Calcula el poder de la prueba
    #power = 1 - chi2.cdf(chi2.ppf(0.95, 1), 1) + chi2.cdf(chi2.ppf(0.95, 1) - np.sqrt(n) * abs(b) / np.sqrt(c1 + c2), 1)


    p_value = round(1 - chi2.cdf(chi2_value, 1)  , 4)

    # Calcula el poder de la prueba
    #power = 1 - binom.cdf(c1, n, 0.5) - binom.cdf(n - c2 - 1, n, 0.5)
    power = round((1 - binom.cdf(c1, n, 0.5) - binom.cdf(n - c2 - 1, n, 0.5)) * -10, 6)
    return p_value, power


def pwr_mcnemar(p10, p01, alpha=0.05, n=None, power=None):
    pdisc = p10 + p01
    pdiff = p10 - p01

    if power is None and n is not None:
        x1 = (pdiff * np.sqrt(n) - norm.ppf(1 - alpha / 2) * np.sqrt(pdisc)) / np.sqrt(pdisc - pdiff ** 2)
        x2 = (-pdiff * np.sqrt(n) - norm.ppf(1 - alpha / 2) * np.sqrt(pdisc)) / np.sqrt(pdisc - pdiff ** 2)
        power = norm.cdf(x1) + norm.cdf(x2)
    elif n is None and power is not None:
        n = ((norm.ppf(1 - alpha / 2) * np.sqrt(pdisc) + norm.ppf(power) * np.sqrt(pdisc - pdiff ** 2)) / pdiff) ** 2
    else:
        raise ValueError("Must supply one of `n` or `power`, but not both.")

    return {"n": n, "power": power}





@app.route('/tablas')
def Tablas():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                        FROM pacientesdepurada
                         ''')
    data4 = cur.fetchall()
    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE RESULTADO_NUMERICO_PREVENTIX ='101' ''')
    data = cur.fetchall()
    # print(data)

    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE Resultado_num_biopsia !='102' ''')
    data3 = cur.fetchall()
    # print(data)

    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE RESULTADO_NUMERICO_VPH IN ('101') AND PREVENTIX = 'POSITIVO' ''')
    data1 = cur.fetchall()
    # print(data1)
    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE RESULTADO_NUMERICO_VPH IN ('101') ''')
    data2 = cur.fetchall()
    # print(data2)
    cur.close()
    return render_template('tablasLimpias.html', pacientesPREVENTIX=data, pacientesPREVVPH=data1, pacientesVPH=data2,
                           pacientesBiopsia=data3, pacientesTotales=data4)

@app.route('/tablageneral')
def Tablageneral():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM pacientesdepurada ''')
    data4 = cur.fetchall()

    cur.close()
    return render_template('baseDepurada.html',  pacientesTotales=data4)

@app.route('/export_excel')
def export_excel():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE RESULTADO_NUMERICO_PREVENTIX ='101' ''')
    data = cur.fetchall()

    # Crea un DataFrame de pandas con los datos
    df = pd.DataFrame(data)

    # Crea un objeto ExcelWriter utilizando XlsxWriter como motor de escritura
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    # Escribe el DataFrame en una hoja de cálculo Excel
    df.to_excel(writer, sheet_name='Pacientes Positivas', index=False)

    # Ajusta el ancho de las columnas
    workbook = writer.book
    worksheet = writer.sheets['Pacientes Positivas']
    for i, col in enumerate(df.columns):
        column_width = max(df[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_width)

    # Cierra el objeto writer para guardar el archivo correctamente
    writer.close()

    # Guarda el contenido del archivo de Excel en una variable
    excel_data = output.getvalue()

    # Crea una respuesta HTTP con el archivo de Excel adjunto
    response = make_response(excel_data)
    response.headers['Content-Disposition'] = 'attachment; filename=pacientes_preventix.xlsx'
    response.headers['Content-type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    return response


@app.route('/export_excelCompleto')
def export_excelCompleto():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT *
                    FROM pacientesdepurada
                   ''')
    data = cur.fetchall()

    # Crea un DataFrame de pandas con los datos
    df = pd.DataFrame(data)

    # Crea un objeto ExcelWriter utilizando XlsxWriter como motor de escritura
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    # Escribe el DataFrame en una hoja de cálculo Excel
    df.to_excel(writer, sheet_name='Pacientes', index=False)

    # Ajusta el ancho de las columnas
    workbook = writer.book
    worksheet = writer.sheets['Pacientes']
    for i, col in enumerate(df.columns):
        column_width = max(df[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_width)

    # Cierra el objeto writer para guardar el archivo correctamente
    writer.close()

    # Guarda el contenido del archivo de Excel en una variable
    excel_data = output.getvalue()

    # Crea una respuesta HTTP con el archivo de Excel adjunto
    response = make_response(excel_data)
    response.headers['Content-Disposition'] = 'attachment; filename=pacientes.xlsx'
    response.headers['Content-type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    return response


if __name__ == "__main__":
    app.run()
