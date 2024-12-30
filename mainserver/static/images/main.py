import bs4,requests

response = requests.get('https://ipolcore.ipol.im/demo/clientApp/demo.html?id=432&key=16C970834D27F788056F1D8072A139B3')

print(response.text)