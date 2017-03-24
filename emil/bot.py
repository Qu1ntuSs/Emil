import emil.send as s
import emil.receive as r
import emil.information as i
import time

def bot(send_reply=True):
	
	print("Bot is online")
	latest_uid = r.get_last_email_uid()
	while True:
		new_uid = r.get_last_email_uid()
		if latest_uid != new_uid:
			the_email, the_raw_email = r.get_email(new_uid)
			latest_uid = latest_uid + 1
			print("You got mail")
			print(the_email)
			print(the_raw_email)
			email_adress = get_email_adress(the_raw_email)
			if send_reply==True:
				s.sendmail(to_adress=email_adress)
			time.sleep(5)
	
	
	
def get_email_adress(raw_email):
	return email_adress
	
#bot()		

