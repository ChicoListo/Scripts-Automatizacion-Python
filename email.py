import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos de la cuenta de correo
sender_email = "tu_correo@gmail.com"
receiver_email = "correo_destinatario@gmail.com"
password = input("Introduce tu contraseña: ")

# Configuración del mensaje
message = MIMEMultipart("alternative")
message["Subject"] = "Correo automatizado"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Hola,
Este es un correo automatizado desde Python.
"""
html = """\
<html>
<body>
<p>Hola,<br>
Este es un correo <b>automatizado</b> desde Python.
</p>
</body>
</html>
"""

# Crear partes del mensaje
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Adjuntar partes al mensaje
message.attach(part1)
message.attach(part2)

# Conexión al servidor SMTP de Gmail
try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Correo enviado correctamente")
except Exception as e:
    print("Error al enviar el correo:", e)
finally:
    server.quit()