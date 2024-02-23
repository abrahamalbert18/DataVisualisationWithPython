import pandas as pd
import plotly.express as px

df = pd.read_csv("alta-noaa-1980-2019.csv")

def preprocessDate(column="DATE"):
    df[column] = pd.to_datetime(df[column])
    df["YEAR"] = df[column].dt.year
    df["MONTH"] = df[column].dt.month
    df["DAY"] = df[column].dt.day
    return df

def plotHistogram(df, column="SNWD", title="Histogram of Snow Depth"):
    figure = px.histogram(data_frame=df, x=column, title=title,
                          labels={"SNWD":"Snow Depth"})
    return figure

histogram = plotHistogram(df=df)  # Default
histogram.show()

def plotScatter(df, xAxis="TOBS", yAxis="SNOW", title="Snow Fall with respect "
                                                      "to "
                                                      "Temperature"):
    figure = px.scatter(data_frame=df, x=xAxis, y= yAxis, title=title,
                          labels={xAxis:"Temperature (Observed) in F",
                                  yAxis:"Snow Fall"})
    return figure

scatter = plotScatter(df=df)  # Default
scatter.show()

def plotLine(df, columns=None, title="Temperature changes "
                                     "between 1980 and 2019",
             xLabel='Year', yLabel="Temperature (degrees F)"):
    if columns is None:
        columns = ["TMIN", "TMAX", "TOBS"]
    figure = px.line(data_frame=df, y=columns, title=title,
                     labels={column:"Temperature in F"
                             for column in columns})
    figure.update_layout(xaxis_title=xLabel,
                      yaxis_title=yLabel)
    return figure

line = plotLine(df=df, xLabel="")  # Default
line.show()

# Group By Year
df = preprocessDate()
newDF = df[["TMIN", "TMAX", "TOBS", "YEAR"]].groupby("YEAR").mean()
line2 = plotLine(newDF, title="Mean Temperature changes between 1980 and 2019")
line2.show()

newDF = df[["TMIN", "TMAX", "TOBS", "YEAR"]].groupby("YEAR").min()
line3 = plotLine(newDF, title="Minimum Temperature changes between 1980 and "
                              "2019")
line3.show()

newDF = df[["TMIN", "TMAX", "TOBS", "YEAR"]].groupby("YEAR").max()
line4 = plotLine(newDF, title="Maximum Temperature changes between 1980 and "
                              "2019")
line4.show()
