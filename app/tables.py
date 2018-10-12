import pandas as pd
import os


my_path = os.path.abspath(os.path.dirname(__file__))

def show_table(d=','):
    url = my_path + '/static/data/redsox_2018_hitting.txt'
    bos18 = pd.read_csv(url, sep=d)
    return bos18.to_html()

def get_runners(filename, d=','):
    url = my_path + filename
    data = pd.read_csv(url, sep=d)
    data[data['Country'] == 'USA'] = 'us'
    data[data['Country'] == 'USA'] = 'us'
    runners = data.groupby(['Country'], as_index=False).count()
    runners = runners[runners['Country'] == 'us']['Overall'].mean()
    return runners
