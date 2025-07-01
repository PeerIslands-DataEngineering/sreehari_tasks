import os
from google.cloud import bigquery
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/saisr/Downloads/ithaproj1-bc5441d8be23.json'
client = bigquery.Client(project="ithaproj1")

# Step 2: Load CSV
df = pd.read_csv("C:/Users/saisr/Downloads/movie_genre_classification_final.csv")
df = df.drop_duplicates()

# Step 3: Dimension - Director
df_director = df[['Director']].drop_duplicates().reset_index(drop=True)
df_director['director_id'] = df_director.index + 1
df = df.merge(df_director, on='Director', how='left')
client.load_table_from_dataframe(
    df_director[['director_id', 'Director']],
    "ithaproj1.miniproj.dim_director",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
)

# Step 4: Dimension - Genre
df_genre = df[['Genre']].drop_duplicates().reset_index(drop=True)
df_genre['genre_id'] = df_genre.index + 1
df = df.merge(df_genre, on='Genre', how='left')
client.load_table_from_dataframe(
    df_genre[['genre_id', 'Genre']],
    "ithaproj1.miniproj.dim_genre",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
)

# Step 5: Dimension - Actor
df_actor = df[['Lead_Actor']].drop_duplicates().reset_index(drop=True)
df_actor['actor_id'] = df_actor.index + 1
df = df.merge(df_actor, on='Lead_Actor', how='left')
client.load_table_from_dataframe(
    df_actor[['actor_id', 'Lead_Actor']],
    "ithaproj1.miniproj.dim_actor",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
)

# Step 6: Dimension - Language
df_language = df[['Language']].drop_duplicates().reset_index(drop=True)
df_language['language_id'] = df_language.index + 1
df = df.merge(df_language, on='Language', how='left')
client.load_table_from_dataframe(
    df_language[['language_id', 'Language']],
    "ithaproj1.miniproj.dim_language",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
)

# Step 7: Create and upload fact_movies table
df_fact_movies = df[['Title', 'Year', 'Duration', 'Rating', 'Votes', 'Budget_USD',
                     'BoxOffice_USD', 'Content_Rating', 'Num_Awards', 'Critic_Reviews',
                     'director_id', 'genre_id', 'actor_id', 'language_id']]
client.load_table_from_dataframe(
    df_fact_movies,
    "ithaproj1.miniproj.fact_movies",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
)

print("Upload completed to ithaproj1.miniproj dataset.")
