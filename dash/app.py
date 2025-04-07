from pathlib import Path

import plotly.express as px

import duckdb
from dash import Dash, dcc, html

db_path = Path(__file__).parent.parent / "duckdb" / "warehouse.duckdb"
con = duckdb.connect(db_path)
df = con.sql("SELECT * FROM main.titanic").df()
con.close()

app = Dash()

app.layout = html.Div(
    style={"textAlign": "center", "fontFamily": "sans-serif"},
    children=[
        html.H1(children="Titanic Dashboard"),
        html.H2(children="Survivors by Age"),
        dcc.Graph(figure=px.histogram(df, x="age", color="survived", nbins=20)),
        html.H2(children="Survivors by Sex"),
        dcc.Graph(figure=px.histogram(df, x="sex", color="survived")),
        html.H2(children="Survivors by Fare"),
        dcc.Graph(figure=px.histogram(df, x="fare", color="survived", nbins=20)),
    ],
)

if __name__ == "__main__":
    app.run()
