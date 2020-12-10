from CasaPrefab import CasaPrefab
from django.http import HttpResponse

class ModeloMedida():
    baños = 0
    dormitorios = 0
    living = False
    comedor = False
    habitaciones = 0
    segundoPiso = False
    ventanas = False
    cocina = 1

    if ventanas == True:
        costeVentanas = 250000
    else:
        costeVentanas = 0

    if living == True:
        costeLiving = 500000
    else:
        costeLiving = 0

    if comedor == True:
        costeComedor = 500000
    else:
        costeComedor = 0

    coste = (baños*750000) + (dormitorios*500000) + costeVentanas + costeLiving + costeComedor + 500000
    casa = CasaPrefab(baños, dormitorios, habitaciones, living, comedor, segundoPiso, ventanas, cocina, coste)