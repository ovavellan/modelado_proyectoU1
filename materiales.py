class Material:
    def __init__(self, nombre, descripcion, resistencia, corrosion, precio_kg):
        self.nombre = nombre
        self.descripcion = descripcion
        self.resistencia = resistencia
        self.corrosion = corrosion
        self.precio_kg = precio_kg

    def toDBCollection(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'resistencia': self.resistencia,
            'corrosion': self.corrosion,
            'precio_kg': self.precio_kg
        }
