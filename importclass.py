from mail_class import sendEmail

mail_body = '''
<p> Hi, </p>
<p> This is an auto sender mail </p>
'''
Subject = 'Auto mail'
From = 'enter with the sender mail'
To = 'enter with the receiver mail' # you can add more emails, just separete them with the comma.
password = 'enter with the app passwords security from the gmail'

objSendMail = sendEmail(Subject, From, To, password, mail_body) # instansing the class 

returnGmail = objSendMail.sending_email()

print('Email has been sent')
