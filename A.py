import plotly_express as px
import pandas as p
import numpy as n

#definition of a function
def plotFigure(data_frame, x_col, y_col):
    fig = px.scatter(data_frame, x =x_col , y = y_col, size=x_col)
    fig.show()
    

def find_correlation(df,x,y):
    list_x = df[x].tolist()
    list_y = df[y].tolist()
    correlation = n.corrcoef(list_x,list_y)
    print(f"Correlation between {x} and {y} is ",correlation[0,1])

def getDataSource():
    name = "Student Marks vs Days Present.csv"
    df = p.read_csv(name)

    col_x = "Marks In Percentage"
    col_y = "Days Present"

    find_correlation(df,col_x,col_y)

    #calling of a function
    plotFigure(df,col_x,col_y) 

getDataSource()