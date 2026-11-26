from flask import Flask

app = Flask(__name__)

@app.route("/micro2")
def micro2():
    return "This is Microservice 2!"

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)