from django import forms
from .models import NoConformidad, AccionCorrectiva

class NoConformidadForm(forms.ModelForm):
    class Meta:
        model = NoConformidad
        fields = ['codigo', 'fecha_apertura', 'origen', 'descripcion', 'gravedad', 'estado', 'responsable', 'producto_proceso_afectado']
        widgets = {
            'fecha_apertura': forms.DateInput(attrs={'type': 'date'}),
        }

class AccionCorrectivaForm(forms.ModelForm):
    class Meta:
        model = AccionCorrectiva
        fields = ['codigo', 'descripcion', 'fecha_prevista', 'fecha_real', 'estado', 'responsable', 'nc_asociada']
        widgets = {
            'fecha_prevista': forms.DateInput(attrs={'type': 'date'}),
            'fecha_real': forms.DateInput(attrs={'type': 'date'}),
        }