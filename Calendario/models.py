from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# clase que guarda los id de las historias de usuario, proyectos a los que pertenecen ciertos usuarios.
# class Miembro(models.Model):
#     id = models.AutoField(primary_key=True)
#     id_usuario = models.PositiveSmallIntegerField('id usuario',blank=False,null=False)
#     id_Proyecto = models.PositiveSmallIntegerField('id proyecto',blank=False,null=False)
#     id_HistUsua = models.ForeignKey('H',blank=False,null=False)

class HistoriaUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la hu', max_length=70,blank=False,null=False)
    fechaInicio = models.DateField('Fecha de inicio',blank=False,null=False)
    fechaFin = models.DateField('Fecha de finalización',blank=False,null=False)
    estado = models.BooleanField(default= False,blank=True,null=False)
    usuario = models.ManyToManyField('User',blank=False,null=False)

    def __str__(self):
        datosFila = "Nombre historia: " + self.nombre + " - Fecha inicio: " + str(self.fechaInicio)
        datosFila += " - Fecha fin: " + str(self.fechaFin)
        return datosFila
    
    def ObtenerFI(self):
        return self.fechaInicio.isoformat()
    def ObtenerFF(self):
        return self.fechaFin.isoformat()
    def ObtenerNombre(self):
        return self.nombre
    def ObtenerColor(self):
        if self.estado:
            return '#3CC45E'
        else:
            return 'red'
    
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del proyecto', max_length=40,blank=False,null=True)
    fechaInicio = models.DateField('Fecha de inicio',blank=False,null=False)
    fechaFin = models.DateField('Fecha de finalización',blank=False,null=False)
    estado = models.BooleanField(default= False,blank=True,null=False)
    rol_miembros = models.SmallIntegerField('Rol de usuario',blank=True,null=True)
    # id_miembros = models.ForeignKey(Miembro,on_delete=models.CASCADE, blank=True, null=False)
    id_gestorP = models.PositiveSmallIntegerField('id gestor del proyecto',blank=False,null=False)
    histUsua = models.ManyToManyField(HistoriaUsuario, blank=True, null=True)

    def __str__(self):
        datosFila = "Nombre proyecto: " + self.nombre + " - Fecha inicio: " + str(self.fechaInicio)
        datosFila += " - Fecha fin: " + str(self.fechaFin)
        return datosFila
    
    def ObtenerFI(self):
        return self.fechaInicio.isoformat()
    def ObtenerFF(self):
        return self.fechaFin.isoformat()
    
    def HistoriaUsuarioActual(self):
        return self.histUsua

# usuario de sistema, puede o no ser miembro de algun proyecto
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre usuario',unique=True,max_length=15)
    proyectos = models.ManyToManyField(Proyecto, blank=True)
    
    # histUsua = models.ForeignKey(HistoriaUsuario,on_delete=models.CASCADE, blank=False, null=True)
    # -------------información que no quiero de abstract user:------------------------------------------------
    last_login = None
    first_name = None
    last_name = None
    REQUIRED_FIELDS = ['nombre']

    
    def __str__(self):
        datosFila = "Nombre usuario: " + self.nombre 

        return datosFila

    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def ProyectoActual(self):
        return self.proyectos;
    def ObtenerNombre(self):
        return self.nombre;
