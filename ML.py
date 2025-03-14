import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('cleaned_data.csv')


for col in ['description', 'director', 'listed_in']:
    df[col].fillna('Unknown', inplace=True)


df['features'] = df['title'] + ' ' + df['listed_in'] + ' ' + df['director'] + ' ' + df['description']


vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


title_index_map = pd.Series(df.index, index=df['title'].str.lower()).to_dict()

def recommend_movies(title, top_n=5):
   
    title_lower = title.strip().lower()
    
    if title_lower not in title_index_map:
        return f"Movie '{title}' not found in dataset."

    idx = title_index_map[title_lower]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    
   
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommended_titles = [df.iloc[movie[0]]['title'] for movie in sorted_movies]
    return recommended_titles

if __name__ == "__main__":
    print("\n🎬 Welcome to the Netflix Movie Recommender! 🎬\n")
    
    while True:
        try:
            movie_name = input("Enter a movie title (or type 'exit' to quit): ").strip()
            
            if movie_name.lower() == 'exit':
                print("Exiting the recommendation system. Goodbye!")
                break

            recommendations = recommend_movies(movie_name)
            
            if isinstance(recommendations, list):
                print(f"\nRecommended movies for '{movie_name}':")
                for rec in recommendations:
                    print(f"- {rec}")
            else:
                print(recommendations)

        except Exception as e:
            print(f"⚠️ An error occurred: {e}")
