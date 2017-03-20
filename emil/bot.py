import emil.send as s
import emil.receive as r

def bot():

	mail_status, email = r.receive_email(send_reply=True)
	print(email)
	
#bot()		

