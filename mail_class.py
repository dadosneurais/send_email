import smtplib, email.message

class sendEmail:
    def __init__(self, Subject, From, To, password, mail_body) -> None: # my obj
        self.Subject = Subject
        self.From = From
        self.To = To
        self.password = password
        self.mail_body = mail_body

    def sending_email(self):
        mail_body = self.mail_body
        msg = email.message.Message()
        msg['Subject'] = self.Subject
        msg['From'] = self.From
        msg['To'] = self.To
        password = self.password
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(mail_body)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        return 'Email has sent'