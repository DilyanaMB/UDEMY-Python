import smtplib

my_email = 'type your email here'
password = 'type your app password here'

# 1st option

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs='test@yahoo.com',
                    msg='Subject:Automation\n\n'
                        'Hello, this is automatically send email :)')
connection.close()


# 2nd option

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='test@yahoo.com',
                        msg='Subject:Automation\n\nHello, this is automatically send email :)')

