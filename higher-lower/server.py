from flask import Flask
import random


random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess_number>")
def play(guess_number):
    if guess_number > random_number:
        return f"<h1 style='color: purple'>Your guess {guess_number} is too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/yMBRzjqgS0penXtdQT/giphy.gif'/>"
    elif guess_number < random_number:
        return f"<h1 style='color: red'>Your guess {guess_number} is too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/YiKiqMTzrQZwmF4I5N/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/PnmVZHD7NbCNYze6IV/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)