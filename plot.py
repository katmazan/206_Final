import plotly.plotly as py
from plotly.graph_objs import *
from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
py.sign_in('katmazan', 'bu1N2yJCR7u3JQIJTthN')
trace1 = {
  "hoverlabel": {"font": {"family": "'Impact'"}}, 
  "labels": ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"], 
  "labelssrc": "katmazan:0:5c2aa8", 
  "marker": {"colors": ["rgb(4, 4, 21)", "rgb(98, 24, 127)", "rgb(176, 52, 122)", "rgb(250, 129, 94)", "rgb(254, 185, 127)", "rgb(252, 234, 172)"]}, 
  "name": "c", 
  "type": "pie", 
  "uid": "2fffa2", 
  "values": [10, 11, 13, 14, 13, 17, 22], 
  "valuessrc": "katmazan:0:eeb484"
}
data = Data([trace1])
layout = {
  "hovermode": "closest", 
  "scene": {
    "aspectmode": "auto", 
    "aspectratio": {
      "x": 1, 
      "y": 1, 
      "z": 1
    }
  }, 
  "title": "Days of the Week I Post"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

trace1 = {
  "x": ["Friday 12pm to 5:59pm", "Friday 6am to 11:59am", "Friday12am to 5:59am", "Friday6pm to 11:59pm", "Monday12am to 5:59am", "Monday12pm to 5:59pm", "Monday6am to 11:59am", "Monday6pm to 11:59pm", "Saturday12am to 5:59am", "Saturday12pm to 5:59pm", "Saturday6am to 11:59 am", "Saturday6pm to 11:59pm", "Sunday12am to 5:59am", "Sunday12pm to 5:59pm", "Sunday6am to 11:59am", "Sunday6pm to 11:59pm", "Thursday12am to 5:59am", "Thursday12pm to 5:59pm", "Thursday6am to 11:59am", "Thursday6pm to 11:59pm", "Tuesday12am to 5:59am", "Tuesday12pm to 5:59pm", "Tuesday6am to 11:59am", "Tuesday6pm to 11:59pm", "Wednesday12am to 5:59am", "Wednesday12pm to 5:59pm", "Wednesday6am to 11:59am", "Wednesday6pm to 11:59pm"], 
  "y": ["0", "0", 5, 5, 5, 3, "0", 3, 6, 2, 1, 4, 2, 4, "0", 8, 1, 4, "0", 8, 13, 3, "0", 1, 11, 5, "0", 6], 
  "marker": {
    "color": "rgb(50, 31, 180)", 
    "opacity": 0.7, 
    "symbol": "asterisk-open"
  }, 
  "mode": "markers", 
  "name": "c", 
  "type": "scatter", 
  "uid": "68b303", 
  "xsrc": "katmazan:2:355d4e", 
  "ysrc": "katmazan:2:28c56a"
}
data = Data([trace1])
layout = {
  "boxmode": "group", 
  "hovermode": "closest", 
  "plot_bgcolor": "rgba(127, 168, 116, 0)", 
  "scene": {
    "aspectmode": "auto", 
    "aspectratio": {
      "x": 1, 
      "y": 1, 
      "z": 1
    }
  }, 
  "title": "Posts Made During Times of the Day", 
  "xaxis": {
    "autorange": True, 
    "range": [-1.78957528958, 28.7895752896], 
    "rangeslider": {
      "autorange": True, 
      "visible": False
    }, 
    "title": "created_time", 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-1.12705530643, 14.1270553064], 
    "title": "c", 
    "type": "linear"
  }
}
import plotly.plotly as py
from plotly.graph_objs import *

trace1 = {
  "x": ["a", "the", "to", "of", "in", "and", "Overwatch", "I", "for", "is", "you", "my", "with", "this", "it", "being", "i", "me", "-", "are", "has", "got", "be", "skin", "heroes", "like", "at", "team", "first", "December", "2017", "OWL", "an", "Feel", "that", "made", "should", "kill", "not", "ult", "have", "ever", "was", "their", "\"Why", "so", "Moira", "again", "It", "AMD", "when", "Mercy", "from", "My", "When", "there", "our", "back", "Don't", "Good", "on", "still", "by", "Junkertown", "point", "Like", "There", "as", "need", "more", "self-destruct", "perspective", "d.va", "Thanks", "now", "I've", "way", "If", "character", "single", "would", "game", "One", "A", "Torb", "Play", "Season", "|", "(Fan-Skin)", "origin", "Uprising", "out", "crash", "The", "Best", "Ever", "CS:GO's", "League", "voice", "lines"], 
  "y": [33, 30, 23, 17, 13, 12, 11, 11, 11, 9, 8, 8, 7, 6, 6, 6, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
  "connectgaps": False, 
  "line": {
    "color": "rgb(243, 168, 25)", 
    "shape": "vh", 
    "width": 2.5
  }, 
  "marker": {
    "color": "#19d3f3", 
    "line": {"width": 1}, 
    "opacity": 0.5, 
    "size": 6
  }, 
  "mode": "lines+markers", 
  "name": "y", 
  "type": "scatter", 
  "uid": "00812d", 
  "xsrc": "katmazan:66:3118b6", 
  "ysrc": "katmazan:66:a2b30f"
}
data = Data([trace1])
layout = {
  "barmode": "stack", 
  "font": {
    "color": "rgb(65, 122, 195)", 
    "size": 12
  }, 
  "hovermode": "closest", 
  "margin": {
    "t": 50, 
    "l": 40
  }, 
  "paper_bgcolor": "rgb(231, 230, 230)", 
  "title": "Most used words on OW Hot", 
  "titlefont": {"color": "rgb(81, 141, 216)"}, 
  "xaxis": {
    "autorange": True, 
    "range": [-6.0258126195, 105.02581262], 
    "showgrid": False, 
    "title": "word", 
    "type": "category", 
    "zeroline": False
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-0.0609756097561, 35.0609756098], 
    "title": "", 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'red_cacnhe.json')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


