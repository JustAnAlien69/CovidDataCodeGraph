import pandas as pd
import plotly.express as px

a = pd.read_csv("covidData.csv")
b = px.scatter(a, x="date",y="cases",color="country",title="Covid Data")
b.show()