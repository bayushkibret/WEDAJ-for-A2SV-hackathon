import requests

def ai(postive_cash_flow, total_savings, total_return, user):

	url = "https://chatgpt-api8.p.rapidapi.com/"

	payload = [
		{
			"content": "hello " + "my name is " + user + "can you advice me by seeing these values?" + "my calculated posetive cash flow,total_saving and total return is " + str(postive_cash_flow) + str(total_savings) + str(total_return) + "respectively",
			"role": "user"
		}
	]
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "1a26f6e78emsh3e3f095fa8b7ed8p1aba17jsn473cca5a8951",
		"X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
	}

	response = requests.post(url, json=payload, headers=headers)
	return response.json()