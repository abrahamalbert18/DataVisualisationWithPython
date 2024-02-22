"""
Seaborn is a Python library built on top of Matplotlib, and offers immense value and simplicity by providing a high-level interface that makes creating visually appealing plots a breeze. Because it uses such straightforward syntax, you’re able to generate various types of charts, such as bar plots, scatter plots, and box plots, with just a few lines of code. Seaborn also comes with built-in themes and color palettes that instantly elevate the aesthetics of your visualizations, even without any design expertise. Another significant advantage is Seaborn's ability to handle complex data structures, making it a seamless companion to your data analysis workflow. With its intuitive and versatile features, Seaborn empowers you to showcase meaningful insights, uncover patterns, and communicate your findings effectively to a wider audience, making it an invaluable tool for your data visualization journey.

Pros:

Simplifies the creation of visually appealing statistical visualizations with concise syntax.

Provides built-in themes and color palettes, enhancing the aesthetic quality of plots.

Supports advanced statistical plotting functions, such as regression plots and distribution plots.

Seamlessly integrates with pandas for data manipulation and analysis tasks.

Cons:

Limited customization options compared to lower-level libraries like Matplotlib.

May require additional code for complex customization beyond the built-in options.

Primarily focused on statistical visualizations, so not as versatile for other types of plots.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("alta-noaa-1980-2019.csv")

def preprocessDate(column="DATE"):
    df[column] = pd.to_datetime(df[column])
    df["YEAR"] = df[column].dt.year
    df["MONTH"] = df[column].dt.month
    df["DAY"] = df[column].dt.day
    return df

sns.set_theme()
def plotHistogram(df, column="SNWD", title="Histogram of Snow Depth"):
    ax = sns.histplot(df[column])
    ax.set_title(title)
    ax.set_xlabel("Snow Depth")
    return ax

histogram = plotHistogram(df=df) #Default
plt.show()

def plotScatter(xAxis="TOBS", yAxis="SNOW", title="Snow Fall with respect to "
                                                  "Temperature"):
    axis = sns.scatterplot(df, x=xAxis, y=yAxis)
    axis.set_ylabel("Snow Fall")
    axis.set_xlabel("Temperature (Observed)")
    axis.set_title(title)
    return axis

scatter = plotScatter() # Default
plt.show()


def plotLine(df, columns=["TMIN", "TMAX", "TOBS"], title="Temperature changes "
                                                     "between 1980 and 2019"):
    axis = sns.lineplot(df[columns])
    axis.set_title(title)
    return axis

line = plotLine(df=df) # Default
plt.show()

# Group By Year
df = preprocessDate()
newDF = df[["TMIN", "TMAX", "TOBS", "YEAR"]].groupby("YEAR").mean()
line2 = plotLine(newDF, title="Mean Temperature changes between 1980 and 2019")
plt.show()

newDF = df[["TMIN", "TMAX", "TOBS", "YEAR"]].groupby("YEAR").min()
line3 = plotLine(newDF, title="Minimum Temperature changes between 1980 and "
                              "2019")
plt.show()

newDF = df[["TMIN", "TMAX", "TOBS", "YEAR"]].groupby("YEAR").max()
line4 = plotLine(newDF, title="Maximum Temperature changes between 1980 and "
                              "2019")
plt.show()