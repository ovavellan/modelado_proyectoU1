class Proveedores:
    def __init__(self, nombre_empresa, producto_suministrado, direccion, nombre_contacto, correo_contacto, telefono_contacto):
        self.nombre_empresa = nombre_empresa
        self.producto_suministrado = producto_suministrado
        self.direccion = direccion
        self.nombre_contacto = nombre_contacto
        self.correo_contacto = correo_contacto
        self.telefono_contacto = telefono_contacto

    def toDBCollection(self):
        return {
            'nombre_empresa': self.nombre_empresa,
            'producto_suministrado': self.producto_suministrado,
            'direccion': self.direccion,
            'nombre_contacto': self.nombre_contacto,
            'correo_contacto': self.correo_contacto,
            'telefono_contacto': self.telefono_contacto
        }
