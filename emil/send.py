import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from emil.information import *


def sendmail(subject="Sent by my Bot", text="No Reply", to_adress=jakob2, number_of_emails=1):
	
	msg = MIMEMultipart()
	msg['From'] = chatbot
	msg['To'] = to_adress
	msg['Subject'] = subject

	msg.attach(MIMEText(text, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(chatbot, chatbot_password)
	body = msg.as_string()

	i = 0
	while i < number_of_emails:
		server.sendmail(chatbot, to_adress, body)
		i = i + 1
		time.sleep(0.5)
	server.quit()

	print ("{} email(s) sent to {}".format(number_of_emails, to_adress))

