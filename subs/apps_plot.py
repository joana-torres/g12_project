from flask import render_template, session
from classes.topic import Topic
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():
    # Creates a pandas dataframe with the orderproduct table data
    engine = create_engine('sqlite:///' + filename + 'socialmedia.db')
    df_topicpost = pd.read_sql('Post', con=engine)
    # Uses groupby to obtain the total quantity order by product id
    result = df_topicpost.groupby('topic_id')['post_id'].count().reset_index()
    result.columns = ['topic_id', 'post_count']
    # From the product class get the product id names
    t_ids = result.index
    t_names = []
    for t_id in t_ids:
        t_obj = Topic.obj[t_id]
        t_names.append(t_obj.name)
    quantities = result['post_count'].tolist()
    # Uses matplotlib to draw a bar chart
    fig, ax = plt.subplots()
    plt.bar(t_names, quantities, width = 0.4,label = 'Topic_id')
    x_index = range(len(t_names))
    plt.xticks(ticks=x_index, labels=t_names)
    plt.xlabel('Topic')
    plt.ylabel('Posts')
    plt.title('Number of posts')
    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')
    # Send the image as a Flask response
    return render_template("plot.html", image=image, ulogin=session.get("user"))
