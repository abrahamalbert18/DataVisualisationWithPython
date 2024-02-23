import plotly.graph_objs as go

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 6, 8, 12, 4]

# Create a bar chart
fig = go.Figure(data=go.Bar(x=x, y=y))
fig.show()
