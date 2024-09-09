from flask import Flask, render_template 
import pandas as pd

app=Flask(__name__)

@app.route('/')

def index():
    df=pd.read_csv("observacionEspecies.csv")
    data_dict=df.to_dict(orient="records")  # varialbel data_dicc asignar el csv a un diccionario
    return render_template("index.html", data=data_dict)


if __name__ =="__main__":
    app.run(debug=True)
