import smtplib, ssl, config

# Aca van los datos de la cuenta que querés utilizar para enviar los mails
port = config.mailPort
smtp_server = config.smtpServer
sender_email = config.senderMail
password = config.mailPassword

def sendMail(model):
    receiver_email = model.to
    context = ssl.create_default_context()
    bodyMessage = getBodyMessage(model.dbName)
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, bodyMessage)

def getBodyMessage(dbName):
    return ("""\
Subject: Aprobación requerida

Se requiere aprobación para la base de datos """ + dbName)