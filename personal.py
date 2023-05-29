class Personal:
    def __init__(self, nombre_per, edad_per, cargo_per, salario_per):
        self.nombre_per = nombre_per
        self.edad_per = edad_per
        self.cargo_per = cargo_per
        self.salario_per = salario_per

    def toDBCollection(self):
        return {
            'nombre_per': self.nombre_per,
            'edad_per': self.edad_per,
            'cargo_per': self.cargo_per,
            'salario_per': self.salario_per,
        }