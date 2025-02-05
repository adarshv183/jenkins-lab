from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline for second time!"

if __name__ == "__main__":
    app.run(debug=True)
