import os
import csv
import itertools
from datetime import datetime


class DataLoader:
    def __init__(self):
        self.file_name = os.path.join(os.getcwd(), 'data', 'covid_19_data.csv')
        self.data_set_full = []
        self.data_set_grouped = []

    def prepare_data_set_full(self):
        """
        prepare the full dataset function
        :return:
        """
        reader = csv.DictReader(open(self.file_name, 'r', newline='\n'))
        for line in reader:
            _line = {k: v for k, v in line.items()}
            _line['ObservationDate'] = datetime.strptime(line['ObservationDate'], '%m/%d/%Y').strftime('%m-%d-%Y')
            self.data_set_full.append(_line)
        self.data_set_full = sorted(self.data_set_full, key=lambda x: x['ObservationDate'])

        return self.data_set_full

    def prepare_data_set_grouped(self):
        """
        prepare the grouped by date dataset function
        :return:
        """
        for key, group in itertools.groupby(self.data_set_full, key=lambda x: x['ObservationDate']):
            _group = list(group)
            self.data_set_grouped.append((key,
                                          sum([float(r.get('Confirmed')) for r in _group]),
                                          sum([float(r.get('Deaths')) for r in _group]),
                                          sum([float(r.get('Recovered')) for r in _group])
                                          ))

        return self.data_set_grouped
