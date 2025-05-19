import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import os

warnings.filterwarnings("ignore", category=UserWarning)


caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'data', 'movies.csv')
df = pd.read_csv(caminho_arquivo)

df['genres'] = df['genres'].fillna('')

vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = vectorizer.fit_transform(df['genres'])

cos_sim = cosine_similarity(genre_matrix, genre_matrix)  

def recomendar_filmes(titulo_filme, n=10):
    if titulo_filme not in df['title'].values:
        print("Filme não encontrado no banco de dados.")
        return []

    idx = df[df['title'] == titulo_filme].index[0]
    similaridades = list(enumerate(cos_sim[idx]))  
    similaridades = sorted(similaridades, key=lambda x: x[1], reverse=True)
    similaridades = similaridades[1:n+1]  
    indices = [i[0] for i in similaridades]
    recomendacoes = df['title'].iloc[indices]
    return recomendacoes.tolist()
