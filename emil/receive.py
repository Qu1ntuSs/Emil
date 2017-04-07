import imaplib
import email
import time
import sys
from io import StringIO
from email.generator import Generator
import base64
import emil.send as s
import emil.information as i

#chatbot = "my.automated.chatbot@gmail.com"
#chatbot_password = "automatedchatbot"

def receive_email(send_reply=False):
	
	latest_uid = get_last_email_uid()
	
	while True:
		new_uid = get_last_email_uid()
		if latest_uid != new_uid:
			the_email, the_raw_email = get_email(new_uid)
			latest_uid = latest_uid + 1
			print("You got mail")
			print(the_email)
			print(the_raw_email)
			#write_to_file(the_email)
			#got_mail = True
			if send_reply==True:
				s.sendmail()
			time.sleep(5)
			
		

					
def get_last_email_uid():
	result, data = email_setup()
	uid = data[0].split()[-1]
	latest_email_uid = int(float(uid))
	return latest_email_uid
	
def get_email(email_uid):
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(i.chatbot, i.chatbot_password)
	mail.list()
	mail.select("inbox")
	result, data = mail.uid('search', None, "ALL")
	latest_email_uid = data[0].split()[-1]
	result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	raw_email = data[0][1]
	clean_email = decode_email(raw_email)
	return clean_email, raw_email
	

	
def decode_email(a):
	#b = email.message_from_string(a)
	b = email.message_from_bytes(a)
	body = ""
	if b.is_multipart():
		for part in b.walk():
			ctype = part.get_content_type()
			cdispo = str(part.get('Content-Disposition'))
			
			if ctype == 'text/plain' and 'attachment' not in cdispo:
				body = part.get_payload(decode=True)  
				break
	else:
		body = b.get_payload(decode=True)
	return body
	

def email_setup():
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(i.chatbot, i.chatbot_password)
	mail.list()
	mail.select("inbox")
	result, data = mail.uid('search', None, "ALL")
	return result, data
	


#receive_email(send_reply=True)
