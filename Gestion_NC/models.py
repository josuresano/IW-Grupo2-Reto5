from django.db import models

class Responsable(models.Model):
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsable"

    def __str__(self):
        return self.nombre + " " + self.apellidos



class NoConformidad(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    fecha_apertura = models.DateField()
    origen = models.CharField(max_length=100)
    descripcion = models.TextField()
    gravedad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    producto_proceso_afectado = models.CharField(max_length=100)
    responsable = models.ManyToManyField(Responsable, related_name='seguimiento')

    class Meta:
        verbose_name = "NoConformidad"
        verbose_name_plural = "NoConformidad"

    def __str__(self):
        return "No Conformidad: " + self.codigo


class AccionCorrectiva(models.Model):

    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    fecha_prevista = models.DateField()
    fecha_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    nc_asociada = models.ForeignKey(NoConformidad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "AccionCorrectiva"
        verbose_name_plural = "AccionCorrectiva"

    def __str__(self):
        return self.codigo
    
    