from app import app
from flask import render_template, request, session

# from models.user_model import *


@app.route('/', methods=['get', 'post'])
def user():
    html = render_template(
        'user.html'
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)