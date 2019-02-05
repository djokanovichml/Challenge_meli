class DataBaseModel:
    def __init__(self, dbName, dbOwner, dbOwnerManager, dbClasificacion):
        self.nombreBaseDatos = dbName
        self.emailManager = dbOwnerManager
        self.clasificacion = dbClasificacion
        self.emailOwner = dbOwner
