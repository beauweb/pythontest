from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask API",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": "2025-01-02T18:11:06+05:30"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
