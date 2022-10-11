from remotezip import RemoteZip
from bs4 import BeautifulSoup
from flask import Flask, request, render_template
import requests
import math

post_ids = []
artist = 3316400
soup = BeautifulSoup(requests.get(f'https://kemono.party/fanbox/user/{artist}').text, 'html.parser')
for o in range(1, math.ceil(int(soup.find('div', class_='paginator').small.string.split(' ')[-1]) / 25) + 1):
    soup = BeautifulSoup(requests.get(f'https://kemono.party/fanbox/user/{artist}?o={o * 25}').text, 'html.parser')
    for post in soup.find_all('article', class_='post-card'):
        post_ids.append(post.attrs.get("data-id", None))

print(post_ids)
"""
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        artist = request.form.get('artist')

        

        return soup.prettify()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000)




with RemoteZip('https://kemono.party/data/75/de/75de4d3f2f3cf3c42368bea9212fe2f4ceb46313b4cef487a054190af39276f8.zip') as zip:
    for file in zip.infolist():
        if file.filename.endswith('.png') or  file.filename.endswith('.jpg') or file.filename.endswith('.jpeg'):
            zip.extract(file.filename)
"""

