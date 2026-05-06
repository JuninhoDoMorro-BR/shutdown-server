from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    subprocess.run('shutdown /s /t 0', shell=True)
    return "Desligando..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
