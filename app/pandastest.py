import pandas as pd
import csv
import mysql.connector

# Establecer la conexión con la base de datos MySQL
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pacientes'
)
cursor = cnx.cursor()

BaseDatos = pd.read_csv('BaseDatos.csv', index_col=False)
BaseDatos.head()
print(BaseDatos)

for row in BaseDatos.itertuples(index=False):
    values = list(row)
    print(row)
    query = '''
            INSERT INTO pacientes (
                Folio, IDForm, Nombre, FechaNacimiento, Edad, Peso, Talla, IMC, TRATAMIENTO_HORMONAL_ACTUAL, VACUNAS, CANCER_ATX, DIABETES, HIPERTENSION, TIROIDEO, INMUNOLOGICO, VIH, ITS, VPH, FUMA, DROGAS, IVSA, NPS, ANO_DEL_ULTIMO_PAP, MPF, Gestas, INTERPRETACION_PREVENTIX_FINAL, VPH2, Gen, CitologiaResultado, TrichomonaVaginalis, MicroorganismosFungicosCandidaSpp, VaginosisBacteriana, BacteriasCompatiblesConActinomycesSpp, CambiosCelularesCompatiblesConHerpes, AlteracionesCelularesInflamatorias, AlteracionesCelularesSecundariasARadiacion, AlteracionesCelularesSecundariasADIU, AtrofiaCelular, CelulasEscamosasASC_US, CelulasEscamosasASC_H, CambiosCelularesVPH, LesionIntraepitelialDisplasiaLeve, LesionIntraepitelialDisplasiaModerada, CarcinomaDeCelulasEscamosas, CelulasEndometrialesBenignasEnPostmenopausia, CelulasGlandularesAtipicasAGUS, AdenocarcinomaDeOrigenEndocervical, AdenocarcinomaDeOrigenEndometrial, AdenocarcinomaDeOrigenNoDefinido, Colposcopia, Cervix, ZonaDeTransformacion, Superficie, Bordes, EpitelioAcetoblanco, PruebaDeShiller, DiagnosticoColposcopico, Otros, Biopsia, Diagnostico
            )
            VALUES (
                %(Folio)s, %(IDForm)s, %(Nombre)s, %(FechaNacimiento)s, %(Edad)s, %(Peso)s, %(Talla)s, %(IMC)s, %(TRATAMIENTO_HORMONAL_ACTUAL)s, %(VACUNAS)s, %(CANCER_ATX)s, %(DIABETES)s, %(HIPERTENSION)s, %(TIROIDEO)s, %(INMUNOLOGICO)s, %(VIH)s, %(ITS)s, %(VPH)s, %(FUMA)s, %(DROGAS)s, %(IVSA)s, %(NPS)s, %(ANO_DEL_ULTIMO_PAP)s, %(MPF)s, %(Gestas)s, %(INTERPRETACION_PREVENTIX_FINAL)s, %(VPH2)s, %(Gen)s, %(CitologiaResultado)s, %(TrichomonaVaginalis)s, %(MicroorganismosFungicosCandidaSpp)s, %(VaginosisBacteriana)s, %(BacteriasCompatiblesConActinomycesSpp)s, %(CambiosCelularesCompatiblesConHerpes)s, %(AlteracionesCelularesInflamatorias)s, %(AlteracionesCelularesSecundariasARadiacion)s, %(AlteracionesCelularesSecundariasADIU)s, %(AtrofiaCelular)s, %(CelulasEscamosasASC_US)s, %(CelulasEscamosasASC_H)s, %(CambiosCelularesVPH)s, %(LesionIntraepitelialDisplasiaLeve)s, %(LesionIntraepitelialDisplasiaModerada)s, %(CarcinomaDeCelulasEscamosas)s, %(CelulasEndometrialesBenignasEnPostmenopausia)s, %(CelulasGlandularesAtipicasAGUS)s, %(AdenocarcinomaDeOrigenEndocervical)s, %(AdenocarcinomaDeOrigenEndometrial)s, %(AdenocarcinomaDeOrigenNoDefinido)s, %(Colposcopia)s, %(Cervix)s, %(ZonaDeTransformacion)s, %(Superficie)s, %(Bordes)s, %(EpitelioAcetoblanco)s, %(PruebaDeShiller)s, %(DiagnosticoColposcopico)s, %(Otros)s, %(Biopsia)s, %(Diagnostico)s
            )
        '''

    # Imprime la consulta SQL y los valores para depurar
    print("Query:", query)
    print("Values:", values)

    # Ejecuta la consulta SQL con los valores proporcionados
    cursor.execute(query, values)

# Cerrar la conexión con la base de datos.
cnx.commit()
cursor.close()
cnx.close()
