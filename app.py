from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase
from materiales import Material
from procesos import Proceso
from productos import Productos
from proveedores import Proveedores
from personal import Personal
from ventas import Ventas

app = Flask(__name__)
db = dbase.dbConnection()

# Rutas inicial de la aplicación
@app.route('/')
def home():
    return render_template('inicio.html')




#rutas para la clase materiales
@app.route('/materiales')
def materiales():
    materiales = db['materiales']
    materialesRecibidos = materiales.find()

    return render_template('materiales.html', materials=materialesRecibidos)

# Método POST
@app.route('/materiales', methods=['POST'])
def addMaterial():
    materiales = db['materiales']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    resistencia = request.form['resistencia']
    corrosion = request.form['corrosion']
    precio_kg = request.form['precio_kg']

    if nombre and descripcion and resistencia and corrosion and precio_kg:
        material = Material(nombre, descripcion, resistencia, corrosion, precio_kg)
        materiales.insert_one(material.toDBCollection())
        return redirect(url_for('materiales'))
    else:
        return notFound()

# Método DELETE
@app.route('/delete/<string:material_name>')
def deleteMaterial(material_name):
    materiales = db['materiales']
    materiales.delete_one({'nombre': material_name})
    return redirect(url_for('materiales'))

# Método PUT
@app.route('/edit/<string:material_name>', methods=['POST'])
def editMaterial(material_name):
    materiales = db['materiales']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    resistencia = request.form['resistencia']
    corrosion = request.form['corrosion']
    precio_kg = request.form['precio_kg']

    if nombre and descripcion and resistencia and corrosion and precio_kg:
        materiales.update_one({'nombre': material_name}, {'$set': {'nombre': nombre, 'descripcion': descripcion, 'resistencia': resistencia, 'corrosion': corrosion, 'precio_kg': precio_kg}})
        return redirect(url_for('materiales'))
    else:
        return notFound()
    




# Rutas para la clase Procesos
@app.route('/procesos')
def procesos():
    procesos = db['procesos']
    procesosRecibidos = procesos.find()

    return render_template('procesos.html', procesos=procesosRecibidos)

# Método POST para la clase Proceso
@app.route('/procesos', methods=['POST'])
def addProceso():
    procesos = db['procesos']
    nombre_proc = request.form['nombre_proc']
    descripcion_proc = request.form['descripcion_proc']
    temperatura_proc = request.form['temperatura_proc']
    presion_proc = request.form['presion_proc']

    if nombre_proc and descripcion_proc and temperatura_proc and presion_proc:
        proceso = Proceso(nombre_proc, descripcion_proc, temperatura_proc, presion_proc)
        procesos.insert_one(proceso.toDBCollection())
        return redirect(url_for('procesos'))
    else:
        return notFound()

# Método DELETE para la clase Proceso
@app.route('/delete-proceso/<string:proceso_name>')
def deleteProceso(proceso_name):
    procesos = db['procesos']
    procesos.delete_one({'nombre_proc': proceso_name})
    return redirect(url_for('procesos'))

# Método PUT para la clase Proceso
@app.route('/edit-proceso/<string:proceso_name>', methods=['POST'])
def editProceso(proceso_name):
    procesos = db['procesos']
    nombre_proc = request.form['nombre_proc']
    descripcion_proc = request.form['descripcion_proc']
    temperatura_proc = request.form['temperatura_proc']
    presion_proc = request.form['presion_proc']

    if nombre_proc and descripcion_proc and temperatura_proc and presion_proc:
        procesos.update_one({'nombre_proc': proceso_name}, {'$set': {'nombre_proc': nombre_proc, 'descripcion_proc': descripcion_proc, 'temperatura_proc': temperatura_proc, 'presion_proc': presion_proc}})
        return redirect(url_for('procesos'))
    else:
        return notFound()




#rutas para la clase Personal
@app.route('/personal')
def personal():
    personal = db['personal']
    personalRecibido = personal.find()

    return render_template('personal.html', staff=personalRecibido)

# Método POST
@app.route('/personal', methods=['POST'])
def addStaff():
    personal = db['personal']
    nombre_per = request.form['nombre_per']
    edad_per = request.form['edad_per']
    cargo_per = request.form['cargo_per']
    salario_per = request.form['salario_per']

    if nombre_per and edad_per and cargo_per and salario_per:
        staff = Personal(nombre_per, edad_per, cargo_per, salario_per)
        personal.insert_one(staff.toDBCollection())
        return redirect(url_for('personal'))
    else:
        return notFound()

# Método DELETE
@app.route('/delete_staff/<string:staff_name>')
def deleteStaff(staff_name):
    personal = db['personal']
    personal.delete_one({'nombre_per': staff_name})
    return redirect(url_for('personal'))

# Método PUT
@app.route('/edit_staff/<string:staff_name>', methods=['POST'])
def editStaff(staff_name):
    personal = db['personal']
    nombre_per = request.form['nombre_per']
    edad_per = request.form['edad_per']
    cargo_per = request.form['cargo_per']
    salario_per = request.form['salario_per']

    if nombre_per and edad_per and cargo_per and salario_per:
        personal.update_one({'nombre_per': staff_name}, {'$set': {'nombre_per': nombre_per, 'edad_per': edad_per, 'cargo_per': cargo_per, 'salario_per': salario_per}})
        return redirect(url_for('personal'))
    else:
        return notFound()




# Rutas para la clase Productos
@app.route('/productos')
def productos():
    productos = db['productos']
    productosRecibidos = productos.find()

    return render_template('productos.html', productos=productosRecibidos)

# Método POST para agregar un producto
@app.route('/productos', methods=['POST'])
def addProducto():
    productos = db['productos']
    nombre_prod = request.form['nombre_prod']
    descripcion_prod = request.form['descripcion_prod']
    longitud_prod = request.form['longitud_prod']
    ancho_prod = request.form['ancho_prod']
    espesor_prod = request.form['espesor_prod']
    precio_prod = request.form['precio_prod']

    if nombre_prod and descripcion_prod and longitud_prod and ancho_prod and espesor_prod and precio_prod:
        producto = Productos(nombre_prod, descripcion_prod, longitud_prod, ancho_prod, espesor_prod, precio_prod)
        productos.insert_one(producto.toDBCollection())
        return redirect(url_for('productos'))
    else:
        return notFound()

# Método DELETE para eliminar un producto
@app.route('/delete-producto/<string:producto_name>')
def deleteProducto(producto_name):
    productos = db['productos']
    productos.delete_one({'nombre_prod': producto_name})
    return redirect(url_for('productos'))

# Método PUT para editar un producto
@app.route('/edit-producto/<string:producto_name>', methods=['POST'])
def editProducto(producto_name):
    productos = db['productos']
    nombre_prod = request.form['nombre_prod']
    descripcion_prod = request.form['descripcion_prod']
    longitud_prod = request.form['longitud_prod']
    ancho_prod = request.form['ancho_prod']
    espesor_prod = request.form['espesor_prod']
    precio_prod = request.form['precio_prod']

    if nombre_prod and descripcion_prod and longitud_prod and ancho_prod and espesor_prod and precio_prod:
        productos.update_one({'nombre_prod': producto_name}, {'$set': {'nombre_prod': nombre_prod, 'descripcion_prod': descripcion_prod, 'longitud_prod': longitud_prod, 'ancho_prod': ancho_prod, 'espesor_prod': espesor_prod, 'precio_prod': precio_prod}})
        return redirect(url_for('productos'))
    else:
        return notFound()



#rutas para la clase Proveedores
@app.route('/proveedores')
def proveedores():
    proveedores = db['proveedores']
    proveedoresRecibidos = proveedores.find()

    return render_template('proveedores.html', proveedores=proveedoresRecibidos)

# Método POST
@app.route('/proveedores', methods=['POST'])
def addProveedor():
    proveedores = db['proveedores']
    nombre_empresa = request.form['nombre_empresa']
    producto_suministrado = request.form['producto_suministrado']
    direccion = request.form['direccion']
    nombre_contacto = request.form['nombre_contacto']
    correo_contacto = request.form['correo_contacto']
    telefono_contacto = request.form['telefono_contacto']

    if nombre_empresa and producto_suministrado and direccion and nombre_contacto and correo_contacto and telefono_contacto:
        proveedor = Proveedores(nombre_empresa, producto_suministrado, direccion, nombre_contacto, correo_contacto, telefono_contacto)
        proveedores.insert_one(proveedor.toDBCollection())
        return redirect(url_for('proveedores'))
    else:
        return notFound()

# Método DELETE
@app.route('/delete-proveedor/<string:proveedor_nombre_empresa>')
def deleteProveedor(proveedor_nombre_empresa):
    proveedores = db['proveedores']
    proveedores.delete_one({'nombre_empresa': proveedor_nombre_empresa})
    return redirect(url_for('proveedores'))

# Método PUT
@app.route('/edit-proveedor/<string:proveedor_nombre_empresa>', methods=['POST'])
def editProveedor(proveedor_nombre_empresa):
    proveedores = db['proveedores']
    nombre_empresa = request.form['nombre_empresa']
    producto_suministrado = request.form['producto_suministrado']
    direccion = request.form['direccion']
    nombre_contacto = request.form['nombre_contacto']
    correo_contacto = request.form['correo_contacto']
    telefono_contacto = request.form['telefono_contacto']

    if nombre_empresa and producto_suministrado and direccion and nombre_contacto and correo_contacto and telefono_contacto:
        proveedores.update_one({'nombre_empresa': proveedor_nombre_empresa}, {'$set': {'nombre_empresa': nombre_empresa, 'producto_suministrado': producto_suministrado, 'direccion': direccion, 'nombre_contacto': nombre_contacto, 'correo_contacto': correo_contacto, 'telefono_contacto': telefono_contacto}})
        return redirect(url_for('proveedores'))
    else:
        return notFound()


@app.route('/ventas')
def ventas():
    ventas = db['ventas']
    ventasRecibidas = ventas.find()

    return render_template('ventas.html', sales=ventasRecibidas)

# Método POST
@app.route('/ventas', methods=['POST'])
def addSale():
    ventas = db['ventas']
    item_vendido = request.form['item_vendido']
    cantidad_vendido = request.form['cantidad_vendido']
    fecha_venta = request.form['fecha_venta']
    precio_unitario = request.form['precio_unitario']
    nombre_cliente = request.form['nombre_cliente']
    correo_cliente = request.form['correo_cliente']
    telefono_cliente = request.form['telefono_cliente']

    if item_vendido and cantidad_vendido and fecha_venta and precio_unitario and nombre_cliente and correo_cliente and telefono_cliente:
        venta = Ventas(item_vendido, cantidad_vendido, fecha_venta, precio_unitario, nombre_cliente, correo_cliente, telefono_cliente)
        ventas.insert_one(venta.toDBCollection())
        return redirect(url_for('ventas'))
    else:
        return notFound()

# Método DELETE
@app.route('/delete_sale/<string:item_vendido>')
def deleteSale(item_vendido):
    ventas = db['ventas']
    ventas.delete_one({'item_vendido': item_vendido})
    return redirect(url_for('ventas'))

# Método PUT
@app.route('/edit_sale/<string:item_vendido>', methods=['POST'])
def editSale(item_vendido):
    ventas = db['ventas']
    item_vendido = request.form['item_vendido']
    cantidad_vendido = request.form['cantidad_vendido']
    fecha_venta = request.form['fecha_venta']
    precio_unitario = request.form['precio_unitario']
    nombre_cliente = request.form['nombre_cliente']
    correo_cliente = request.form['correo_cliente']
    telefono_cliente = request.form['telefono_cliente']

    if item_vendido and cantidad_vendido and fecha_venta and precio_unitario and nombre_cliente and correo_cliente and telefono_cliente:
        ventas.update_one({'item_vendido': item_vendido}, {'$set': {'item_vendido': item_vendido, 'cantidad_vendido': cantidad_vendido, 'fecha_venta': fecha_venta, 'precio_unitario': precio_unitario, 'nombre_cliente': nombre_cliente, 'correo_cliente': correo_cliente, 'telefono_cliente': telefono_cliente}})
        return redirect(url_for('ventas'))
    else:
        return notFound()



@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 not found'
    }

    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)
