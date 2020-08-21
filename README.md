# Flask, Chart.js drilldown example project
Flask and Chart.js example project allowing the web application user to drilldown to the detailed data through the main chart data point.
In the current version of Chart.js library (March 2020), this functionality is not available. The chart datapoint drilldown feature is covered
<a href="https://github.com/datahappy1/flask_chartjs_drilldown_example_project/blob/master/flaskr/templates/index.html#L71">here</a>.

This example repository uses the Kaggle "covid19" dataset. 

*Currently designed to run on Windows, but if you replace Waitress WSGI with Gunicorn for instance, can
run also on *nix based OS

## Screenshots from the web app
![alt text][screens]

[screens]: https://github.com/datahappy1/flask_chartjs_drilldown_example_project/blob/master/flaskr/docs/screens_gif.gif "screens"


## How to get started
1) Git clone this repository
2) Create and activate yourself a Python virtual environment
3) run `pip3 install -r requirements.txt`
4) set your Windows Python working directory to `C:\<<<folder where you cloned this repo to>>>\flaskr`
5) run `python3 C:\<<<folder where you cloned this repo to>>>\flaskr\app.py`

### Useful links:
- https://www.chartjs.org/
- https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#covid_19_data.csv
