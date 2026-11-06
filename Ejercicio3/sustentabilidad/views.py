"""Vistas de la app sustentabilidad."""
from django.shortcuts import render
from core.metricas import obtener_metricas_consumo

# Create your views here.


def vista_panel_sustentabilidad(request):
    """Vista del panel de sustentabilidad."""
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 850},
        {"planta": "Planta Centro", "consumo_kwh": 1500},
    ]
    
    metricas = obtener_metricas_consumo(registros)
    
    contexto = {
        "titulo": "Panel de Sustentabilidad",
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "detalle": metricas["detalle"],
        "unidad": "kg CO2",
    }
    
    return render(request, "sustentabilidad/panel.html", contexto)