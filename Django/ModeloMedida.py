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
    coste = 0
    cocina = 1
    casa = CasaPrefab(baños, dormitorios, habitaciones, living, comedor, segundoPiso, ventanas, cocina, coste)