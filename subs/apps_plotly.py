from flask import render_template, session
from classes.topic import Topic
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    # Cria dataframe a partir da base de dados
    engine = create_engine('sqlite:///' + filename + 'socialmedia.db')
    df_post = pd.read_sql('Post', con=engine)

    # Agrupa por tópico e conta quantos posts há em cada
    result = df_post.groupby('topic_id')['id'].count()
    p_ids = result.index
    p_names = []
    for p_id in p_ids:
        p_obj = Topic.obj[p_id]
        p_names.append(p_obj.topic_name)
    quantities = result.values

    # Cria gráfico de barras com Plotly Express
    fig = px.bar(
        x=p_names,
        y=quantities,
        labels={'x': 'Topic Name', 'y': 'Quantity of Posts'},
        title='Number of posts per topic',
        color_discrete_sequence=['#93d3ae']  # verde menta
    )

    # Personaliza o layout para combinar com o site
    fig.update_layout(
    plot_bgcolor='#fdfaf6',
    paper_bgcolor='#fcd5bd',
    font=dict(
        family='Patrick Hand, cursive',
        color='#333',
        size=18
    ),
    title=dict(
        text='Number of posts per topic',
        font=dict(size=24),
        x=0.5  # <-- isto centra o título
    ),
    xaxis=dict(
        gridcolor='#fcd5bd',
        tickangle=-45
    ),
    yaxis=dict(
        gridcolor='#fcd5bd'
    )
)

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))

    
