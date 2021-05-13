import plotly.graph_objects as go
import plotly.io as pio

from numpy import sqrt


def simulateCities(rg, n_cities):
    cities = {}
    for j in range(n_cities):
        cities[j] = tuple(rg.random(size=2).round(2)) # we use round(2) to make the digits more human readable
    return cities

def drawSalesman(path, cities, title="Path taken"):
    # loop through the coordinates using the path sequence
    x = [cities[p][0] for p in path]
    y = [cities[p][1] for p in path]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='path', mode='lines'))
    fig.add_trace(go.Scatter(x=x, y=y, name="cities", mode='markers+text', 
        marker={'size': 10}, text=[str(i) for i in path], textposition="bottom center",))
    fig.update_layout(template="presentation", title=title, xaxis_title="X", yaxis_title="Y", width=800, height=600)
    fig.update_xaxes(range=[0, 1])
    fig.update_yaxes(range=[0, 1])
    fig.show() # to reveal the figure
    
def evaluate(path, cities):
    # measure the total distance travelled
    distance = 0
    for n, p in enumerate(path[:-1]): # we loop until the last city -1
        x1, y1 = cities[p]
        x2, y2 = cities[path[n+1]]
        length = sqrt((x2-x1)**2 + (y2-y1)**2)
        distance += length
    
    return distance