from pymongo import MongoClient

host = 'localhost'  # Cambia esto al nombre de host de tu base de datos MongoDB
port = 27017  # Cambia esto al número de puerto de tu base de datos MongoDB
database_name = 'ejemplo_proyecto'  # Cambia esto al nombre de tu base de datos MongoDB

def dbConnection():
    try:
        client = MongoClient(host, port)
        db = client[database_name]
        return db
    except Exception as e:
        print("Error de conexión a la base de datos:", str(e))
        return None
