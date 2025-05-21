from flask import render_template, session
from classes.topic import Topic
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    # Creates a pandas dataframe with the orderproduct table data
    engine = create_engine('sqlite:///' + filename + 'socialmedia.db')
    df_topicpost = pd.read_sql('Post', con=engine)
    # Uses groupby to obtain the total quantity order by product id
    result = df_topicpost.groupby('topic_id')['post_id'].count()
    # From the product class get the product id names
    t_ids = result.index
    t_names = []
    for t_id in t_ids:
        t_obj = Topic.obj[t_id]
        t_names.append(t_obj.name)
    quantities = result.values

    # Create interactive plot with Plotly
    fig = px.bar(x=t_names, y=quantities, labels={'x': 'Topic', 'y': 'Posts'}, title='Number of posts')

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))
