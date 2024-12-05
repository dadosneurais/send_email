from mail_class import sendEmail

mail_body = '''
<p> Olá, </p>
<p> Segue meu email automático </p>
'''
Subject = 'Auto mail'
From = 'petshirablade@gmail.com'
To = 'petshirablade@gmail.com'
password = 'eiepznnzrsqgzizh'

objSendMail = sendEmail(Subject, From, To, password, mail_body) # instansing the class 

returnGmail = objSendMail.sending_email()

print('Email has been sent')