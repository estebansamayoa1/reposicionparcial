from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, Environment, FileSystemLoader
from typing import Dict, Text


file_loader=FileSystemLoader('templates')
env=Environment(loader=file_loader)

app=Flask(__name__)



def vocales(palabra:str)->str:
    vocales={'a','e','i','o','u'}
    contador=0;
    for i in palabra:
        for j in vocales:
            if (i==j):
                contador+=1
    return contador

def updown(palabra:str)->str:
    nueva=" "
    for i in range(len(palabra)):
        if i%2==0:
            nueva+=palabra[i].upper()
        else:
            nueva+=palabra[i].lower()
    return nueva

def naive(palabra:str)->str:
    nuevo=" "
    nuevo = palabra.replace("a", "@").replace("e", "Ω").replace("i", "/").replace("o", "0").replace("u", "^")
    return nuevo



def modificar(palabra: str) -> Dict:
    palabras = {}
    if palabra== "":
        return palabras
    palabras["Reversa"] = palabra[::-1]
    palabras["Largo"] = len(palabra)
    palabras["Mayusculas"] = palabra.upper()
    palabras["Minusculas"] = palabra.lower()
    palabras["Vocales"]=vocales(palabra)
    vocas=vocales(palabra)
    palabras["Consonantes"]=(len(palabra))-vocas
    palabras["Updown"]=updown(palabra)
    palabras["Naive"]=naive(palabra)
    return palabras


@app.route("/", methods=["GET", "POST"])
@app.route('/', methods=['GET', 'POST'])
def index():
    template = env.get_template('palabra.html')
    palabra=" "
    pala={}
    if request.method == 'POST':
        palabra = request.form['palabra']
        print (f'{palabra}')
        pala=modificar(palabra)
    return template.render(pala=pala)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
