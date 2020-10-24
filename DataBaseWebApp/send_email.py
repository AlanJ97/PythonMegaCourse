from email.mime.text import MIMEText
import  smtplib

def send_email(email, height, average_height, count ):
    #
    #
    from_email = "Aquí va el correo"
    from_passwrod = "Aqui va la password del correo de arriba"
    to_email = email
    subject="height data"
    message= "hey there, your height is <strong> %s </strong> in an average of <strong> %s </strong> with <strong> %s </strong> people registered " % (height, average_height, count)
    
    msg = MIMEText(message, 'html')
    msg['subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    
    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_passwrod)
    gmail.send_message(msg)