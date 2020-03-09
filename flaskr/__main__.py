"""
__main__.py
"""
import os
import csv
import itertools
from datetime import datetime
from flask import Flask, render_template, send_from_directory
from waitress import serve

def create_app():
    APP = Flask(__name__)
    return APP


APP = create_app()

DATA_SET = []
reader = csv.DictReader(open('data/covid_19_data.csv', 'r', newline='\n'))
for line in reader:
    _line = {k:v for k,v in line.items()}
    _line['ObservationDate'] = datetime.strptime(line['ObservationDate'], '%m/%d/%Y').strftime('%m-%d-%Y')
    DATA_SET.append(_line)


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
    output = []
    for key, group in itertools.groupby(DATA_SET, key=lambda x: x['ObservationDate']):
        _group = list(group)
        output.append((key,
                       sum([float(r.get('Confirmed')) for r in _group]),
                       sum([float(r.get('Deaths')) for r in _group]),
                       sum([float(r.get('Recovered')) for r in _group])
                       ))

    labels = [x[0] for x in output]
    values_confirmed = [x[1] for x in output]
    values_deaths = [x[2] for x in output]
    values_recovered = [x[3] for x in output]

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
    filtered_data_set = [x for x in DATA_SET if x.get('ObservationDate') == item]

    return render_template('details.html', template_data_set=filtered_data_set)


if __name__ == "__main__":
    serve(APP, host='0.0.0.0', port=80, threads=4)
