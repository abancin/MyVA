from django.contrib import admin

from MyVA.Apps.GestionActivos.models import *


# Register your models here.

admin.site.Register(Equipo)
admin.site.Register(EspecificacionesTecnicas)
