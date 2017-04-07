import emil.send as s
import emil.receive as r
import emil.information as i
import time
#import emil.data as d
import re

def bot(send_reply=True):
	
	print("Bot is online")
	latest_uid = r.get_last_email_uid()
	while True:
		new_uid = r.get_last_email_uid()
		if latest_uid != new_uid:
			the_email, the_raw_email = r.get_email(new_uid)
			latest_uid = latest_uid + 1
			#print(the_email)
			#print(the_raw_email)
			write_to_file(the_raw_email)
			email_adress = read_email_adress()
			adress = email_adress[1]
			print("You got mail from {}".format(adress))
			#email_adress = get_email_adress(the_raw_email)
			if send_reply==True:
				s.sendmail(to_adress=adress, subject=i.subject_2, text=i.reply_1)
			time.sleep(5)
	
	
	
#def get_email_adress(raw_email):
#	email = raw_email.decode("utf-8")
#	match = re.findall(r'[\w\.-]+@[\w\.-]+', raw_email)
#	return email_adress
	
#bot()		
def read_email_adress():
	f = open('mail.txt', 'r')
	file = f.read()
	match = re.findall(r'[\w\.-]+@[\w\.-]+', file)
	#print(match)
	return match
	
	
#read_email_adress()


def write_to_file(email):
	file = open('mail.txt', 'w')
	text = email.decode("utf-8")
	file.write(text)
	file.close()









