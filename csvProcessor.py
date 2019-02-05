import csv
import config

# Declaro un array vacio que es lo que voy a devolver en getData()
csvData = []

# Obtener toda la información y guardarla en un array
def getData():
    # Abrir el archivo
    with open(config.csvLocation, 'r') as csv_file:
      reader = csv.reader(csv_file)

      # Iterar en el csv y generar un nuevo item dentro del array que se va a devolver
      for row in reader:
        csvData.append({'rowId': row[0], 'userId': row[1], 'userState': row[2], 'userManager': row[3]})
    return csvData

# Funcion que recibe el nombre del owner de una base de datos y devuelve el manager
def getManagerFromOwner(ownerName):
    manager = ""

    # Se hace un for each donde se valida si el userId
    # del item del array coincide con el nombre recibido como parametro
    # en caso de ser asi, se corta el guarda el valor del manager en la variable
    # que se va a devolver y se corta el for para evitar que siga iterando
    for data in csvData:
        if (data['userId'] == ownerName):
            manager = data['userManager']
            break
    return manager