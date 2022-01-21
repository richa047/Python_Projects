import smtplib 
#from email.message import EmailMessage
content = 'example email stuff'

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('email','password')
mail.semdmail('rpricha4@gmail.com','rpricha4@gmail.com',content)
mail.close()




#command-   pip install secure-smtplib
#status- 