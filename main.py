from flask import Flask

class Main:
    def __init__(self):
        pass

    def run(self):
        app = Flask(__name__)

        @app.route("/")
        def hello_world():
            return "<p>Hello, World! How are you what is your name</p>"

        sapp.run(host='0.0.0.0')

main = Main()
main.run()
