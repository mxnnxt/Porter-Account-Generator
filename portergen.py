import requests
import time
from random import getrandbits

print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " - Mr Porter account creator")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " - Developed by @mxnnxt")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------\n")

session = requests.session()

headers = {
    "Connection": "keep-alive",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"Upgrade-Insecure-Requests": "1",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.9"
}
#EDIT THIS
prefix = "test"
domain = "@gmail.com"

password = "Test123"
firstName = "John"
lastName = "Doe"



times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of account(s) you would like to create: ")))

text_file = open("Accounts.txt", "w")



def create_account():
	
	print("[" + (time.strftime("%H:%M:%S")) + "]" + " - SUBMITTING INFO.....")
	global session
	global email

	email = (prefix + "{}" + domain).format(getrandbits(40))
	
	
	url = "https://www.mrporter.com/am/en-us/lightRegistration.mrp"
	payload = {
		"title":"Mr",
		"firstName":firstName,
		"lastName":lastName,
		"email":email,
		"emailConfirmIfError":"false",
		"password":password,
		"verifyPassword":password,
		"country":"US",
		"_optOutOfMailList":"on"
	}

	response = session.post(url, data = payload, headers = headers)

	if "Thank" in response.text:
		print("[" + (time.strftime("%H:%M:%S")) + "]" +" - SUCCESSFULLY CREATED ACCOUNT "+email+":"+password)
		write()
	else:
		print("[" + (time.strftime("%H:%M:%S")) + "]" +" - ERROR COULD NOT CREATE "+email+":"+password)

def write():

    text_file.write(email + ":" + password + "\n")
	

for i in range (times):
    create_account()
