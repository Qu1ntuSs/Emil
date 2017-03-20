import imaplib
import email
import time
import sys
from io import StringIO
from email.generator import Generator
import base64
#from emil.information import *
#from information import *
#import send 
#from emil.send import sendmail
#import emil.send
import emil.send as s

chatbot = "my.automated.chatbot@gmail.com"
chatbot_password = "automatedchatbot"

def receive_email(send_reply=False):
	
	latest_uid = get_last_email_uid()
	while True:
		new_uid = get_last_email_uid()
		if latest_uid != new_uid:
			the_email = get_email(new_uid)
			latest_uid = latest_uid + 1
			print("You got mail")
			print(the_email)
			#write_to_file(the_email)
			#got_mail = True
			if send_reply==True:
				s.sendmail()
			time.sleep(5)
		
		
#def write_to_file(email):
#	file = open('mymail.txt', 'a')
#	text = email.decode("utf-8")
#	insert_newlines(text)
#	file.write("-------------------------------------------------------------------------------------" + "\n" + text)
#	file.close()	
					
def get_last_email_uid():
	result, data = email_setup()
	uid = data[0].split()[-1]
	latest_email_uid = int(float(uid))
	return latest_email_uid
	
def get_email(email_uid):
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('my.automated.chatbot@gmail.com', 'automatedchatbot')
	mail.list()
	mail.select("inbox")
	result, data = mail.uid('search', None, "ALL")
	latest_email_uid = data[0].split()[-1]
	result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	raw_email = data[0][1]
	clean_email = decode_email(raw_email)
	return clean_email
	
def get_clean_email(raw_email):
	c_email = email.message_from_bytes(raw_email)
	clean_email = c_email.get_payload(decode=True)
	return clean_email
	
def decode_email(a):
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
	
#def insert_newlines(string, every=64):
 #   return '\n'.join(string[i:i+every] for i in range(0, len(string), every))	

def email_setup():
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('my.automated.chatbot@gmail.com', 'automatedchatbot')
	mail.list()
	mail.select("inbox")
	result, data = mail.uid('search', None, "ALL")
	return result, data
	

	

receive_email(send_reply=True)