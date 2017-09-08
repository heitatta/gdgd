from flask import Flask
from flask_ask import Ask, statement, question
from random import randint

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def handle_launch():
    return question('カフェ&バー ぐだぐだへようこそ')


suggest_list = ['うどん', 'すし', 'ラーメン']


@ask.intent('DishIntent', convert={'dish': str})
def handle_dish_intent(dish):
    suggest = suggest_list[randint(0, len(suggest_list) - 1)]
    return statement(dish + 'には' + suggest + 'がいいんじゃないかな')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
