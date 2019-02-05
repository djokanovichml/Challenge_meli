import jsonProcessor
import csvProcessor
import dataBaseProcessor
import mailProcessor
from Entities.dataBaseModel import DataBaseModel
from Entities.mailModel import MailModel

# 1) obtengo la informacion del json (ir a jsonProcessor.py para ver el paso a paso)
jsonData = jsonProcessor.getData()

# 2) obtengo la informacion del csv (ir a csvProcessor.py para ver el paso a paso)
csvData = csvProcessor.getData()

# 3) Itero por cada valor que se encuentre en el jsonData
for data in jsonData:

    # Guardo el valor del nombre de la base de datos en una variable y la imprimo en consola
    dbName = data["dn_name"]
    print("Nombre de la base de datos: " + dbName)

    # Si el objeto owner contiene el mail, sigo adelante,
    # sino lo informo y continuo con el siguiente registro
    if 'email' in data["owner"]:
        dbOwnerMail = data["owner"]["email"]
        dbOwnerUserId = data["owner"]["uid"]
        print("  Owner: " + dbOwnerUserId + " mail: " + dbOwnerMail)

        # Obtengo el mail del manager utilizando el metodo de csvProcessor.py
        dbOwnerManager = csvProcessor.getManagerFromOwner(dbOwnerUserId)
        print("  Manager del owner: " + dbOwnerManager)

        dbConfidentiality = data["classification"]["confidentiality"]
        print("  Confidencialidad: " + dbConfidentiality)

        # Genero el objeto con los datos que voy a persistir en la base de datos
        dbModel = DataBaseModel(dbName, dbOwnerMail, dbOwnerManager, dbConfidentiality)

        # Guardo en la base de datos
        dataBaseProcessor.SaveRecord(dbModel)

        # Si la confidencialidad es alta, envío mail al manager del owner
        # En caso de que no lo sea, no envío nada
        if dbConfidentiality == "high":
            # Armo el modelo
            mailModel = MailModel(dbOwnerMail, dbName, dbOwnerManager)

            #Envío el mail
            mailProcessor.sendMail(mailModel)
            print("  Mail enviado a " + dbOwnerManager)
    else:
        print("!!! No existe el mail del usuario en la db: " + dbName)\
