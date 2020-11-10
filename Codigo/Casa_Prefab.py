import django

class Prefab:
    cant_habitacion = 0
    cant_baño = 0
    habitacion = 500000
    baño = 750000
    amplias_ventanas = 250000
    living = 0
    comedor = 500000
    cocina = 500000
    validez_cant = True
    msg = str((cant_baño*baño) + (cant_habitacion*habitacion) + amplias_ventanas + living + comedor + cocina)

    tr_living = False
    tr_comedor = False
    tr_cocina = False
    tr_amplias_ventanas = False