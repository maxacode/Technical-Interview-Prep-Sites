import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '4175228598',
  'message': 'Hello Maks from TextBelft',
  'key': 'textbelt',
})
print(resp.json())