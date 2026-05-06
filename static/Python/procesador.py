def calcular_datos_globales(ncs, acciones, responsables):
    total_nc = ncs.count()
    abiertas = ncs.filter(estado='Abierta').count()

    total_ac = acciones.count()
    finalizadas = acciones.filter(estado='Finalizada').count()

    total_responsables = responsables.count()

    return {
        'total_nc': total_nc,
        'abiertas_nc': abiertas,
        'total_ac': total_ac,
        'finalizadas_ac': finalizadas,
        'total_responsables': total_responsables
    }