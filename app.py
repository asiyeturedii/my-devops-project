from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>DevOps Projesine Hos Geldin!</h1><p>Sistem su an Docker uzerinde calisiyor.</p>"

@app.route('/data')
def get_data():
    
    sample_data = {
        "status": "success",
        "message": "Veri basariyla cekildi",
        "tools": ["Docker", "GitHub Actions", "Flask"]
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)