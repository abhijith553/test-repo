from dash import Dash, html
import os

app = Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div([
        html.H3("retail store market trends and predictions", style={
                                                                        'display': 'flex',
                                                                        'justifyContent': 'flex-start',
                                                                        'alignItems': 'flex-start',
                                                                        'width': '100%',
                                                                        'fontSize': '24px',
                                                                        'fontFamily': 'Monospace',
                                                                        'color' : '#fff'

                                                                    }
),
        html.Details([
            html.Summary("Pages", style={
                                            'cursor': 'pointer',
                                            'fontSize': '21px',
                                            'fontFamily': 'Consolas',
                                            'backgroundColor': '#000',
                                            'color': '#fff',
                                            'border': '1.5px solid #fff',
                                            'padding': '8px 12px',
                                            'listStyleType': 'none',
                                            'position': 'fixed',       
                                            'top': '20px',            
                                            'right': '30px',           
                                            'zIndex': '1000',
                                            'borderRadius': '7px'
            }),
            html.Div([
                dcc.Link("Home", href='#', style=link_style),
                dcc.Link("EDA", href='#', style=link_style),
                dcc.Link("More Insights", href='#', style=link_style),
                dcc.Link("Forecast", href='#', style=link_style),
                dcc.Link("Methodology", href='#', style=link_style),
                dcc.Link("About", href='#', style=link_style),
            ], style={
                        'display': 'flex',
                        'flexDirection': 'column',
                        'flexWrap': 'wrap',
                        'padding': '10px',
                        'border': '3px solid #000',
                        'backgroundColor': '#000',
                        'position': 'absolute',
                        'right': '0.1px',
                        'top': '100px',
                        'zIndex': '1000',
                        'borderRadius': '7px'
            })
        ], style={'position': 'relative', 'backgroundColor': '#000'})
    ], style={
                'display': 'flex',
                'justifyContent': 'flex-end',
                'padding': '2px 20px',
                'backgroundColor': '#000',
                'color' : '#fff'
    }),

    html.Div(id='page-content')
], style = {'backgroundColor': '#fff'})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print("Starting on port", port)
    app.run(debug=False, host="0.0.0.0", port=port)
