import emil.send as s
import emil.receive as r

def bot():
	#r.receive_email(send_reply=True)
	#mail_status, email = r.receive_email(send_reply=True)
	#print(email)
	print("Bot is online")
	while True:
		mail_status, email, raw_email = r.receive_email(send_reply=True)
		print(raw_email)
		
		
#bot()		

