# Digital Divide application
import json
from dash import Dash
import dash_leaflet as dl
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl
import geojson as gs

app = Dash(__name__)
server = app.server
with open("orlando.geojson", 'r') as f:
    OrlandoData = json.load(f)
def get_color(d):
    color_limits = {1000: '#800026', 500: '#BD0026', 200: '#E31A1C', 100: '#FC4E2A', 50: '#FD8D3C', 20: '#FEB24C',
                    10: '#FED976', -1: '#FFEDA0'}
    for key in color_limits:
        if d > key:
            return color_limits[key]
def get_style(d):
    return dict(fillColor=get_color(d), weight=2, opacity=1, color='white', dashArray='3', fillOpacity=0.7)

# Bind per-feature style information.
featureOptions = {}
for item in OrlandoData["features"]:
    featureOptions[item["id"]] = dict(style=get_style(item["properties"]["NeighID"]["NeighName"]),
                                      popupContent="{:.3f} people/mi2".format(item["properties"]["NeighID"]["NeighName"]))
# Create geojson.
options = dict(hoverStyle=dict(weight=5, color='#666', dashArray=''), zoomToBoundsOnClick=True)
geojson = dl.GeoJSON(data=OrlandoData, id="geojson", options=options)

# Create app.
app.layout = html.Div(
    className='App',
    children=[
        html.Header([html.H1('Digital Divide')
        ]
        ),
        html.Div(
            className='Body',
            children=[
                        dcc.Dropdown(
                            id='dd_neighborhoods',
                            options=[
                                {'label': 'Azalea Park', 'value': 'AzaPar'}
                            ],
                            value='AzaPar'
                        )
                    ]
        ),
        html.Div(
            className='View',
            children=[
    dl.Map(children=[dl.TileLayer(url="https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")] + [geojson],
           style={'width': "100%", 'height': "100%"}, center=[28.4845, -81.2519], zoom=11, id="map", maxZoom=18, dragmode=False),
], style={'width': '75%', 'height': '75vh', 'margin': "auto", "display": "block"} 
        ),
        html.Footer([
            html.P('Created by the Magnificent 7')
        ])
    ]
)
if __name__ == '__main__':
    app.run_server()
