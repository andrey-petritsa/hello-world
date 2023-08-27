from flask import Flask

class Main:
    def __init__(self):
        pass

    def run(self):
        app = Flask(__name__)

        @app.route("/")
        def hello_world():
            return "<p>Hello, World!</p>"

        app.run(debug=True)

main = Main()
main.run()
