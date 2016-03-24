# this automation hack is used to froward the emails of your gmail account

import smtplib, imaplib, email, string

imap_host = "imap.gmail.com"
imap_port = 993
smtp_host = "smtp.gmail.com"
smtp_port = 587
user = "email@gmail.com"
passwd = "excelsior8"
msgid = 1
from_addr = "email@gmail.com"
to_addr = "email1@gmail.com"


# open IMAP connection and fetch message with id msgid
# store message data in email_data
client = imaplib.IMAP4_SSL(imap_host, imap_port)
client.login(user, passwd)
client.select()
typ, data = client.search(None, 'ALL')
for mail in data[0].split():
    typ, data = client.fetch(msgid, "(RFC822)")
    email_data = data[0][1]
client.close()
client.logout()


# create a Message instance from the email data
message = email.message_from_string(email_data)

# replace headers (could do other processing here)
message.replace_header("From", from_addr)
message.replace_header("To", to_addr)
print message.as_string()

# open authenticated SMTP connection and send message with
# specified envelope from and to addresses
smtp = smtplib.SMTP(smtp_host, smtp_port)
smtp.set_debuglevel(1)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(user, passwd)
smtp.sendmail(from_addr, to_addr, 'test') 
smtp.quit()
