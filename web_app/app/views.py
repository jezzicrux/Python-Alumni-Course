from flask import Flask
app = Flask(__name__)

@app.route ('/')
def index():
    greeting = "Hello"
    return f"{greeting} World"

@app.route ('/2')
def second_page():
    return ('You are on 2nd page')

if __name__ == "__main__":
    app.run()
