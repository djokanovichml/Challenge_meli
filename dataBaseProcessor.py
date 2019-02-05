import pymysql
import config

# Recibe un objeto del tipo dataBaseModel.py y lo guarda en la base de datos
def SaveRecord(record):

    connection = pymysql.connect(host=config.dbHost,
                                 user=config.dbUser,
                                 password=config.dbPassword,
                                 db=config.dbName,
                                 charset=config.dbCharset,
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `datos` (`nombreBaseDatos`, `emailOwner`, `emailManager`, `clasificacion`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (record.nombreBaseDatos, record.emailOwner, record.emailManager, record.clasificacion))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()