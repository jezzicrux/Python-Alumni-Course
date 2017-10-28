from flask import Flask
app = Flask(__name__)

@app.route ('/')
def index():

@app.route ('/2')
def second_page():

if __name__ == "__main__":
    app.run()
