import pandas as pd

df = pd.read_csv('/Users/vedantbrahmbhatt/Desktop/Netflix_EDA/netflix_movies .csv')

df = df.drop_duplicates(subset='show_id', keep='first')

df['release_year'] = df['release_year'].fillna(df['release_year'].mode()[0])
df['duration'] = df['duration'].fillna(df['duration'].mode()[0])

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')
df['listed_in'] = df['listed_in'].fillna('Unknown')
df['description'] = df['description'].fillna('No description')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

df['duration'] = df['duration'].apply(lambda x: ''.join(filter(str.isdigit, str(x))) if isinstance(x, str) else x)
df['duration'] = pd.to_numeric(df['duration'], errors='coerce')

df = df.dropna(subset=['release_year', 'duration'])

df = df.reset_index(drop=True)

df.to_csv('cleaned_data.csv', index=False)

print("Data cleaning completed and saved to 'cleaned_data.csv'.")
