# Digital Divide application
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    className='App',
    children=[
        html.Header([
            html.H1('Digital Divide')
        ]),

        html.Div(
            className='Body',
            children=[
                html.Div(
                    className='Operations',
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
                        dl.Map(
                            id='dl_geojson',
                            center={'lat': 28.5383, 'lon': -81.3792},
                            zoom=10,
                            children=[
                                dl.TileLayer()
                            ]
                        )
                    ]
                )
            ]
        ),

        html.Footer([
            html.P('Created by the Magnificent 7')
        ])
    ]
)

if __name__ == '__main__':
    app.run_server()
