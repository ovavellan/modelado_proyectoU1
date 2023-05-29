class Ventas:
    def __init__(self, item_vendido, cantidad_vendido, fecha_venta, precio_unitario, nombre_cliente, correo_cliente, telefono_cliente):
        self.item_vendido = item_vendido
        self.cantidad_vendido = cantidad_vendido
        self.fecha_venta = fecha_venta
        self.precio_unitario = precio_unitario
        self.nombre_cliente = nombre_cliente
        self.correo_cliente = correo_cliente
        self.telefono_cliente = telefono_cliente

    def toDBCollection(self):
        return {
            'item_vendido': self.item_vendido,
            'cantidad_vendido': self.cantidad_vendido,
            'fecha_venta': self.fecha_venta,
            'precio_unitario': self.precio_unitario,
            'nombre_cliente': self.nombre_cliente,
            'correo_cliente': self.correo_cliente,
            'telefono_cliente': self.telefono_cliente
        }
