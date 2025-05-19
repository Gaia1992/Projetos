from src.recomendador import recomendar_filmes

if __name__ == "__main__":
    filme = input("Digite o nome de um filme (ex: Heat (1995)): ")
    resultados = recomendar_filmes(filme)

    if resultados:
        print("\nFilmes recomendados:")
        for r in resultados:
            print(r)
