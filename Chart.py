
import pandas as pd
import plotly.express as px


df = pd.read_csv('cleaned_data.csv')


df['country'].fillna('Unknown', inplace=True)
df['listed_in'].fillna('Unknown', inplace=True)
df['release_year'].fillna(0, inplace=True)


def genre_distribution():
    genre_counts = df['listed_in'].str.split(', ').explode().value_counts().head(10)
    fig = px.bar(
        genre_counts,
        x=genre_counts.index,
        y=genre_counts.values,
        labels={'x': 'Genre', 'y': 'Count'},
        title='Top 10 Genres Distribution',
        color=genre_counts.values,
        color_continuous_scale='Blues'
    )
    return fig

import plotly.express as px

def movies_by_country():
    country_counts = df['country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']
    
    color_scale = px.colors.sequential.Turbo

    fig = px.choropleth(
        country_counts,
        locations='country',
        locationmode='country names',
        color='count',
        color_continuous_scale=color_scale,
        title='Movies Distribution by Country',
        labels={'count': 'Number of Movies'},
        template='plotly_dark'  
    )
    
    fig.update_layout(
        coloraxis_colorbar=dict(
            title="Number of Movies",
            tickvals=[1, 10, 50, 100, 500, 1000, 2000],
            ticktext=['1', '10', '50', '100', '500', '1000', '2000'],
        ),
        geo=dict(
            showcoastlines=True,
            coastlinecolor="Black",
            showland=True,
            landcolor="lightgray",
            projection_type="natural earth"
        )
    )
    
    return fig


def release_year_trend():
    release_counts = df['release_year'].value_counts().sort_index()
    fig = px.line(
        release_counts,
        x=release_counts.index,
        y=release_counts.values,
        labels={'x': 'Release Year', 'y': 'Number of Movies'},
        title='Movie Release Trend Over the Years'
    )
    return fig


def top_directors():
    director_counts = df[df['director'] != 'Unknown']['director'].value_counts().head(10)
    
    fig = px.bar(
        director_counts,
        x=director_counts.index,
        y=director_counts.values,
        labels={'x': 'Director', 'y': 'Count'},
        title='Top 10 Directors with Most Movies',
        color=director_counts.values,
        color_continuous_scale='Viridis'
    )
    return fig

