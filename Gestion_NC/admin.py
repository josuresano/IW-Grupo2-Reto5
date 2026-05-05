from django.contrib import admin
from .models import Responsable, NoConformidad, AccionCorrectiva

admin.site.register(Responsable)
admin.site.register(NoConformidad)
admin.site.register(AccionCorrectiva)
