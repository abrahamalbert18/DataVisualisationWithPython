"""
Introduction

Pandas is a powerful python library that simplifies the process of data manipulation and organization, allowing you to effortlessly prepare your data for visualization. Using Pandas dataframes, you can easily import, clean, and analyze data from various sources like CSV files or Excel spreadsheets. Once your data is prepped, Pandas seamlessly integrates with other visualization libraries, such as Matplotlib and Seaborn, making it a crucial component of the data visualization pipeline. This seamless integration enables you to create an array of visualizations, including bar plots, scatter plots, and heatmaps, in the exact same environment that you would use to clean or preprocess your data. By harnessing the power of Pandas for data visualization, you can gain deeper insights into your data, make informed decisions, and present your findings in a compelling and impactful manner.

Pros:

Provides a comprehensive and powerful data manipulation and analysis toolkit in Python.

Offers flexible data structures like DataFrames, allowing for easy handling of structured data.

Supports various data transformation operations, making it ideal for data cleaning and preprocessing tasks.

Integrates well with other libraries in the Python ecosystem, such as Matplotlib and Seaborn, for visualization purposes.

Can easily convert code to work with Snowflake or Big Query using tools like Ponder

Cons:

Steeper learning curve compared to spreadsheet-based tools like Excel or Google Sheets.

May require writing more code for complex data manipulations compared to drag-and-drop interfaces.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alta-noaa-1980-2019.csv")

def preprocessDate(column="DATE"):
    df[column] = pd.to_datetime(df[column])
    df["YEAR"] = df[column].dt.year
    df["MONTH"] = df[column].dt.month
    df["DAY"] = df[column].dt.day
    return df
def plotHistogram(column="SNWD", title="Histogram of Snow Depth"):
    plt.figure(dpi=125)
    plt.hist(df[column])
    plt.title(title)
    plt.ylabel("Frequency of Snow Depth")
    plt.xlabel("Snow Depth")
    return plt

histogram = plotHistogram() #Default
histogram.show()

def plotScatter(xAxis="TOBS", yAxis="SNOW", title="Snow Fall with respect to "
                                                  "Temperature"):
    plt.figure(dpi=125)
    plt.scatter(x=df[xAxis], y=df[yAxis])
    plt.title(title)
    plt.ylabel("Snow Fall")
    plt.xlabel("Temperature (Observed)")
    return plt

scatter = plotScatter() # Default
scatter.show()

def plotLine(df, columns=["TMIN", "TMAX", "TOBS"], title="Temperature changes "
                                                     "between 1980 and 2019"):
    plt.figure(dpi=125)
    plt.plot(df[columns], label=columns)
    plt.title(title)
    plt.legend()
    return plt

line = plotLine(df=df) # Default
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