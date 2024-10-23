from django.contrib import admin
from .models import User,HistoriaUsuario,Proyecto#,Miembro
admin.site.register(HistoriaUsuario) 
admin.site.register(User) 
admin.site.register(Proyecto)
# admin.site.register(Miembro)
# Register your models here.
