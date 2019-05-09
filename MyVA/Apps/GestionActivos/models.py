from django.db import models

# Create your models here.

class Equipo(models.Model) :
    CodigodeInventario = models.CharField(max_length=40)
    Fabricante = models.CharField(max_length=40)
    Modelo = models.CharField(max_length=40)
    Marca = models.CharField(max_length=10)
    Ubicacion = models.CharField(max_length=10)
    Seccion = models.CharField(max_length=10)
    Peso = models.CharField(max_length=4)
    Altura = models.CharField(max_length=4)
    Ancho = models.CharField(max_length=4)
    Largo = models.CharField(max_length=4)
    Operativo=(('S','Si'),('N','No'))
    Operativo=models.CharField(max_length=1, choice=Operativo,defaul='S')
    

    def Equipo(self):
        cadena="{0} {1}, {2}"
        return cadena.format(self.CodigodeInventario,self.Fabricante,self.Modelo)

    def __str__(self):
        return self.Equipo()

class EspecificacionesTecnicas(models.Model):
    PotenciaNominal = models.CharField(max_length=4)
    Voltaje = models.CharField(max_length=4)
    Amp = models.CharField(max_length=4)
    rpm = models.CharField(max_length=4)
    Hz = models.CharField(max_length=4)
    Kw = models.CharField(max_length=4)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.PotenciaNominal,self.Estado)

class sistema(models.Model):
    Equipo=models.ForeignKey(Equipo,null=False,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        cadena ="{0} => {1}" 
        return cadena.format(self.Equipo)

    







