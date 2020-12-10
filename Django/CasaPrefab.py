class CasaPrefab():
    def __init__(self, baños, dormitorios, habitaciones, living, comedor, segundoPiso, ventanas, cocina,coste):
        self.nmroBaños = baños
        self.nmroDormitorio = dormitorios
        self.nmroHabitaciones = habitaciones
        self.trliving = living
        self.trcomedor = comedor
        self.trsegundoPiso = segundoPiso
        self.trampliasVentanas = ventanas
        self.cocina = cocina
        self.coste = coste
        filtroCasa()

        def filtroCasa(nmroBaños, nmroDormitorio):
            if baños < 0 or baños > 2:
                print("error: la cantidad de baños exeden el limite, ah, y no alcanzamos a implementar django aca")
                return
            elif dormitorios < 0 or baños > 4:
                print("error: la cantidad de dormitorios exeden el limite, ah, y no alcanzamos a implementar django aca")
                return