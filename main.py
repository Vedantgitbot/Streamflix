import streamlit as st
import pandas as pd
from Chart import genre_distribution, movies_by_country, release_year_trend, top_directors

from ML import recommend_movies


st.set_page_config(page_title="Netflix Data Dashboard", layout="wide")


st.title("Netflix Data Analysis & Movie Recommendation")


st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose a page", ["Data Analysis","Movie Recommendations"])


if options == "Data Analysis":
    st.header("Data Analysis")
    
    st.subheader("1. Genre Distribution")
    genre_fig = genre_distribution()
    st.plotly_chart(genre_fig, use_container_width=True)
    
    st.subheader("2. Movies by Country")
    country_fig = movies_by_country()
    st.plotly_chart(country_fig, use_container_width=True)
    
    st.subheader("3. Movie Release Trend Over the Years")
    release_trend_fig = release_year_trend()
    st.plotly_chart(release_trend_fig, use_container_width=True)
    
    st.subheader("4. Top 10 Directors")
    directors_fig = top_directors()
    st.plotly_chart(directors_fig, use_container_width=True)




elif options == "Movie Recommendations":
    st.header("Movie Recommendations")
    
    st.subheader("Enter a movie title to get recommendations")
    movie_name = st.text_input("Movie Title")
    
    if movie_name:
        recommendations = recommend_movies(movie_name)
        
        if isinstance(recommendations, list):
            st.write(f"Recommended movies for '{movie_name}':")
            for rec in recommendations:
                st.write(f"- {rec}")
        else:
            st.write(recommendations)

