from flask import Flask,jsonify,request
import pickle
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text



app=Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    
    return """
    <h1> Pantalla Inicio</h1>
    Rutas:</br>
    All barrios->/api/v1/barrios</br>
    By Nombre->/api/v1/barrios/nombre</br> 
    By limites->/api/v1/barrios/limits
    """

@app.route("/api/v1/barrios", methods=["GET"])
def get_barrios():

    engine = create_engine('postgresql://postgres:88Bz3sVGMOfZcwf6J2NU@containers-us-west-50.railway.app:6161/railway')
    #datos = pd.read_sql('select * from "Barrios"', con=engine)
    query = text('SELECT * FROM "Barrios"')

    df = pd.read_sql_query(query, engine.connect())

    return jsonify(df.to_json())

@app.route("/api/v1/barrios/nombre", methods=["GET"])
def by_name():
    nombre = request.args["Nombre"]
    engine = create_engine('postgresql://postgres:88Bz3sVGMOfZcwf6J2NU@containers-us-west-50.railway.app:6161/railway')
    #datos = pd.read_sql('select * from "Barrios"', con=engine)
    query = text(f"""SELECT * FROM "Barrios" WHERE "Nombre"='{nombre}'""")
    df = pd.read_sql_query(query, engine.connect())

    return jsonify(df.to_json())

@app.route("/api/v1/barrios/limits", methods=["GET"])
def by_limits():
    area_min = request.args["area_min"]
    area_max = request.args["area_max"]
    engine = create_engine('postgresql://postgres:88Bz3sVGMOfZcwf6J2NU@containers-us-west-50.railway.app:6161/railway')
    #datos = pd.read_sql('select * from "Barrios"', con=engine)
    query = text(f"""SELECT * FROM "Barrios" WHERE "Areas de barrios">'{area_min}' and "Areas de barrios"<'{area_max}'""")
    df = pd.read_sql_query(query, engine.connect())

    return jsonify(df.to_json())

if __name__=="__main__":
    app.run(debug=True)

    
