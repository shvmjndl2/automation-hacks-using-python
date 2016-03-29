import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import getpass
import random
import time

def send_message(fromaddr,password ,toaddr,subject,body):

	toaddr = toaddr.split(',')
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = ", ".join(toaddr)
	msg['Subject'] = subject
 
 
	msg.attach(MIMEText(body, 'plain'))
 	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, password)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

recipients={
         'shivam jindal':'shvmjndl2@gmail.com',
          'sachin':'rsachin587@gmail.com',
}



def generate_excuse(recipient,receiveraddr,excuse):
	date=time.strftime("%x");
	resultText='Respected %s,\n\nI am unable to attend the lectures of today because of %s. Please grant me the attendance for today %s.\n\nThanking you\nYours Sincerely\n %s '%(recipient,excuse,date,'shivam jindal ');
	send_message(sender,passwd,receiveraddr,'Application for leave letter',resultText);	
	print 'Emails were sent succesfully';
	

sender="shvmjndl2@gmail.com"

print sender;
passwd=getpass.getpass();
index=random.randint(0,3);

excuses=['High fever. I will provide the medical certificate as soon as i get back',' a doctor checkup . I will provide the medical certificate as soon as i get back',' family problems. I apologize for my inability to attend the classes',' a close friend''s accident. I had to take him to the hospital ' ]; 

for name,eid in recipients.iteritems():
	generate_excuse(name,eid,excuses[index]);
	
