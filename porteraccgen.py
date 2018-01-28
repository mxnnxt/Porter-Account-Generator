import requests

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
email = "email@domain.com"
password = "Test123"
firstName = "John"
lastName = "Doe"

def create_account():
	print("SUBMITTING INFO.....")
	global session

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

	print("SUCCESSFULLY CREATED ACCOUNT "+email+":"+password)
	
	

create_account()
