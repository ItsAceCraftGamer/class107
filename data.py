import csv
import pandas as p
import plotly.graph_objects as g

df = p.read_csv("data.csv")
student_df = df.loc[df['student_id'] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

grph = g.Figure(g.Bar(
    y = student_df.groupby("level")["attempt"].mean(),
    x = ["level1","level2","level3","level4"],
    orientation = 'v'  
))

grph.show()