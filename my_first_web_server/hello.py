from flask import Flask
app = Flask(__name__)
import time

# @app.route("/")
# def hello_world():
#     return "Hello, World!"
#
# if __name__ == "__main__":
#     app.run()

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)

        function()

    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()
