
import pandas as pd
import plotly.express as px
import numpy as np


df = pd.read_csv('cleaned_data.csv')


df['country'].fillna('Unknown', inplace=True)
df['listed_in'].fillna('Unknown', inplace=True)
df['release_year'].fillna(0, inplace=True)


def genre_distribution(df):
    genre_counts = df['listed_in'].str.split(', ').explode().value_counts().head(10)
    fig = px.bar(
        genre_counts,
        x=genre_counts.index,
        y=genre_counts.values,
        labels={'x': 'Genre', 'y': 'Count'},
        title='Top 10 Genres Distribution',
        color=genre_counts.values,
        color_continuous_scale='Reds'
    )
    return fig

def movie_distribution_by_country(df):
    import plotly.express as px

    country_counts = df['country'].dropna().str.split(', ').explode().value_counts()
    country_df = country_counts.reset_index()
    country_df.columns = ['country', 'count']

    fig = px.choropleth(
        country_df,
        locations='country',
        locationmode='country names',
        color='count',
        hover_name='country',
        color_continuous_scale='Reds',
        title='Movies/Shows Released by Country',
        range_color=(0, country_df['count'].max())  
    )

    fig.update_layout(geo=dict(showframe=False, projection_type='natural earth'))
    return fig


def release_year_trend(df):
    release_counts = df['release_year'].value_counts().sort_index()
    
    fig = px.line(
        x=release_counts.index,
        y=release_counts.values,
        labels={'x': 'Release Year', 'y': 'Number of Releases'},
        title='Release Trend Over the Years',
    )
    
   
    fig.update_traces(line=dict(color='red'))
    
    return fig


def top_directors(df):
    director_counts = (
        df['director']
        .dropna()
        .str.split(', ')
        .explode()
    )

    director_counts = director_counts[director_counts.str.lower() != 'unknown']

    
    top_counts = director_counts.value_counts().head(10)

    fig = px.bar(
        top_counts,
        x=top_counts.index,
        y=top_counts.values,
        labels={'x': 'Director', 'y': 'Count'},
        title='Top 10 Directors',
        color=top_counts.index, 
        color_discrete_sequence=['red']  
    )
    return fig

def rating_distribution(df):
    rating_counts = df['rating'].value_counts().nlargest(10)
    fig = px.bar(
        rating_counts, 
        x=rating_counts.index, 
        y=rating_counts.values,
        labels={'x': 'Rating', 'y': 'Count'},
        title='Content Rating Distribution',
        color_discrete_sequence=['red']
    )
    return fig

