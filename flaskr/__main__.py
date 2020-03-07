"""
__main__.py
"""
import os
from flask import Flask, render_template, send_from_directory
from waitress import serve

def create_app():
    APP = Flask(__name__)
    return APP


APP = create_app()

DATA_SET = {"2020-01-02": 11, "2020-01-03": 10, "2020-01-11": 14}


@APP.route('/favicon.ico')
def favicon():
    """
    function to properly handle favicon
    :return:
    """
    return send_from_directory(os.path.join(APP.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@APP.route('/', methods=['GET'])
def main():
    """
    the main route rendering index.html
    :return:
    """
    return render_template('index.html', template_data_set=DATA_SET)


@APP.route('/<string:item>', methods=['GET'])
def item(item):
    filtered_data_set = {k: v for k, v in DATA_SET.items() if k==item}
    return render_template('details.html', template_data_set=filtered_data_set)


if __name__ == "__main__":
    serve(APP, host='0.0.0.0', port=80, threads=4)
