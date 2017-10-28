from flask import Flask, render_template, request
app = Flask(__name__)

@app.route ('/')
def index():
    name = str.upper("Jess")
    othername = str.upper("Nessa")
    day = 'thrusday'
    return render_template('index.html', user1=name, user2=othername, today=day)

@app.route ('/page2', methods=['POST', 'GET'])
def second_page():
    name = request.args.get('name')
    if name:
        greeting = f"Hello, {name}"
    else:
        greeting = "Hello World"
    return render_template("page2.html", greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
