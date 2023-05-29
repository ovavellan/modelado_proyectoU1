from pymongo import MongoClient

host = 'localhost'  
port = 27017  
database_name = 'ejemplo_proyecto'  

def dbConnection():
    try:
        client = MongoClient(host, port)
        db = client[database_name]
        return db
    except Exception as e:
        print("Error de conexión a la base de datos:", str(e))
        return None
