import random
from flask import Flask
app = Flask(__name__)
@app.route("/")
def ask():
    return "<h1> Guess a number between 0 and 9 </h1>"

Random_number = random.randint(0,9)
@app.route("/URL/<int:Guess>")
def print_gif(Guess):
    print(Random_number, Guess)
    if(Random_number == Guess):
        return '<h1> Guess a number between 0 and 9 </h1>' \
        f'<h1 style="color: red;"> You got it right the secret number was <span style="color:blue;"> {Random_number}</span></h1>' \
        '<img width= "600" src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmtmejNta2J3d3VxeDJuajl5NGZnNnV2eGtkb2E0cGMybGFhdXJhcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V0IdVIIW1y5d6/giphy.gif">'
    else:
        return '<h1> Guess a number between 0 and 9 </h1>' \
        '<img src = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGM0ZW9wcWs1bHk3dHg0aXlrMXlhNzdxczg5bHY2dGhrc2F4NmkxcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2bOND626iXpYc/giphy.gif">'
if __name__ == "__main__":
    app.run(debug=True)