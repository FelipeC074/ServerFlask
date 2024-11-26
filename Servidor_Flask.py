# Server Flask

#Para Inicializar:
#1 Escribir set nombre para server = RutaAbsolutaDeEsteArchivo.py
#2 Escribir flask run
from flask import Flask, request, redirect, url_for

ArchivoHTML = open("PaginaWeb.html", "r")
ListaLineas = ArchivoHTML.readlines()
Texto_Inicio = ""
for linea in ListaLineas:
   if linea.strip() == "</form>":
      break
   else:
      for carct in linea:
        Texto_Inicio = Texto_Inicio + carct
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
    return ListaLineas[14]

@Server.route("/cumbia")
def cumbia():
    return ListaLineas[15]

@Server.route("/osos")
def osos():
    return ListaLineas[16]

@Server.route("/perros")
def perros():
    return ListaLineas[17]

@Server.route("/tortas")
def tortas():
    return ListaLineas[18]

if __name__ == "Servidor_Flask":    #Para que se ejecute solo y nos de bien los errores
   Server.run(debug=True)