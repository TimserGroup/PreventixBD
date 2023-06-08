from flask import Blueprint, request, render_template, redirect, url_for, flash, Flask
import numpy as np
from scipy.stats import chi2_contingency
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "mysecretkey"

# Mysql Settings
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'sql9624432'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'BNMN2TSHZL'
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'sql9.freemysqlhosting.net'
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'sql9624432'
app.config['MYSQL_PORT'] = os.getenv('PORT') or 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)

pacientes = Blueprint('pacientes', __name__, template_folder='app/templates')

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientes')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', pacientes=data)

@app.route('/add_paciente', methods=['POST'])
def add_paciente():
    if request.method == 'POST':
        Folio = request.form['Folio']
        IDForm = request.form['IDForm']
        Nombre = request.form['Nombre']
        FechaNacimiento = request.form['FechaNacimiento']
        Edad = int(request.form['Edad'])
        Peso = float(request.form['Peso'])
        Talla = float(request.form['Talla'])
        IMC = float(request.form['IMC'])
        TRATAMIENTO_HORMONAL_ACTUAL = request.form['TRATAMIENTO_HORMONAL_ACTUAL']
        VACUNAS = request.form['VACUNAS']
        CANCER_ATX = request.form['CANCER_ATX']
        DIABETES = request.form['DIABETES']
        HIPERTENSION = request.form['HIPERTENSION']
        TIROIDEO = request.form['TIROIDEO']
        INMUNOLOGICO = request.form['INMUNOLOGICO']
        VIH = request.form['VIH']
        ITS = request.form['ITS']
        VPH = request.form['VPH']
        FUMA = request.form['FUMA']
        DROGAS = request.form['DROGAS']
        IVSA = request.form['IVSA']
        NPS = request.form['NPS']
        ANO_DEL_ULTIMO_PAP = request.form['ANO_DEL_ULTIMO_PAP']
        MPF = request.form['MPF']
        Gestas = int(request.form['Gestas'])
        INTERPRETACION_PREVENTIX_FINAL = request.form['INTERPRETACION_PREVENTIX_FINAL']
        VPH2 = request.form['VPH2']
        Gen = request.form['Gen']
        CitologiaResultado = request.form['CitologiaResultado']
        TrichomonaVaginalis = request.form['TrichomonaVaginalis']
        MicroorganismosFungicosCandidaSpp = request.form['MicroorganismosFungicosCandidaSpp']
        VaginosisBacteriana = request.form['VaginosisBacteriana']
        BacteriasCompatiblesConActinomycesSpp = request.form['BacteriasCompatiblesConActinomycesSpp']
        CambiosCelularesCompatiblesConHerpes = request.form['CambiosCelularesCompatiblesConHerpes']
        AlteracionesCelularesInflamatorias = request.form['AlteracionesCelularesInflamatorias']
        AlteracionesCelularesSecundariasARadiacion = request.form['AlteracionesCelularesSecundariasARadiacion']
        AlteracionesCelularesSecundariasADIU = request.form['AlteracionesCelularesSecundariasADIU']
        AtrofiaCelular = request.form['AtrofiaCelular']
        CelulasEscamosasASC_US = request.form['CelulasEscamosasASC_US']
        CelulasEscamosasASC_H = request.form['CelulasEscamosasASC_H']
        CambiosCelularesVPH = request.form['CambiosCelularesVPH']
        LesionIntraepitelialDisplasiaLeve = request.form['LesionIntraepitelialDisplasiaLeve']
        LesionIntraepitelialDisplasiaModerada = request.form['LesionIntraepitelialDisplasiaModerada']
        CarcinomaDeCelulasEscamosas = request.form['CarcinomaDeCelulasEscamosas']
        CelulasEndometrialesBenignasEnPostmenopausia = request.form['CelulasEndometrialesBenignasEnPostmenopausia']
        CelulasGlandularesAtipicasAGUS = request.form['CelulasGlandularesAtipicasAGUS']
        AdenocarcinomaDeOrigenEndocervical = request.form['AdenocarcinomaDeOrigenEndocervical']
        AdenocarcinomaDeOrigenEndometrial = request.form['AdenocarcinomaDeOrigenEndometrial']
        AdenocarcinomaDeOrigenNoDefinido = request.form['AdenocarcinomaDeOrigenNoDefinido']
        Colposcopia = request.form['Colposcopia']
        Cervix = request.form['Cervix']
        ZonaDeTransformacion = request.form['ZonaDeTransformacion']
        Superficie = request.form['Superficie']
        Bordes = request.form['Bordes']
        EpitelioAcetoblanco = request.form['EpitelioAcetoblanco']
        PruebaDeShiller = request.form['PruebaDeShiller']
        DiagnosticoColposcopico = request.form['DiagnosticoColposcopico']
        Otros = request.form['Otros']
        Biopsia = request.form['Biopsia']
        Diagnostico = request.form['Diagnostico']

        try:
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO pacientes (Folio, IDForm, Nombre, FechaNacimiento, Edad, Peso, Talla, IMC, TRATAMIENTO_HORMONAL_ACTUAL, VACUNAS, CANCER_ATX, DIABETES, HIPERTENSION, TIROIDEO, INMUNOLOGICO, VIH, ITS, VPH, FUMA, DROGAS, IVSA, NPS, ANO_DEL_ULTIMO_PAP, MPF, Gestas, INTERPRETACION_PREVENTIX_FINAL, VPH2, Gen, CitologiaResultado, TrichomonaVaginalis, MicroorganismosFungicosCandidaSpp, VaginosisBacteriana, BacteriasCompatiblesConActinomycesSpp, CambiosCelularesCompatiblesConHerpes, AlteracionesCelularesInflamatorias, AlteracionesCelularesSecundariasARadiacion, AlteracionesCelularesSecundariasADIU, AtrofiaCelular, CelulasEscamosasASC_US, CelulasEscamosasASC_H, CambiosCelularesVPH, LesionIntraepitelialDisplasiaLeve, LesionIntraepitelialDisplasiaModerada, CarcinomaDeCelulasEscamosas, CelulasEndometrialesBenignasEnPostmenopausia, CelulasGlandularesAtipicasAGUS, AdenocarcinomaDeOrigenEndocervical, AdenocarcinomaDeOrigenEndometrial, AdenocarcinomaDeOrigenNoDefinido, Colposcopia, Cervix, ZonaDeTransformacion, Superficie, Bordes, EpitelioAcetoblanco, PruebaDeShiller, DiagnosticoColposcopico, Otros, Biopsia, Diagnostico)
            VALUES (%(Folio)s, %(IDForm)s, %(Nombre)s, %(FechaNacimiento)s, %(Edad)s, %(Peso)s, %(Talla)s, %(IMC)s, %(TRATAMIENTO_HORMONAL_ACTUAL)s, %(VACUNAS)s, %(CANCER_ATX)s, %(DIABETES)s, %(HIPERTENSION)s, %(TIROIDEO)s, %(INMUNOLOGICO)s, %(VIH)s, %(ITS)s, %(VPH)s, %(FUMA)s, %(DROGAS)s, %(IVSA)s, %(NPS)s, %(ANO_DEL_ULTIMO_PAP)s, %(MPF)s, %(Gestas)s, %(INTERPRETACION_PREVENTIX_FINAL)s, %(VPH2)s, %(Gen)s, %(CitologiaResultado)s, %(TrichomonaVaginalis)s, %(MicroorganismosFungicosCandidaSpp)s, %(VaginosisBacteriana)s, %(BacteriasCompatiblesConActinomycesSpp)s, %(CambiosCelularesCompatiblesConHerpes)s, %(AlteracionesCelularesInflamatorias)s, %(AlteracionesCelularesSecundariasARadiacion)s, %(AlteracionesCelularesSecundariasADIU)s, %(AtrofiaCelular)s, %(CelulasEscamosasASC_US)s, %(CelulasEscamosasASC_H)s, %(CambiosCelularesVPH)s, %(LesionIntraepitelialDisplasiaLeve)s, %(LesionIntraepitelialDisplasiaModerada)s, %(CarcinomaDeCelulasEscamosas)s, %(CelulasEndometrialesBenignasEnPostmenopausia)s, %(CelulasGlandularesAtipicasAGUS)s, %(AdenocarcinomaDeOrigenEndocervical)s, %(AdenocarcinomaDeOrigenEndometrial)s, %(AdenocarcinomaDeOrigenNoDefinido)s, %(Colposcopia)s, %(Cervix)s, %(ZonaDeTransformacion)s, %(Superficie)s, %(Bordes)s, %(EpitelioAcetoblanco)s, %(PruebaDeShiller)s, %(DiagnosticoColposcopico)s, %(Otros)s, %(Biopsia)s, %(Diagnostico)s)''')

            mysql.connection.commit()
            flash('Paciente añadido correctamente')
            return redirect(url_for('pacientes.Index'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('pacientes.Index'))


@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_paciente(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pacientes WHERE id = %s', id)
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-patient.html', paciente=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_paciente(id):
    if request.method == 'POST':
        Folio = request.form['Folio']
        IDForm = request.form['IDForm']
        Nombre = request.form['Nombre']
        FechaNacimiento = request.form['FechaNacimiento']
        Edad = int(request.form['Edad'])
        Peso = float(request.form['Peso'])
        Talla = float(request.form['Talla'])
        IMC = float(request.form['IMC'])
        TRATAMIENTO_HORMONAL_ACTUAL = request.form['TRATAMIENTO_HORMONAL_ACTUAL']
        VACUNAS = request.form['VACUNAS']
        CANCER_ATX = request.form['CANCER_ATX']
        DIABETES = request.form['DIABETES']
        HIPERTENSION = request.form['HIPERTENSION']
        TIROIDEO = request.form['TIROIDEO']
        INMUNOLOGICO = request.form['INMUNOLOGICO']
        VIH = request.form['VIH']
        ITS = request.form['ITS']
        VPH = request.form['VPH']
        FUMA = request.form['FUMA']
        DROGAS = request.form['DROGAS']
        IVSA = request.form['IVSA']
        NPS = request.form['NPS']
        ANO_DEL_ULTIMO_PAP = request.form['ANO_DEL_ULTIMO_PAP']
        MPF = request.form['MPF']
        Gestas = int(request.form['Gestas'])
        INTERPRETACION_PREVENTIX_FINAL = request.form['INTERPRETACION_PREVENTIX_FINAL']
        VPH2 = request.form['VPH2']
        Gen = request.form['Gen']
        CitologiaResultado = request.form['CitologiaResultado']
        TrichomonaVaginalis = request.form['TrichomonaVaginalis']
        MicroorganismosFungicosCandidaSpp = request.form['MicroorganismosFungicosCandidaSpp']
        VaginosisBacteriana = request.form['VaginosisBacteriana']
        BacteriasCompatiblesConActinomycesSpp = request.form['BacteriasCompatiblesConActinomycesSpp']
        CambiosCelularesCompatiblesConHerpes = request.form['CambiosCelularesCompatiblesConHerpes']
        AlteracionesCelularesInflamatorias = request.form['AlteracionesCelularesInflamatorias']
        AlteracionesCelularesSecundariasARadiacion = request.form['AlteracionesCelularesSecundariasARadiacion']
        AlteracionesCelularesSecundariasADIU = request.form['AlteracionesCelularesSecundariasADIU']
        AtrofiaCelular = request.form['AtrofiaCelular']
        CelulasEscamosasASC_US = request.form['CelulasEscamosasASC_US']
        CelulasEscamosasASC_H = request.form['CelulasEscamosasASC_H']
        CambiosCelularesVPH = request.form['CambiosCelularesVPH']
        LesionIntraepitelialDisplasiaLeve = request.form['LesionIntraepitelialDisplasiaLeve']
        LesionIntraepitelialDisplasiaModerada = request.form['LesionIntraepitelialDisplasiaModerada']
        CarcinomaDeCelulasEscamosas = request.form['CarcinomaDeCelulasEscamosas']
        CelulasEndometrialesBenignasEnPostmenopausia = request.form['CelulasEndometrialesBenignasEnPostmenopausia']
        CelulasGlandularesAtipicasAGUS = request.form['CelulasGlandularesAtipicasAGUS']
        AdenocarcinomaDeOrigenEndocervical = request.form['AdenocarcinomaDeOrigenEndocervical']
        AdenocarcinomaDeOrigenEndometrial = request.form['AdenocarcinomaDeOrigenEndometrial']
        AdenocarcinomaDeOrigenNoDefinido = request.form['AdenocarcinomaDeOrigenNoDefinido']
        Colposcopia = request.form['Colposcopia']
        Cervix = request.form['Cervix']
        ZonaDeTransformacion = request.form['ZonaDeTransformacion']
        Superficie = request.form['Superficie']
        Bordes = request.form['Bordes']
        EpitelioAcetoblanco = request.form['EpitelioAcetoblanco']
        PruebaDeShiller = request.form['PruebaDeShiller']
        DiagnosticoColposcopico = request.form['DiagnosticoColposcopico']
        Otros = request.form['Otros']
        Biopsia = request.form['Biopsia']
        Diagnostico = request.form['Diagnostico']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE pacientes
            SET 
                Folio=%s,
                IDForm =%s,
                Nombre =%s,
                FechaNacimiento =%s,
                Edad =%s,
                Peso =%s,
                Talla =%s,
                IMC =%s,
                TRATAMIENTO_HORMONAL_ACTUAL =%s,
                VACUNAS =%s,
                CANCER_ATX =%s,
                DIABETES =%s,
                HIPERTENSION =%s,
                TIROIDEO =%s,
                INMUNOLOGICO =%s,
                VIH =%s,
                ITS =%s,
                VPH =%s,
                FUMA=%s,
                DROGAS =%s,
                IVSA =%s,                                
                NPS =%s,                               
                ANO_DEL_ULTIMO_PAP =%s,                                   
                MPF =%s,                                     
                Gestas =%s,                                    
                INTERPRETACION_PREVENTIX_FINAL =%s,                                
                VPH2 =%s,                                                      
                Gen =%s,                                             
                CitologiaResultado =%s,                                
                TrichomonaVaginalis =%s,                               
                MicroorganismosFungicosCandidaSpp =%s,              
                VaginosisBacteriana =%s,                      
                BacteriasCompatiblesConActinomycesSpp =%s,         
                CambiosCelularesCompatiblesConHerpes =%s,          
                AlteracionesCelularesInflamatorias =%s,          
                AlteracionesCelularesSecundariasARadiacion =%s,     
                AlteracionesCelularesSecundariasADIU =%s,       
                AtrofiaCelular =%s,         
                CelulasEscamosasASC_US =%s,          
                CelulasEscamosasASC_H =%s,          
                CambiosCelularesVPH =%s,          
                LesionIntraepitelialDisplasiaLeve =%s,         
                LesionIntraepitelialDisplasiaModerada =%s,         
                CarcinomaDeCelulasEscamosas =%s,       
                CelulasEndometrialesBenignasEnPostmenopausia =%s,
                CelulasGlandularesAtipicasAGUS =%s,       
                AdenocarcinomaDeOrigenEndocervical =%s,        
                AdenocarcinomaDeOrigenEndometrial =%s,        
                AdenocarcinomaDeOrigenNoDefinido =%s,        
                Colposcopia =%s,       
                Cervix =%s,        
                ZonaDeTransformacion =%s,         
                Superficie =%s,                
                Bordes =%s,                   
                EpitelioAcetoblanco =%s,                    
                PruebaDeShiller =%s,                     
                DiagnosticoColposcopico=%s,                      
                Otros =%s,                      
                Biopsia =%s,                        
                Diagnostico =%s,  
            WHERE id = %s
        """, (Folio, IDForm, Nombre, FechaNacimiento, Edad, Peso, Talla, IMC, TRATAMIENTO_HORMONAL_ACTUAL, VACUNAS,
              CANCER_ATX, DIABETES, HIPERTENSION, TIROIDEO, INMUNOLOGICO, VIH, ITS, VPH, FUMA, DROGAS, IVSA, NPS,
              ANO_DEL_ULTIMO_PAP, MPF, Gestas, INTERPRETACION_PREVENTIX_FINAL, VPH2, Gen, CitologiaResultado,
              TrichomonaVaginalis, MicroorganismosFungicosCandidaSpp, VaginosisBacteriana,
              BacteriasCompatiblesConActinomycesSpp, CambiosCelularesCompatiblesConHerpes,
              AlteracionesCelularesInflamatorias, AlteracionesCelularesSecundariasARadiacion,
              AlteracionesCelularesSecundariasADIU, AtrofiaCelular, CelulasEscamosasASC_US, CelulasEscamosasASC_H,
              CambiosCelularesVPH, LesionIntraepitelialDisplasiaLeve, LesionIntraepitelialDisplasiaModerada,
              CarcinomaDeCelulasEscamosas, CelulasEndometrialesBenignasEnPostmenopausia, CelulasGlandularesAtipicasAGUS,
              AdenocarcinomaDeOrigenEndocervical, AdenocarcinomaDeOrigenEndometrial, AdenocarcinomaDeOrigenNoDefinido,
              Colposcopia, Cervix, ZonaDeTransformacion, Superficie, Bordes, EpitelioAcetoblanco, PruebaDeShiller,
              DiagnosticoColposcopico, Otros, Biopsia, Diagnostico))
        flash('Paciente actualizado correctamente')
        mysql.connection.commit()
        return redirect(url_for('pacientes.Index'))


@app.route('/busquedas', methods=['GET'])
def busquedas():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT COUNT(*) 
                    FROM pacientesdepurada
                    WHERE PREVENTIX = 'positivo' AND Resultado_biopsia_de_cervix != 'NO SE REALIZO' ''')
    dataPrevBiopsia = cur.fetchall()[0]['COUNT(*)']

    cur.execute('''SELECT COUNT(*) 
                        FROM pacientesdepurada
                        WHERE PREVENTIX = 'positivo' AND Resultado_biopsia_de_cervix = 'NO SE REALIZO' ''')
    dataPrevBiopsiaN = cur.fetchall()[0]['COUNT(*)']

    cur.execute('''SELECT COUNT(*) 
                        FROM pacientesdepurada
                        WHERE PREVENTIX = 'negativo' AND Resultado_biopsia_de_cervix != 'NO SE REALIZO' ''')
    dataPrevNBiopsia = cur.fetchall()[0]['COUNT(*)']

    cur.execute('''SELECT COUNT(*) 
                            FROM pacientesdepurada
                            WHERE PREVENTIX = 'negativo' AND Resultado_biopsia_de_cervix = 'NO SE REALIZO' ''')
    dataPrevNBiopsiaN = cur.fetchall()[0]['COUNT(*)']

    cur.close()
    return render_template('graficas.html', dataPrevNBiopsiaN=dataPrevNBiopsiaN, dataPrevNBiopsia=dataPrevNBiopsia,
                           dataPrevBiopsiaN=dataPrevBiopsiaN, dataPrevBiopsia=dataPrevBiopsia)


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_paciente(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM pacientes WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Paciente borrado correctamente')
    return redirect(url_for('pacientes.Index'))


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
        'RESULTADO_NUMERICO_PAP': 'Papanicolaou',
        'Resultado_num_biopsia': 'Biopsia',
        'resultado_numerico_colposcopia': 'Colposcopia'
    }

    opcionr1 = opciones.get(opcion1, opcion1)
    opcionr2 = opciones.get(opcion2, opcion2)

    # Construir y ejecutar la consulta SQL
    consulta = f"SELECT COUNT(*)  FROM pacientesdepurada WHERE {opcion1} = '101' AND {opcion2} = '101'"
    cur.execute(consulta)
    consulta01 = cur.fetchall()[0]['COUNT(*)']

    consulta1 = f"SELECT COUNT(*)  FROM pacientesdepurada WHERE {opcion1} = '101' AND {opcion2} = '100'"
    cur.execute(consulta1)
    consulta02 = cur.fetchall()[0]['COUNT(*)']

    consulta2 = f"SELECT COUNT(*)  FROM pacientesdepurada WHERE {opcion1} = '100' AND {opcion2} = '101'"
    cur.execute(consulta2)
    consulta03 = cur.fetchall()[0]['COUNT(*)']

    consulta3 = f"SELECT COUNT(*)  FROM pacientesdepurada WHERE {opcion1} = '100' AND {opcion2} = '100'"
    cur.execute(consulta3)
    consulta04 = cur.fetchall()[0]['COUNT(*)']
    cur.close()

    data = [[consulta01, consulta02], [consulta03, consulta04]]
    # sensibilidad = consulta01 / (consulta01 + consulta03)
    # especificidad = consulta04 / (consulta02 + consulta04)
    # vpp = consulta01 / (consulta01 + consulta02)
    # vpn = consulta04 / (consulta03 + consulta04)
    # rpp = sensibilidad / (1 - especificidad)
    # rpn = (1 - sensibilidad) / especificidad
    if consulta01 + consulta03 != 0:
        sensibilidad = consulta01 / (consulta01 + consulta03)
    else:
        sensibilidad = 0.0

    if consulta02 + consulta04 != 0:
        especificidad = consulta04 / (consulta02 + consulta04)
    else:
        especificidad = 0.0

    if consulta01 + consulta02 != 0:
        vpp = consulta01 / (consulta01 + consulta02)
    else:
        vpp = 0.0

    if consulta03 + consulta04 != 0:
        vpn = consulta04 / (consulta03 + consulta04)
    else:
        vpn = 0.0

    if 1 - especificidad != 0:
        rpp = sensibilidad / (1 - especificidad)
    else:
        rpp = 0.0

    if especificidad != 0:
        rpn = (1 - sensibilidad) / especificidad
    else:
        rpn = 0.0

    # print(data)
    # Realizar la prueba de chi-cuadrado
    chi2, p_value, dof, expected = chi2_contingency(data, correction=False)

    # Realizar el cálculo para obtener el valor P_value

    return render_template('busquedaPersonalizada.html', vpp=vpp, vpn=vpn, rpp=rpp, rpn=rpn, sensibilidad=sensibilidad,
                           especificidad=especificidad, consulta01=consulta01, consulta02=consulta02,
                           consulta03=consulta03, consulta04=consulta04, chi2=chi2, p_value=p_value, opcion2=opcion2,
                           opcion1=opcion1, opcionr1=opcionr1, opcionr2=opcionr2)


@app.route('/tablas')
def Tablas():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE PREVENTIX ='positivo' ''')
    data = cur.fetchall()
    # print(data)

    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE Resultado_biopsia_de_cervix !='NO SE REALIZO' ''')
    data3 = cur.fetchall()
    # print(data)

    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE Resultado_PCR_VPH IN ('POOL DE 13 SEROTIPOS', 'SEROTIPO 16', 'POSITIVO (31,33,35,39,45,51,52,56,58,59,66,67,68)') AND PREVENTIX = 'POSITIVO' ''')
    data1 = cur.fetchall()
    # print(data1)
    cur.execute('''SELECT ID, RESULTADO_NUMERICO_PREVENTIX, RESULTADO_NUMERICO_VPH, RESULTADO_NUMERICO_PAP, resultado_numerico_colposcopia, Resultado_num_biopsia
                    FROM pacientesdepurada
                    WHERE Resultado_PCR_VPH IN ('POOL DE 13 SEROTIPOS', 'SEROTIPO 16', 'POSITIVO (31,33,35,39,45,51,52,56,58,59,66,67,68)') ''')
    data2 = cur.fetchall()
    # print(data2)
    cur.close()
    return render_template('tablasLimpias.html', pacientesPREVENTIX=data, pacientesPREVVPH=data1, pacientesVPH=data2,
                           pacientesBiopsia=data3)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
