import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os

def plotPoints(x, y, xlabel, ylabel, title):
    fig = plt.figure(figsize=(20, 10))
    plt.plot(x, y, 'bo-')
    plt.title('{}'.format(title), fontsize=36)
    plt.xlabel('{}'.format(xlabel), fontsize=24)
    plt.ylabel('{}'.format(ylabel), fontsize=24)

    my_path = os.path.abspath(os.path.dirname(__file__)) + '/static/graph_images/'

    plot_name = 'plot_points.png'
    url = my_path + plot_name
    fig.savefig(url)
    return plot_name
