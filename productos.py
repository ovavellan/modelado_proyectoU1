class Productos:
    def __init__(self, nombre_prod, descripcion_prod, longitud_prod, ancho_prod, espesor_prod, precio_prod):
        self.nombre_prod = nombre_prod
        self.descripcion_prod = descripcion_prod
        self.longitud_prod = longitud_prod
        self.ancho_prod = ancho_prod
        self.espesor_prod = espesor_prod
        self.precio_prod = precio_prod

    def toDBCollection(self):
        return {
            'nombre_prod': self.nombre_prod,
            'descripcion_prod': self.descripcion_prod,
            'longitud_prod': self.longitud_prod,
            'ancho_prod': self.ancho_prod,
            'espesor_prod': self.espesor_prod,
            'precio_prod': self.precio_prod
        }
