from dash import dash_table
import plotly.graph_objs as go
from dash import html
from dash import dcc
import dash
import plotly.express as px
import pandas as pd

#Подключение к csv
df = pd.read_csv('Data_Base/Data.csv')
line_df = pd.read_csv('Data_Base/Data_line.csv')
ran_df = pd.read_csv('Data_Base/Data_rad.csv')
table_df = pd.read_csv('Data_Base/Data_table.csv')
dif = pd.read_csv('Data_Base/Data_str.csv')

#карта
fig = px.scatter(df, x='x', y='y', color='color')

#Линейный график
line = pd.DataFrame(line_df)
line['date'] = pd.to_datetime(line['date'], format='%d.%m.%Y')

#Круговой
figure = go.Figure(data=[go.Pie(labels=ran_df['labels'], values=ran_df['values'])])

#ТАБЛИЦА
data = pd.DataFrame(table_df)

# Создаем Dash приложение
app = dash.Dash(__name__)

# Определяем макет приложения
app.layout = html.Div([
    html.H1('Применение библиотеки Dash'),
    html.H3('Анализ данных о продажах', style={'text-align': 'center'}),
    dcc.Graph(
        figure={
            'data': [
                {'x': line['date'], 'y': line['value'], 'type': 'scatter', 'mode': 'lines+markers', 'name': 'Временной ряд'}
            ],
            'layout': {
                'title': '',
                'xaxis': {'title': 'День'},
                'yaxis': {'title': 'Сумма'}
            }
        }
    ),
    html.Div([
    html.H3('Анализ данных о посещении веб-сайта', style={'text-align': 'center'}),
        dcc.Graph(figure=figure)
    ]),
    html.Div([
    html.H3('Анализ данных о розничной продаже', style={'text-align': 'center'}),
        dash_table.DataTable(
            columns=[{'id': 'Показатель', 'name': 'Показатель'}, {'id': 'Значение', 'name': 'Значение'}],
            data=data.to_dict('records'),
            style_table={'border': '1px solid black'},
            style_header={'backgroundColor': 'rgb(20, 20, 20)', 'color': 'white'},
            style_cell={'textAlign': 'center', 'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'}
        )
    ]),
    html.Div([
        html.H3('Анализ зависимостей', style={'text-align': 'center'}),
        dcc.Graph(figure=fig)
]),
html.Div([
    html.H1('Интерактивный график', style={'text-align': 'center'}),
    dcc.Dropdown(
        id='column1',
        options=[
            {'label': 'Зависимость 1', 'value': 'column1'},
            {'label': 'Зависимость 2', 'value': 'column2'},
            {'label': 'Зависимость 3', 'value': 'column3'}
        ],
        value='column3'
    ),
    dcc.Graph(id='graph')
])
])
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('column1', 'value')]
)
def update_graph(selected_column1):
    fig = px.scatter(dif, x='x', y=selected_column1, color = 'color')
    return fig

# Запускаем приложение
if __name__ == '__main__':
    app.run_server(debug=True)

