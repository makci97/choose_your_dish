from flask import Flask

from app.dish_chooser import DishChooser


app = Flask(__name__)
dish_chooser = DishChooser()


@app.route('/')
def index():
    meat, side_dish = dish_chooser()
    return f"{meat} и {side_dish}"


if __name__ == '__main__':
    app.run()
