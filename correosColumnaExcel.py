import smtplib
import pandas as pd

# Abrir archivo de Excel
data = pd.read_excel('data.xlsx')

# Obtener correos electrónicos de la columna AJ omitiendo el primer campo
emails = data['AJ'].tolist()[1:]

# Configurar servidor SMTP y credenciales
smtp_server = "smtp.example.com"  # Reemplazar con servidor SMTP real
port = 587  # Reemplazar con puerto SMTP real
sender_email = "tucorreo@ejemplo.com"  # Reemplazar con tu correo electrónico
sender_password = "tucontraseña"  # Reemplazar con tu contraseña

# Asunto y mensaje del correo electrónico
subject = "Asunto del correo electrónico"
message = """
**Cuerpo del mensaje del correo electrónico**

**Puedes personalizar el mensaje aquí.**

Atentamente,

**Tu nombre**
"""

# Crear conexión SMTP
with smtplib.SMTP(smtp_server, port) as server:
    # Iniciar sesión en el servidor SMTP
    server.starttls()
    server.login(sender_email, sender_password)

    # Enviar correos electrónicos a cada dirección de correo electrónico
    for email in emails:
        # Preparar el mensaje del correo electrónico
        email_message = f"Subject: {subject}\n\n{message}"

        # Enviar el correo electrónico
        server.sendmail(sender_email, email, email_message)
        print(f"Correo electrónico enviado a: {email}")
