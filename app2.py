# app2_receiver.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    print(f"[Receiver] Received data: {data}")
    return {"status": "received"}

if __name__ == '__main__':
    app.run(port=5000)