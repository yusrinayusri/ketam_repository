import requests as r

webpage = r.get('')
html = webpage.text

print(html)