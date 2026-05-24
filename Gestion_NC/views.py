import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import NoConformidadSerializer, AccionCorrectivaSerializer, ResponsableSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import NoConformidad, AccionCorrectiva, Responsable
from .forms import NoConformidadForm, AccionCorrectivaForm
import procesador

logger = logging.getLogger('Gestion_NC')

def login_view(request):
    return render(request, 'HTML/login.html')


def inicio(request):
    ncs = NoConformidad.objects.all()
    acs = AccionCorrectiva.objects.all()
    resps = Responsable.objects.all()
    resumen = procesador.calcular_datos_globales(ncs, acs, resps)
    return render(request, 'HTML/inicio.html', {'datos': resumen})


def lista_nc(request):
    logger.info(f"El usuario '{request.user}' ha consultado el listado de NC")
    
    ncs_list = NoConformidad.objects.all()
    
    paginator = Paginator(ncs_list, 10)
    page_number = request.GET.get('page')
    ncs = paginator.get_page(page_number)
    
    return render(request, 'HTML/lista_nc.html', {'ncs': ncs})


def lista_acciones(request):
    logger.info(f"El usuario '{request.user}' ha consultado el listado de acciones correctivas")
    
    acciones_list = AccionCorrectiva.objects.all()
    
    paginator = Paginator(acciones_list, 10)
    page_number = request.GET.get('page')
    acciones = paginator.get_page(page_number)
    
    return render(request, 'HTML/lista_acciones.html', {'acciones': acciones})


def lista_responsables(request):
    logger.info(f"El usuario '{request.user}' ha consultado el listado de responsables")
    
    resps_list = Responsable.objects.all()
    
    paginator = Paginator(resps_list, 10)
    page_number = request.GET.get('page')
    resps = paginator.get_page(page_number) 
    return render(request, 'HTML/lista_responsables.html', {'resps': resps})


def detalle_nc(request, id_nc):
    nc = NoConformidad.objects.get(id=id_nc)
    return render(request, 'HTML/detalle_nc.html', {'nc': nc})


def alta_nc(request):
    if request.method == "POST":
        form = NoConformidadForm(request.POST)
        if form.is_valid():
            nueva_nc = form.save()
            logger.info(f"El usuario '{request.user}' ha creado con éxito la NC código [{nueva_nc.codigo}]")
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
            logger.info(f"El usuario '{request.user}' ha editado la NC código [{nc.codigo}]")
            return redirect('lista_nc')
    else:
        form = NoConformidadForm(instance=nc)
    return render(request, 'HTML/formulario_universal.html', {'form': form, 'titulo': 'Actualizar No Conformidad'})


def borrar_nc(request, id_nc):
    nc = get_object_or_404(NoConformidad, id=id_nc)
    if request.method == "POST":
        codigo_eliminado = nc.codigo
        nc.delete()
        logger.warning(f"¡AVISO! El usuario '{request.user}' ha ELIMINADO la NC código [{codigo_eliminado}]")
        return redirect('lista_nc')
    return render(request, 'HTML/confirmar_borrado.html', {'objeto': nc, 'volver': 'lista_nc'})


def alta_accion(request):
    if request.method == "POST":
        form = AccionCorrectivaForm(request.POST)
        if form.is_valid():
            nueva_accion = form.save()
            logger.info(f"El usuario '{request.user}' ha registrado una nueva Acción Correctiva ID [{nueva_accion.id}]")
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
            logger.info(f"El usuario '{request.user}' ha actualizado la Acción Correctiva ID [{ac.id}]")
            return redirect('lista_acciones')
    else:
        form = AccionCorrectivaForm(instance=ac)
    return render(request, 'HTML/formulario_universal.html', {'form': form, 'titulo': 'Actualizar Acción'})


def borrar_accion(request, id_ac):
    ac = get_object_or_404(AccionCorrectiva, id=id_ac)
    if request.method == "POST":
        id_eliminado = ac.id
        ac.delete()
        logger.warning(f"¡AVISO! El usuario '{request.user}' ha ELIMINADO la Acción Correctiva ID [{id_eliminado}]")
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
        logger.info(f"API: El usuario '{request.user}' ha solicitado listado JSON de NC")
        ncs = NoConformidad.objects.all()
        return Response(NoConformidadSerializer(ncs, many=True).data)
    
class AccionCorrectivaListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info(f"API: El usuario '{request.user}' ha solicitado listado JSON de Acciones")
        acciones = AccionCorrectiva.objects.all()
        return Response(AccionCorrectivaSerializer(acciones, many=True).data)
    
class ResumenPublicoAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'total_responsables': Responsable.objects.count(),
        })