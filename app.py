from flask import Flask, render_template, jsonify
import pandas as pd

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/D_Boyaca.html')

def D_Boyaca():
    df=pd.read_csv("agrupado_boyaca.csv")
    data_dict=df.to_dict(orient="records")  # varialbel data_dicc asignar el csv a un diccionario
    return render_template("D_Boyaca.html", data=data_dict)

@app.route('/data')

def data():
    
    df2=pd.read_csv('agrupado_boyaca.csv')# Leer los datos desde el archivo CSV
    # Convertir las columnas a listas
    data = {
            'labels': df2['País'].tolist(),    # Etiquetas de la torta (Categorías)
            'values': df2['Especies'].tolist()      # Valores (Cantidad)
    }

    return jsonify(data)

@app.route('/data1')

def data1():
    
    df3=pd.read_csv('agrupado_boyaca.csv')# Leer los datos desde el archivo CSV
    # Convertir las columnas a listas
    data1 = {
            'labels': df3['País'].tolist(),    # Etiquetas de la torta (Categorías)
            'values': df3['Observaciones'].tolist()      # Valores (Cantidad)
    }

    return jsonify(data1)

@app.route('/D_Cundi.html')

def D_Cundi():
    df=pd.read_csv("agrupado_cundinamarca.csv")
    data_dict=df.to_dict(orient="records")  # varialbel data_dicc asignar el csv a un diccionario
    return render_template("D_Cundi.html", data=data_dict)

@app.route('/boyaca.html')

def boyaca():
    return render_template('boyaca.html')

@app.route('/cundinamarca.html')

def cundinamarca():
    return render_template('cundinamarca.html')

@app.route('/mapa_boyaca.html')

def mapa_boyaca():
    return render_template('mapa_boyaca.html')

@app.route('/mapacund.html')

def mapacund():
    return render_template('mapacund.html')

if __name__ =="__main__":
    app.run(debug=True)
