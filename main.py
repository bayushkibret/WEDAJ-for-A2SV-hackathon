import requests

url = "https://google-bard1.p.rapidapi.com/"

headers = {
	"text": "Who is sundarpichai? ",
	"lang": "en",
	"psid": "agjMJtObH2L24XqvS8IK3VgKw1TTjQKiWKHk6NNP9GvXNhpxIZPxctFBGfRgew-7Nh77mw.",
	"X-RapidAPI-Key": "1a26f6e78emsh3e3f095fa8b7ed8p1aba17jsn473cca5a8951",
	"X-RapidAPI-Host": "google-bard1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())