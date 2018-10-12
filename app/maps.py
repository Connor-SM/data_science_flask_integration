import pygal
import os
from app.tables import get_runners


def world_map():
    runners = get_runners('/static/data/boston_marathon2017.csv')
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Some countries'
    worldmap_chart.add('US Runners', {
        'us': runners
    })

    my_path = os.path.abspath(os.path.dirname(__file__)) + '/static/graph_images/'

    plot_name = 'world_map.svg'
    url = my_path + plot_name
    worldmap_chart.render_to_file(url)
