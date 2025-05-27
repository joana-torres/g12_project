from flask import render_template, session
from classes.topic import Topic
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    # Creates a pandas dataframe with the orderproduct table data
    engine = create_engine('sqlite:///' + filename + 'socialmedia.db')
    df_post = pd.read_sql('Post', con=engine)
    # Uses groupby to obtain the total quantity order by product id
    result = df_post.groupby('topic_id')['id'].count()
    # From the product class get the product id names
    p_ids = result.index
    p_names = []
    for p_id in p_ids:
        p_obj = Topic.obj[p_id]
        p_names.append(p_obj.name)
    quantities = result.values

    # Create interactive plot with Plotly
    fig = px.bar(x=p_names, y=quantities, labels={'x': 'Topic ID', 'y': 'Quantity of posts'}, title='Number of posts in each topic')

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))


#%%
    
