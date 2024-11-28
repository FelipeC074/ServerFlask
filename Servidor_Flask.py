# Server Flask

#Para Inicializar:
#1 Escribir set nombre para server = RutaAbsolutaDeEsteArchivo.py
#2 Escribir flask run
from flask import Flask, request, redirect, url_for

ArchivoHTML = open("PaginaWeb.html", "r")
Texto_Inicio = ArchivoHTML.read()
#Sale error si se returna ArchivoHTML
#Es correcto returnar Texto_Inicio
Server = Flask(__name__)

@Server.route("/")
def Funcion_Init():
    return Texto_Inicio

@Server.route('/', methods=['POST'])
def Cons_Nombre():
    NombreArch = request.form["Archi"]  #El formulario debe llamarse como dice en los corchetes
    NombreArch.lower()
    try:
      return redirect(url_for(NombreArch))    #Debe ir el nombre de una funcion entre los parentesis, la funcion no debe traer sus parentesis
    except:
       return "El archivo al que quieres dirigirte no existe"
@Server.route("/rock")
def rock():
    return "<ul><li>Soda Estereo</li><li>Divididos</li><li>ACDC</li></ul>"

@Server.route("/cumbia")
def cumbia():
    return "<ul><li>Pedro Capo</li><li>Juan Luis Guerra</li><li>Camilo</li></ul>"

@Server.route("/osos")
def osos():
    return "<ul><li>Polar</li><li>Pardo</li><li>Panda</li></ul>"

@Server.route("/perros")
def perros():
    return "<ul><li>Caniche</li><li>Pastor Suizo</li><li>Chihuahua</li></ul>"

@Server.route("/tortas")
def tortas():
    return "<ul><li>Bodas</li><li>Madre Selva</li><li>Margarita</li></ul>"

if __name__ == "main":    #Para que se ejecute solo y nos de bien los errores
   Server.run(debug=True)