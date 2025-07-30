from flask import Flask, render_template, request, jsonify
from conversions import ConversionEngine
from calculator import Calculator
import json, os

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Load options from Home Assistant
OPTIONS_PATH = '/data/options.json'
def load_options():
    if os.path.exists(OPTIONS_PATH):
        with open(OPTIONS_PATH) as f:
            return json.load(f)
    return {}

conversion_engine = ConversionEngine()
calculator = Calculator()

@app.route('/')
def index():
    options = load_options()
    return render_template('calculator.html', options=options)

@app.route('/<service>')
def service_page(service):
    options = load_options()
    if service in ['weight','liquid','distance','temperature','area','speed','cooking']:
        return render_template(f'{service}.html', options=options)
    return render_template('calculator.html', options=options)

@app.route('/api/convert', methods=['POST'])
def api_convert():
    data = request.json
    result = conversion_engine.convert(data)
    return jsonify(result)

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    data = request.json
    result = calculator.process(data)
    return jsonify(result)

@app.route('/api/options')
def api_options():
    return jsonify(load_options())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099)
