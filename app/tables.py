import pandas as pd
import os


my_path = os.path.abspath(os.path.dirname(__file__))

def show_table(d=','):
    url = my_path + '/static/data/redsox_2018_hitting.txt'
    bos18 = pd.read_csv(url, sep=d)
    return bos18.to_html()
