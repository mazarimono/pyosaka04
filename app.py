import dash  
import dash_core_components as dcc  
import dash_html_components as html
import plotly.graph_objs as go  
import pandas as pd 
import os   

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

df223 = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'cb5392c35661370d95f300086accea51/raw/'
    '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
    'indicators.csv')

available_indicators = df223['Indicator Name'].unique()

app.layout = html.Div([
    dcc.Tabs(id='tabs', style=tabs_styles, children=[
        dcc.Tab(label='Front-Page',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.Div([html.P("Dashを使ってプレゼン資料を作る")], style={'color': 'blue', 'fontSize': 50}),
                        html.Div([html.P("PyOsaka 2019/01/09")], style={'color': 'skyblue', 'marginTop': '5%', 'fontSize': 40}),
                        html.Div([html.P("合同会社長目　小川　英幸")], style={'color': 'green', 'marginTop': '5%', 'fontSize': 50})
                        ],style={'marginTop': '15%', 'textAlign': 'center'})
                    ]),
        dcc.Tab(label='Self-Introduce',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.H1('Who am I?'),
                        html.Div([
                            html.H3('小川　英幸(@OgawaHideyuki)')
                        ], style={'marginTop': '3%'}),
                        html.Div([
                            html.H3('はんなりPython,BlockchainKyotoのオーガナイザー')
                        ], style={'marginTop': '3%'}),
                        html.Div([
                            html.H3('プログラミング歴　3年　==  Python歴')
                        ], style={'marginTop': '3%'}),
                        html.Div([
                            html.H3('2つ目の言語としてJavaScriptを勉強中')
                        ], style={'marginTop': '3%'})
                    ], style={'marginTop': '10%', 'textAlign': 'center'})
                ]),
        dcc.Tab(label='Blockchain_Kyoto',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.H1("Blockchain Kyoto 2019/1/13 IOST MeetUp"),
                        html.H1("JavaScriptでスマートコントラクトを作ろう！"),
                        html.Img(src= "https://cdn-ak.f.st-hatena.com/images/fotolife/m/mazarimono/20190107/20190107132618.png"),
                    html.Div([
                        html.H4(
                        "通常会も1月23日に開催　connpassはhttps://blockchain-kyoto.connpass.com/event/114802/")
                        ], style={'marginTop': '4%'}),
            #ローカルの画像の埋め込みができない。サードパーティーに入れていると出きるみたいだけど
                        ], style={'marginTop': '5%', 'textAlign': 'center'})
                ]),
        dcc.Tab(label='Hannari_Python',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                            html.H1("はんなりPythonの会#13　2019年1月18日金曜日"),
                            html.H3('Dash Hands On Returns'),
                            html.Img(src="https://cdn-ak.f.st-hatena.com/images/fotolife/m/mazarimono/20190107/20190107172847.png"),
                            html.H3('11月の1回目はPydata Osakaのブログで取り上げていただきました！  https://bit.ly/2TBXlgl')
                    ], style={'marginTop': '5%', 'textAlign': 'center'})
                ]),
        dcc.Tab(label='Dash-1',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.Div([
            html.H1("Dash： 可視化ツール")], style={'marginTop': '3%', "marginLeft": '5%'}),
            html.Div([
            html.H3("/ FlaskとReactJSとPlotlyJSを使ってウェブアプリケーションを作るライブラリ")], style={'marginTop': '3%', "marginLeft": '5%'}),
            html.Div(style={"backgroundColor": colors['background']}, children=[
                html.H1(
                    children="Hello Dash",
                    style={
                        'textAlign': 'center',
                        'color': colors['text'],
                        'marginTop': '3%'
                    }
                ),
                html.Div(children="Dash: A web application framework for Python.", style={
                    'textAlign': 'center',
                    'color': colors['text']
                }),

                dcc.Graph(
                    id = 'first-graph',
                    figure = {
                    'data' : [
                        {'x': [1, 2, 3, 4, 5], 'y':[4, 5, 6, 3, 2], 'type':'bar', 'name': 'TOkyo'},
                        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3,4, 5], 'type': 'bar', 'name': 'Osaka'},
                        {'x': [1, 3,4,5], 'y': [1, 1, 3,6 ], 'type': 'bar', 'name': 'Kyoto'}
                    ],
                    'layout' :{
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                    } 
                )
            ]),
            html.Div([
                html.H3("/ 見難いものも見やすくできる！"),
                html.H3("/ 下のように見難い線グラフもlegendをクリックするとその要素のオンオフができる"),
            ], style={'marginTop': '3%', 'marginLeft': '5%'}),
            html.Div([
                dcc.Graph(
                    id='second-graph',
                    figure = {
                        'data':[
                        {'x': [1, 2, 3, 4, 5], 'y':[4, 5, 6, 3, 2], 'type':'line', 'name': 'TOkyo'},
                        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3,4, 5], 'type': 'line', 'name': 'Osaka'},
                        {'x': [1, 3,4,5], 'y': [1, 1, 3,6 ], 'type': 'line', 'name': 'Kyoto'} ,
                        {'x': [1, 2, 3, 4, 5], 'y':[3, 5, 4, 3, 1], 'type': 'line', 'name': 'mie'},
                        {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 3, 6, 4], 'type': 'line', 'name': 'wakayama'},
                        {'x': [1, 2, 3, 4, 5], 'y': [4, 3, 4, 2, 1], 'type': 'line', 'name': 'shiga'} ,
                        {'x': [1, 2, 3, 4, 5], 'y':[2, 4, 1, 3, 4], 'type': 'line', 'name': 'nara'},
                        {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 4, 3], 'type': 'line', 'name': 'hyogo'}                          
                        ],
                    'layout': {
                        'height': 600
                    }
                    }
                )
            ], style={'marginBottom': '5%'})
                    ])
                ]),
        dcc.Tab(label='Dash-2',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                        html.Div([
                            html.Div([
                            html.H3('時系列データも色々な見方ができる！')],
                            style={'textAlign': 'center'}),
                            html.Div([
                            dcc.Graph(id='graph-with-slider')],style={'marginBottom':'2%'}),
                            dcc.Slider(
                                id = 'year-slider',
                                min = df['year'].min(),
                                max = df['year'].max(),
                                value = df['year'].min(),
                                marks={str(year): str(year) for year in df['year'].unique()}
                                ),
                            html.Div([
                            html.H4('/ スライダーで年を変えられる!'),
                            html.H4('/ legendクリックで大陸のオンオフができる！')], style={'textAlign': 'center', 'marginTop': "5%"}),
                            ], style={'marginTop': '3%'})
                        ])
                ]),
        dcc.Tab(label='Dash-3',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div([
                            html.Div([
                            html.Div([
                            html.H3('めちゃ複雑なこともできる！')],style={'textAlign': 'center', 'marginBottom': '2%'}),

                    html.Div([
                        dcc.Dropdown(
                        id='crossfilter-xaxis-column',
                        options=[{'label': i, 'value': i} for i in available_indicators],
                        value='Fertility rate, total (births per woman)'
                        ),
                        dcc.RadioItems(
                        id='crossfilter-xaxis-type',
                        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                        value='Linear',
                        labelStyle={'display': 'inline-block'}
                        )
                        ],
                        style={'width': '49%', 'display': 'inline-block'}),

                        html.Div([
                        dcc.Dropdown(
                        id='crossfilter-yaxis-column',
                        options=[{'label': i, 'value': i} for i in available_indicators],
                        value='Life expectancy at birth, total (years)'
                        ),
                        dcc.RadioItems(
                        id='crossfilter-yaxis-type',
                        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                        value='Linear',
                        labelStyle={'display': 'inline-block'}
                        )
                        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
                        ], style={
                        'borderBottom': 'thin lightgrey solid',
                        'backgroundColor': 'rgb(250, 250, 250)',
                        'padding': '10px 5px'
                        }),

                        html.Div([
                        dcc.Graph(
                        id='crossfilter-indicator-scatter',
                        hoverData={'points': [{'customdata': 'Japan'}]}
                        )
                        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
                        html.Div([
                        dcc.Graph(id='x-time-series'),
                        dcc.Graph(id='y-time-series'),
                        ], style={'display': 'inline-block', 'width': '49%'}),

                        html.Div(dcc.Slider(
                        id='crossfilter-year--slider',
                        min=df223['Year'].min(),
                        max=df223['Year'].max(),
                        value=df223['Year'].max(),
                        marks={str(year): str(year) for year in df223['Year'].unique()}
                        ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
                    ], style={'marginTop': '3%'}),
                    html.Div([
                        html.H3('ドロップダウンで表示させるデータを変えられます。'),
                        html.H3('左のチャートをマウスホバーさせると右側に時系列データが表示されます！')
                    ], style={'marginTop': '3%', 'textAlign': 'center'})
                ]
                ),
        dcc.Tab(label='Conclusion',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                html.Div([
                    html.Div([
                        html.H2('Conclusion')], style={'marginBottom': '4%'}),
                        html.Div([
                        html.H3('これまでのプレゼン資料は紙芝居と揶揄されるよう退屈だった。')],style={'marginBottom': '4%'}),
                        html.Div([
                        html.H3('一方、Dashを使ってデータをインタラクティブに動かせるようにすれば異なる視点を得られることが多くなる。')],style={'marginBottom': '4%'}),
                        html.Div([
                        html.H3('ブレインストーミングなども多くの意見が出やすくなり、それを落とし込みやすくなる。')],style={'marginBottom': '4%'}),
                        html.Div([
                        html.H3('データを活用して利益に還元することがより活発にできる。')], style={'marginBottom': '4%'}),
                        html.Div([
                        html.H3('手がかかるという意見が聞かれると思うが、逆にデータの活用を考えるのであれば手間を惜しんでいる場合ではない。')
                        ])

                ], style={'marginTop': '3%','marginLeft': '3%', 'marginRight':'3%', 'textAlign': 'center'})            
                ])
            ])
    ])

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')]
)

def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    df223f = df223[df223['Year'] == year_value]

    return {
        'data': [go.Scatter(
            x=df223f[df223f['Indicator Name'] == xaxis_column_name]['Value'],
            y=df223f[df223f['Indicator Name'] == yaxis_column_name]['Value'],
            text=df223f[df223f['Indicator Name'] == yaxis_column_name]['Country Name'],
            customdata=df223f[df223f['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }


def create_time_series(df223f, axis_type, title):
    return {
        'data': [go.Scatter(
            x=df223f['Year'],
            y=df223f['Value'],
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {'type': 'linear' if axis_type == 'Linear' else 'log'},
            'xaxis': {'showgrid': False}
        }
    }


@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    country_name = hoverData['points'][0]['customdata']
    df223f = df223[df223['Country Name'] == country_name]
    df223f = df223f[df223f['Indicator Name'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
    return create_time_series(df223f, axis_type, title)


@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value')])
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    df223f = df223[df223['Country Name'] == hoverData['points'][0]['customdata']]
    df223f = df223f[df223f['Indicator Name'] == yaxis_column_name]
    return create_time_series(df223f, axis_type, yaxis_column_name)


if __name__ == '__main__':
    app.run_server(debug=True)