#importo la libreria para utilizar json https://docs.python.org/3/library/json.html
#definición de json: https://www.json.org/
import json

#importo config.py donde esta jsonLocation
import config

#Obtengo todos los datos
def getData():
    #abro un archivo como json_file
    with open(config.jsonLocation) as json_file:
        #cargo el archivo excluyendo el header "db_list"
        jsonData = json.load(json_file)["db_list"]

    #retorno la informaciön como un objeto json
    return jsonData