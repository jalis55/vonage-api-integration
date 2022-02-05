import vonage

client=vonage.Client(Key="fc9426bb",secret="Goodway98")
sms=vonage.sms(client)
def send_sms(num):
	responseData=sms.send_message({
	"from":"Hello",
	"to":num,
	"text":"hello this is test mesage"
	})
	if responseData["message"][0]["status"] =="0":
		print("Message sent successfully")
	else:
		 print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
	


file=open('numbers.txt','r')
numbers=file.readlines()

for number in numbers:
	send_sms(number)