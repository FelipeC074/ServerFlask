# Server Flask

#Para Inicializar:
#1 Escribir set nombre para server = RutaAbsolutaDeEsteArchivo.py
#2 Escribir flask run
from flask import  request, Flask
import json

ArchivoHTML = open("PaginaWeb.html", "r")
Inter = ArchivoHTML.readlines()
ArchivoHTML.close()
Texto = ""
for i in Inter:
    Texto += i
ArchivoXML = open("Textos.xml", "r")
Interin = ArchivoXML.readlines()
ArchivoXML.close()
Textos = ""
for i in Interin:
    Textos += i

#Sale error si se returna ArchivoHTML
#Es correcto returnar Texto
Server = Flask(__name__, template_folder = "Programacion_BackEnd")  #El primer parametro especifica que archivo será la app
                                                                    #El segundo parametro especifica donde buscar los templates

@Server.route("/") #Texto es igual al un archivo html, el cual no puede returnarse con solo abrirlo
def Funcion_Init(): 
    return Texto
@Server.route("/InitRegistrarse")
def Prim_Form():
    return '''<form action = "/Registrarse" method = "post">
    <label for = "nombre">Su nombre De usuario será</label>
    <input type = "text" name="nombre" required><br>
    <label for = "Cant_Archs">Cuantos archivos busca tener?</label>
    <input type = "number" name="Cant_Archs"  required><br
    ><button type = "sumbit">Enviar</button>
    </form> '''

@Server.route("/Registrarse", methods=["POST"]) #Al 
def New_User():
    global Nombre
    global Cant_Archs
    Nombre = request.form["nombre"]
    Cant_Archs = request.form["Cant_Archs"]
    
    Nombre,Cant_Archs = Nombre.lower(), int(Cant_Archs)
    Kamtda = ""

    for i in range(Cant_Archs):
        Kamtda +=  f'''<label for = "nombreArch{str(i)}">NombreDeArchivo</label><input type = "text" name="nombreArch{str(i)}" required><br><label for = "tipoArch{str(i)}">TipoDeArchivo</label>
    <input type = "text" name="tipoArch{str(i)}"  required value = "."><br>'''
    return   '''<form action = "/FinRegistro" method = "post">''' + Kamtda + '''<button type = "sumbit">Enviar</button>
    </form> '''


@Server.route("/FinRegistro", methods = ["POST"])
def Formar_Archivos():
    
    file = open("Usuarios.json", "r")
    JonhSON = json.load(file)
    New_Num_User = JonhSON["Cant_Users"]
    New_Num_User += 1
    
    ListaArchivos = []
    for i in range(Cant_Archs):
        NameArch = request.form["nombreArch" + str(i)]
        Parko = request.form["tipoArch" + str(i)]
        NameArch += Parko
        ListaArchivos.append(NameArch)
    Diccion_User = {"Nombre": Nombre, "Nivel": "visitante", "Archivos": ListaArchivos}
    
    Ulo = {"U" + str(New_Num_User): Diccion_User}
    file.close()

    
    JonhSON["U" + str(New_Num_User)] = Diccion_User
    with open("Usuarios.json", "w") as file:
      json.dump(JonhSON, file, indent=4)
    
    return "<h1> Te has registrado correctamente</h1>" + Texto
@Server.route("/IniciarSesion")
def Initium():
    return Textos

if __name__ == "__main__":    #Para que se ejecute al clickear el play y no al escribir en CMD
   Server.run(debug=True)  #Debug es para que de bien los errores
   print("Listo")

#Cant_Archivos es un str()