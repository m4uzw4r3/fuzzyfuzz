import requests
import sys



def fuzzer():
	for word in sys.stdin:
		response = requests.get(url=f"http://192.168.1.57/dvwa/index.php/{word}")
		if response.status_code == 404:
			fuzzer()
	
		else:
			data = response.json()
			print(data)
			print(response.status_code)
			print(word)


fuzzer()
