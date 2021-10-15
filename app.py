import random
from random import choice
from flask import Flask, render_template

images_path = [
    "https://raw.githubusercontent.com/aryan-jadon/serverless-assignment-fall2021/main/templates/images/1.jpg",
    "https://raw.githubusercontent.com/aryan-jadon/serverless-assignment-fall2021/main/templates/images/2.jpg",
    "https://raw.githubusercontent.com/aryan-jadon/serverless-assignment-fall2021/main/templates/images/3.jpg",
    "https://raw.githubusercontent.com/aryan-jadon/serverless-assignment-fall2021/main/templates/images/4.jpg",
    "https://raw.githubusercontent.com/aryan-jadon/serverless-assignment-fall2021/main/templates/images/5.jpg",
    "https://raw.githubusercontent.com/aryan-jadon/serverless-assignment-fall2021/main/templates/images/6.jpg"
]

lazy_quotes = [
    "In a cat's eye, all things belong to cats.",
    "If cats could write history, their history would be mostly about cats.",
    "Cats are connoisseurs of comfort.",
    "As every cat owner knows, nobody owns a cat.",
    "If cats could talk, they wouldn’t.",
    "The only thing a cat worries about is what's happening right now."
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_random_quote():
    return render_template('index.html',
                           image_link=images_path[random.randint(0, 5)],
                           quote=lazy_quotes[random.randint(0, 5)])
