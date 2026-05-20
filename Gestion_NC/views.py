import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import NoConformidadSerializer, AccionCorrectivaSerializer, ResponsableSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import NoConformidad, AccionCorrectiva, Responsable
from .forms import NoConformidadForm, AccionCorrectivaForm
import procesador

logger = logging.getLogger(__name__)

def login_view(request):
    return render(request, 'HTML/login.html')


def inicio(request):
    ncs = NoConformidad.objects.all()
    acs = AccionCorrectiva.objects.all()
    resps = Responsable.objects.all()
    resumen = procesador.calcular_datos_globales(ncs, acs, resps)
    return render(request, 'HTML/inicio.html', {'datos': resumen})

def lista_nc(request):
    ncs = NoConformidad.objects.all()
    return render(request, 'HTML/lista_nc.html', {'ncs': ncs})

def lista_acciones(request):
    acciones = AccionCorrectiva.objects.all()
    return render(request, 'HTML/lista_acciones.html', {'acciones': acciones})

def lista_responsables(request):
    resps = Responsable.objects.all()
    return render(request, 'HTML/lista_responsables.html', {'resps': resps})

def detalle_nc(request, id_nc):
    nc = NoConformidad.objects.get(id=id_nc)
    return render(request, 'HTML/detalle_nc.html', {'nc': nc})

# --- Gestión No Conformidades (CRUD) ---

def alta_nc(request):
    if request.method == "POST":
        form = NoConformidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_nc')
    else:
        form = NoConformidadForm()
    return render(request, 'HTML/formulario_universal.html', {'form': form, 'titulo': 'Alta de No Conformidad'})

def editar_nc(request, id_nc):
    nc = get_object_or_404(NoConformidad, id=id_nc)
    if request.method == "POST":
        form = NoConformidadForm(request.POST, instance=nc)
        if form.is_valid():
            form.save()
            return redirect('lista_nc')
    else:
        form = NoConformidadForm(instance=nc)
    return render(request, 'HTML/formulario_universal.html', {'form': form, 'titulo': 'Actualizar No Conformidad'})

def borrar_nc(request, id_nc):
    nc = get_object_or_404(NoConformidad, id=id_nc)
    if request.method == "POST":
        nc.delete()
        return redirect('lista_nc')
    return render(request, 'HTML/confirmar_borrado.html', {'objeto': nc, 'volver': 'lista_nc'})

# --- Gestión Acciones Correctivas (CRUD) ---

def alta_accion(request):
    if request.method == "POST":
        form = AccionCorrectivaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_acciones')
    else:
        form = AccionCorrectivaForm()
    return render(request, 'HTML/formulario_universal.html', {'form': form, 'titulo': 'Nueva Acción Correctiva'})

def editar_accion(request, id_ac):
    ac = get_object_or_404(AccionCorrectiva, id=id_ac)
    if request.method == "POST":
        form = AccionCorrectivaForm(request.POST, instance=ac)
        if form.is_valid():
            form.save()
            return redirect('lista_acciones')
    else:
        form = AccionCorrectivaForm(instance=ac)
    return render(request, 'HTML/formulario_universal.html', {'form': form, 'titulo': 'Actualizar Acción'})

def borrar_accion(request, id_ac):
    ac = get_object_or_404(AccionCorrectiva, id=id_ac)
    if request.method == "POST":
        ac.delete()
        return redirect('lista_acciones')
    return render(request, 'HTML/confirmar_borrado.html', {'objeto': ac, 'volver': 'lista_acciones'})

class MiPerfilAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info(f"Perfil consultado por {request.user.username}")
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
        })

class NoConformidadListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ncs = NoConformidad.objects.all()
        return Response(NoConformidadSerializer(ncs, many=True).data)
    
class AccionCorrectivaListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        acciones = AccionCorrectiva.objects.all()
        return Response(AccionCorrectivaSerializer(acciones, many=True).data)
    
class ResumenPublicoAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'total_responsables': Responsable.objects.count(),
        })
   
