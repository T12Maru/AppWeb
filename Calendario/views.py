from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import get_user_model
from .models import Proyecto,HistoriaUsuario
User = get_user_model()
# Create your views here.
def Inicio(request):
    return render(request,"inicio.html")

def Signin(request):
    return render(request,"Signin.html")

def Signup(request):
    return render(request,"signup.html")

def Logout(request):
    logout(request)
    return redirect('signin')

def Perfil(request):
    return render(request,"perfil.html")

def Equipo(request):
    return render(request,"equipo.html")

def Historias(request):
    return render(request,"historias.html")

def Reportes(request):
    return render(request,"reportes.html")

def Calendario(request):
    ##esto es para pruebas nomas, aprendo a hacer querys en django
    # #buscar una query para obtener un proyecto y hacer proyecto.historiausuario
    usuario = User.objects.get(nombre=request.user.ObtenerNombre())
    nomPro = usuario.proyectos.all()
    print("este es una prueba del diccionario:   -->  ", end="")
    print(nomPro)

    #Primer metodo, crear funciones que por medio del request me regresen la info que requiero
    #Esto no funciono porque al momento de utilizar ManytoMany fields, queda ambiguo las historias de usuario
    #que quiero obtener
    # fi = request.user.ProyectoActual().HistoriaUsuarioActual().ObtenerFI()
    # ff = request.user.ProyectoActual().HistoriaUsuarioActual().ObtenerFF()
    # color = request.user.ProyectoActual().HistoriaUsuarioActual().ObtenerColor()
    # fei = proyecto.ObtenerFI()
    # fef = request.user.ObtenerFF()

    # context = {
    #     "fi": fi,
    #     "ff": ff,
    #     "color": color
    # }

    ## segundo metodo
    #  para mandar la info al calendario, se hacen diccionarios 
    # nombreHi = {}
    # fechaIni = {}
    # fechaFin = {}
    # colorHis = {}
    # claves = {}

    # clave = 0
    # #Con este ciclo se agrega la info de las historias de usuario a los diccionarios creados.
    # for historia in HistoriaUsuario.objects.filter(usuario=usuario):
    #     nombreHi[clave] = historia.nombre
    #     fechaIni[clave] = historia.fechaInicio
    #     fechaFin[clave] = historia.fechaInicio
    #     colorHis[clave] = historia.ObtenerColor()
    #     claves[clave] = clave
    #     clave += 1

    #context = {
        # "nombre": nombreHi,
        # "fi": fechaIni,
        # "ff": fechaFin,
        # "color": colorHis,
        # "claves": claves
        #}

    #------------------ tercer metodo
    #------------------ el anterior metodo era algo tedioso, mejor decidí mandarle la lista completa de HU
    #------------------ y crear un for event in events en el calendario, y trabajar directamente la
    #------------------ info de los objetos en el calendario, ver la linea de codigo 20 de calendario.html
    
    eventos = HistoriaUsuario.objects.filter(usuario=usuario)
    print(eventos)
    
    context = {
        "eventos": eventos
        }
    
    return render(request,"calendario.html",context)

