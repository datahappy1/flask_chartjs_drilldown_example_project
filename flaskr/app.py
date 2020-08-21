"""
__main__.py
"""
import os
from flask import Flask, render_template, send_from_directory
from waitress import serve
from flaskr.data import data_loader


def create_app():
    APP = Flask(__name__)
    return APP


APP = create_app()

# load the data sets from the covid_19_data.csv
dlo = data_loader.DataLoader()
DATA_SET_FULL = data_loader.DataLoader.prepare_data_set_full(dlo)
DATA_SET_GROUPED = data_loader.DataLoader.prepare_data_set_grouped(dlo)


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
    labels = [x[0] for x in DATA_SET_GROUPED]
    values_confirmed = [x[1] for x in DATA_SET_GROUPED]
    values_deaths = [x[2] for x in DATA_SET_GROUPED]
    values_recovered = [x[3] for x in DATA_SET_GROUPED]

    return render_template('index.html', template_labels=labels,
                           template_values_confirmed=values_confirmed,
                           template_values_deaths=values_deaths,
                           template_values_recovered=values_recovered)


@APP.route('/<string:item>', methods=['GET'])
def item(item):
    """
    the route for each "drilldown" item
    :param item:
    :return:
    """
    filtered_data_set = [x for x in DATA_SET_FULL if x.get('ObservationDate') == item]

    return render_template('details.html', template_data_set=filtered_data_set)


if __name__ == "__main__":
    serve(APP, host='0.0.0.0', port=80, threads=4)
