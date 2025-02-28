import requests
import sys


#it will loop thorugh wordlist and search for API
def fuzzer():
	for word in sys.stdin:
		response = requests.get(url=f"http://enter_domain_name/{word}")
		if response.status_code == 404:
			fuzzer()
	
		else:
			data = response.json()
			print(data)
			print(response.status_code)
			print(word)


fuzzer()
