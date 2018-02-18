from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Test page'

app.run(port=8000)

