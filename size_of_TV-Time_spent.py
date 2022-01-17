import csv
from statistics import correlation
import numpy as np

import plotly.express as px
with open("Size of TV,_Average time spent watching TV in a week (hours).csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Size of TV", y = "\tAverage time spent watching TV in a week (hours)")
    fig.show()

def findCorelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Size of Tv and Average time spent watching Tv in a week :- \n--->", correlation[0, 1])


def getDataSource(data_path):
    size_of_tv = []
    time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x":size_of_tv,"y":time_spent}


def setup():
    data_path = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    datasource = getDataSource(data_path)
    findCorelation(datasource)

setup()