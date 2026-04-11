from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)
# Professional User-Agent string as requested by Wikimedia best practices
HEADERS = {'User-Agent': 'Outreachy-Smart-Auditor/1.0 (shehrbanoali2230@gmail.com)'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_status', methods=['POST'])
def check_status():
    url = request.json.get('url')
    try:
        # Timeout set to 5s to prevent the app from hanging on slow Lusophone servers
        res = requests.get(url, headers=HEADERS, timeout=5)
        return jsonify({'status': res.status_code})
    except requests.exceptions.RequestException as e:
        # Capturing the name of the error (like ConnectionError or Timeout):
        error_name = type(e).__name__
        return jsonify({'status': f'FAILED ({error_name})'})

@app.route('/get_score', methods=['POST'])
def get_score():
    url = request.json.get('url')
    qid = None
    
    # Extracting QID using Regex for Wikidata or local museum links
    if "wikidata.org" in url:
        match = re.search(r"Q\d+", url)
        if match:
            qid = match.group()
    elif "museudofutebol.org.br" in url:
        match = re.search(r"personalidades/(\d+)", url)
        if match: 
            qid = f"Q{match.group(1)}"
    
    if qid:
        api_url = f"https://www.wikidata.org/w/api.php?action=wbgetentities&ids={qid}&format=json"
        try:
            res = requests.get(api_url, headers=HEADERS, timeout=5).json()
            item = res.get('entities', {}).get(qid, {})
            
            # Metadata Scoring Logic
            score = (1 if item.get('labels') else 0) + \
                    (1 if item.get('descriptions') else 0) + \
                    len(item.get('claims', {}))
            
            return jsonify({'qid': qid, 'score': score})
        except requests.exceptions.RequestException as e:
            # Updated the API error reporting
            error_name = type(e).__name__
            print(f"Wikidata API Error: {error_name}")
            return jsonify({'score': 0, 'error': error_name})
            
    return jsonify({'score': None})

if __name__ == '__main__':
    app.run(debug=True)
