import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('LeoLuo22', 'a29qfrh2d9')
trace0 = go.Bar(
    x=['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'],
    y=[3442, 3591, 4588, 5039, 5736, 6200, 5511, 5988, 5844, 5238, 5333],
    #text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

data = [trace0]
layout = go.Layout(
    title='2005-2015招生人数',
)

fig = go.Figure(data=data, layout=layout)
try:
    py.iplot(fig, filename='test')
except KeyError:
    print("Success! ")
