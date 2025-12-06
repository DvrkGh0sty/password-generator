
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generate_passwd(length=8):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789#@!$*=+-/'
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = int(data.get('length', 8))
    if length < 6:
        return jsonify({'error': 'Password length must be at least 6.'}), 400
    password = generate_passwd(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
