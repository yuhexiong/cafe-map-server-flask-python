import requests as req
import json
from flask import Flask, make_response, render_template

app = Flask(__name__)

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
}

@app.route('/')
def index():
    return render_template('index.html')

# https://cafenomad.tw/
@app.route('/taipei', methods=['GET'])
def taipei():
    url = 'https://cafenomad.tw/api/v1.2/cafes/taipei'
    res = req.get(url, headers = my_headers)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=5000
    )
