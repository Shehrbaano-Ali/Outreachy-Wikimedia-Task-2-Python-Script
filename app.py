from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)
HEADERS = {'User-Agent': 'Outreachy-Smart-Auditor/1.0'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_status', methods=['POST'])
def check_status():
    url = request.json.get('url')
    try:
        res = requests.get(url, headers=HEADERS, timeout=5)
        return jsonify({'status': res.status_code})
    except:
        return jsonify({'status': 'FAILED'})

@app.route('/get_score', methods=['POST'])
def get_score():
    url = request.json.get('url')
    qid = None
    if "wikidata.org" in url:
        qid = re.search(r"Q\d+", url).group()
    elif "museudofutebol.org.br" in url:
        match = re.search(r"personalidades/(\d+)", url)
        if match: qid = f"Q{match.group(1)}"
    
    if qid:
        api_url = f"https://www.wikidata.org/w/api.php?action=wbgetentities&ids={qid}&format=json"
        try:
            res = requests.get(api_url, headers=HEADERS).json()
            item = res.get('entities', {}).get(qid, {})
            score = (1 if item.get('labels') else 0) + (1 if item.get('descriptions') else 0) + len(item.get('claims', {}))
            return jsonify({'qid': qid, 'score': score})
        except: return jsonify({'score': 0})
    return jsonify({'score': None})

if __name__ == '__main__':
    app.run(debug=True)