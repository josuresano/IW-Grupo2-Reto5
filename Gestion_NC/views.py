from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import NoConformidad, AccionCorrectiva, Responsable
from .forms import NoConformidadForm, AccionCorrectivaForm

def inicio(request):
    ncs = NoConformidad.objects.all()
    acs = AccionCorrectiva.objects.all()
    resps = Responsable.objects.all()
    
    resumen = {
        'total_nc': ncs.count(),
        'total_acciones': acs.count(),
        'total_responsables': resps.count(),
        'nc_abiertas': ncs.filter(estado__icontains="abierta").count(),
        'nc_cerradas': ncs.filter(estado__icontains="cerrada").count(),
    }
    
    return render(request, 'HTML/inicio.html', {'datos': resumen})



def lista_nc(request):
    query = request.GET.get('q', '').strip()
    if query:
        ncs = NoConformidad.objects.filter(codigo__icontains=query)
    else:
        ncs = NoConformidad.objects.all()
    return render(request, 'HTML/lista_nc.html', {'ncs': ncs, 'query': query})


def lista_acciones(request):
    query = request.GET.get('q', '').strip()
    if query:

        acciones = AccionCorrectiva.objects.filter(
            Q(descripcion__icontains=query) | 
            Q(estado__icontains=query) |
            Q(nc_asociada__codigo__icontains=query)
        )
    else:
        acciones = AccionCorrectiva.objects.all()
    return render(request, 'HTML/lista_acciones.html', {'acciones': acciones, 'query': query})


def lista_responsables(request):
    query = request.GET.get('q', '').strip()
    if query:
        resps = Responsable.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellidos__icontains=query) | 
            Q(email__icontains=query)
        )
    else:
        resps = Responsable.objects.all()
    return render(request, 'HTML/lista_responsables.html', {'resps': resps, 'query': query})



def detalle_nc(request, id_nc):
    nc = get_object_or_404(NoConformidad, id=id_nc)
    return render(request, 'HTML/detalle_nc.html', {'nc': nc})


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