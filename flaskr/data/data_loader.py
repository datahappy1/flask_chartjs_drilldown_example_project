import os
import csv
import itertools
from datetime import datetime


class DataLoader:
    def __init__(self):
        self.file_name = os.path.join(os.getcwd(), 'data', 'covid_19_data.csv')
        self.data_set_raw = []
        self.data_set_grouped = []

    def prepare_data_set_raw(self):
        reader = csv.DictReader(open(self.file_name, 'r', newline='\n'))
        for line in reader:
            _line = {k: v for k, v in line.items()}
            _line['ObservationDate'] = datetime.strptime(line['ObservationDate'], '%m/%d/%Y').strftime('%m-%d-%Y')
            self.data_set_raw.append(_line)
        return self.data_set_raw

    def prepare_data_set_grouped(self):
        for key, group in itertools.groupby(self.data_set_raw, key=lambda x: x['ObservationDate']):
            _group = list(group)
            self.data_set_grouped.append((key,
                                          sum([float(r.get('Confirmed')) for r in _group]),
                                          sum([float(r.get('Deaths')) for r in _group]),
                                          sum([float(r.get('Recovered')) for r in _group])
                                          ))
        return self.data_set_grouped
