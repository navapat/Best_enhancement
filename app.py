from flask import Flask

app = Flask(__name__)

@app.route('/<string:var_1>')
def index(var_1):
    return """
        <!DOCTYPE html>
        <html>
        <body>
        <h1>Hello World</h1>
        <p>I'm Flask app</p>
        <p>Hello {}
        <button type="button">Click Me!</button>
        </body>
        </html> """ .format(var_1)
if __name__ == "__main__":
    app.run(debug = True)