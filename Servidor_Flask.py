# Server Flask

#Para Inicializar:
#1 Escribir set nombre para server = RutaAbsolutaDeEsteArchivo.py
#2 Escribir flask run
from flask import  request, Flask   #Importamos lo que necesitamos de flask para este proyecto
import json

ArchivoHTML = open("PaginaWeb.html", "r")   #Abrimos un archivo HTML para convertir sus lineas en una lista
Inter = ArchivoHTML.readlines()
ArchivoHTML.close()
Texto = ""
for i in Inter: #Ahora sumamos cada elemento para hacer un string que se imprimirá
    Texto += i
"""ArchivoXML = open("Textos.xml", "r") #Hacemos lo mismo que antes pero con un archivo xml
Interin = ArchivoXML.readlines()
ArchivoXML.close()
Textos = ""
for i in Interin:
    Textos += i
"""
#Sale error si se returna ArchivoHTML
#Es correcto returnar Texto
Server = Flask(__name__, template_folder = "Programacion_BackEnd")  #El primer parametro especifica que archivo será la app
                                                                    #El segundo parametro especifica donde buscar los templates

@Server.route("/") #Texto es igual a la página hmtl, la cual returnamos cuando alguien ingresa al server
def Funcion_Init(): 
    return Texto
@Server.route("/InitRegistrarse") #Si presionan registrarse, devolvemos el primer formulario
def Prim_Form():
    return '''<form action = "/Registrarse" method = "post">
    <label for = "nombre">Su nombre De usuario será</label>
    <input type = "text" name="nombre" required><br>
    <label for = "Cant_Archs">Cuantos archivos busca tener?</label>
    <input type = "number" name="Cant_Archs" min= "1"  required><br
    ><button type = "sumbit">Enviar</button>
    </form> '''

@Server.route("/Registrarse", methods=["POST"]) #Al enviar el anterior formulario con el nombre y la cantidad de archivos
def New_User():
    global Nombre #Hacemos globales a estas dos variables que necesitaremos en varias funciones
    global Cant_Archs
    Nombre = request.form["nombre"] #Recibmos los datos del formulario
    Cant_Archs = request.form["Cant_Archs"]
    
    Nombre,Cant_Archs = Nombre.lower(), int(Cant_Archs) #Importante transformarlos correctamente para que coincidan con el tipo de dato buscado
    Kamtda = ""

    for i in range(Cant_Archs): #Segun la cantidad de archivos que se pidan creamos más formularios con distinto nombre segun su numero
        Kamtda +=  f'''<label for = "nombreArch{str(i)}">NombreDeArchivo</label><input type = "text" name="nombreArch{str(i)}" required><br><label for = "tipoArch{str(i)}">TipoDeArchivo</label>
    <input type = "text" name="tipoArch{str(i)}"  required value = "."><br>'''

    return   '''<form action = "/FinRegistro" method = "post">''' + Kamtda + '''<button type = "sumbit">Enviar</button>
    </form> ''' #Lo devolvemos agregando la direccion y boton para enviarlos


@Server.route("/FinRegistro", methods = ["POST"])
def Formar_Archivos():
    
    with open("Usuarios.json", "r") as file:
      JonhSON = json.load(file)
    
    New_Num_User = JonhSON["Cant_Users"]
    New_Num_User += 1
    JonhSON["Cant_Users"] = New_Num_User
    
    ListaArchivos = []
    for i in range(Cant_Archs):
        NameArch = request.form["nombreArch" + str(i)]
        TypeArch = request.form["tipoArch" + str(i)]
        NameArch += TypeArch

        ListaArchivos.append(NameArch)
    Diccion_User = {"Nombre": Nombre, "Nivel": "visitante", "Archivos": ListaArchivos}

    JonhSON["U" + str(New_Num_User)] = Diccion_User
    with open("Usuarios.json", "w") as file:
      json.dump(JonhSON, file, indent=4)

    return "<h1> Te has registrado correctamente</h1>" + Texto
@Server.route("/IniciarSesion")
def Initium():
    return "Este espacio no esta disponible"

if __name__ == "__main__":    #Para que se ejecute al clickear el play y no al escribir en CMD
   Server.run(debug=True)  #Debug es para que de bien los errores
   print("Listo")