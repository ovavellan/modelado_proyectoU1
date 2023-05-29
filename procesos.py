class Proceso:
    def __init__(self, nombre_proc, descripcion_proc, temperatura_proc, presion_proc):
        self.nombre_proc = nombre_proc
        self.descripcion_proc = descripcion_proc
        self.temperatura_proc = temperatura_proc
        self.presion_proc = presion_proc

    def toDBCollection(self):
        return {
            'nombre_proc': self.nombre_proc,
            'descripcion_proc': self.descripcion_proc,
            'temperatura_proc': self.temperatura_proc,
            'presion_proc': self.presion_proc,
        }