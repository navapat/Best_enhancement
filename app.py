from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <!DOCTYPE html>
        <html>
        <body>
        <h1>Hello World</h1>
        <p>I'm Flask app</p>
        <button type="button">Click Me!</button>
        </body>
        </html> """
if __name__ == "__main__":
    app.run(debug = True)