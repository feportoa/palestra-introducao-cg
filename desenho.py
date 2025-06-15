# Criando um desenho

def desenhar(tilemap, setTile, cores):
    vermelho = cores["vermelho"]
    vermelho_escuro = cores["vermelho_escuro"]
    preto = cores["preto"]
    amarelo = cores["amarelo"]
    amarelo_queimado = cores["amarelo_queimado"]
    laranja = cores["laranja"]
    laranja_escuro = cores["laranja_escuro"]
    marrom_claro = cores["marrom_claro"]

    # Criando tiles
    # Vermelho
    setTile(tilemap, 7, 2, vermelho)
    setTile(tilemap, 8, 2, vermelho)
    setTile(tilemap, 9, 2, vermelho)

    setTile(tilemap, 6, 3, vermelho)
    setTile(tilemap, 10, 3, vermelho)

    setTile(tilemap, 5, 4, vermelho)
    setTile(tilemap, 11, 4, vermelho)

    setTile(tilemap, 12, 5, vermelho)
    setTile(tilemap, 5, 5, vermelho)

    setTile(tilemap, 7, 3, vermelho_escuro)
    setTile(tilemap, 8, 3, vermelho_escuro)
    setTile(tilemap, 9, 3, vermelho_escuro)

    setTile(tilemap, 6, 4, vermelho_escuro)
    setTile(tilemap, 7, 4, vermelho_escuro)
    setTile(tilemap, 8, 4, vermelho_escuro)
    setTile(tilemap, 9, 4, vermelho_escuro)
    setTile(tilemap, 10, 4, vermelho_escuro)

    setTile(tilemap, 6, 5, vermelho_escuro)
    setTile(tilemap, 7, 5, vermelho_escuro)
    setTile(tilemap, 8, 5, vermelho_escuro)
    setTile(tilemap, 9, 5, vermelho_escuro)
    setTile(tilemap, 10, 5, vermelho_escuro)
    setTile(tilemap, 11, 5, vermelho_escuro)

    setTile(tilemap, 8, 6, vermelho)
    setTile(tilemap, 9, 6, vermelho_escuro)
    setTile(tilemap, 11, 6, vermelho_escuro)
    setTile(tilemap, 12, 6, vermelho_escuro)

    setTile(tilemap, 8, 7, vermelho_escuro)
    setTile(tilemap, 9, 7, vermelho_escuro)
    setTile(tilemap, 10, 7, vermelho_escuro)
    setTile(tilemap, 11, 7, vermelho_escuro)
    setTile(tilemap, 12, 7, vermelho_escuro)

    setTile(tilemap, 8, 8, vermelho_escuro)
    setTile(tilemap, 9, 8, vermelho_escuro)
    setTile(tilemap, 10, 8, vermelho_escuro)
    setTile(tilemap, 11, 8, vermelho_escuro)
    setTile(tilemap, 12, 8, marrom_claro)
    setTile(tilemap, 7, 7, vermelho)
    setTile(tilemap, 7, 8, vermelho)

    setTile(tilemap, 8, 9, marrom_claro)
    setTile(tilemap, 9, 9, marrom_claro)
    setTile(tilemap, 10, 9, vermelho_escuro)
    setTile(tilemap, 11, 9, vermelho_escuro)

    setTile(tilemap, 10, 10, marrom_claro)
    setTile(tilemap, 11, 10, marrom_claro)

    # Amarelo e Laranja
    setTile(tilemap, 13, 6, amarelo)
    setTile(tilemap, 13, 7, amarelo)
    setTile(tilemap, 14, 7, amarelo)

    setTile(tilemap, 7, 6, laranja)
    setTile(tilemap, 6, 7, laranja)

    setTile(tilemap, 5, 8, laranja)
    setTile(tilemap, 6, 8, amarelo_queimado)

    setTile(tilemap, 4, 9, laranja)
    setTile(tilemap, 5, 9, amarelo)
    setTile(tilemap, 6, 9, laranja_escuro)
    setTile(tilemap, 7, 9, laranja_escuro)

    setTile(tilemap, 4, 10, laranja)
    setTile(tilemap, 3, 10, amarelo_queimado)
    setTile(tilemap, 5, 10, laranja_escuro)
    setTile(tilemap, 6, 10, laranja_escuro)
    setTile(tilemap, 7, 10, amarelo_queimado)
    setTile(tilemap, 8, 10, laranja_escuro)
    setTile(tilemap, 9, 10, laranja_escuro)

    setTile(tilemap, 3, 11, amarelo_queimado)
    setTile(tilemap, 4, 11, laranja)
    setTile(tilemap, 5, 11, amarelo)
    setTile(tilemap, 6, 11, laranja_escuro)
    setTile(tilemap, 7, 11, amarelo_queimado)
    setTile(tilemap, 8, 11, amarelo)
    setTile(tilemap, 9, 11, laranja_escuro)
    setTile(tilemap, 10, 11, amarelo_queimado)

    setTile(tilemap, 2, 12, laranja)
    setTile(tilemap, 3, 12, laranja_escuro)
    setTile(tilemap, 4, 12, laranja)
    setTile(tilemap, 5, 12, laranja_escuro)
    setTile(tilemap, 6, 12, amarelo)
    setTile(tilemap, 7, 12, laranja_escuro)
    setTile(tilemap, 8, 12, amarelo_queimado)
    setTile(tilemap, 9, 12, laranja_escuro)
    setTile(tilemap, 10, 12, laranja_escuro)

    setTile(tilemap, 2, 13, laranja)
    setTile(tilemap, 3, 13, laranja_escuro)
    setTile(tilemap, 4, 13, laranja_escuro)
    setTile(tilemap, 5, 13, laranja_escuro)
    setTile(tilemap, 6, 13, laranja_escuro)
    setTile(tilemap, 7, 13, amarelo)
    setTile(tilemap, 8, 13, laranja_escuro)
    setTile(tilemap, 9, 13, amarelo_queimado)
    setTile(tilemap, 10, 13, laranja_escuro)

    setTile(tilemap, 1, 14, laranja)
    setTile(tilemap, 2, 14, laranja_escuro)
    setTile(tilemap, 3, 14, laranja_escuro)
    setTile(tilemap, 4, 14, laranja_escuro)
    setTile(tilemap, 5, 14, amarelo_queimado)
    setTile(tilemap, 6, 14, laranja_escuro)
    setTile(tilemap, 7, 14, laranja_escuro)
    setTile(tilemap, 8, 14, amarelo)
    setTile(tilemap, 9, 14, laranja_escuro)
    setTile(tilemap, 10, 14, amarelo_queimado)

    setTile(tilemap, 1, 15, laranja)
    setTile(tilemap, 2, 15, laranja_escuro)
    setTile(tilemap, 3, 15, laranja_escuro)
    setTile(tilemap, 4, 15, laranja_escuro)
    setTile(tilemap, 5, 15, laranja_escuro)
    setTile(tilemap, 6, 15, laranja_escuro)
    setTile(tilemap, 7, 15, laranja_escuro)
    setTile(tilemap, 8, 15, laranja_escuro)
    setTile(tilemap, 9, 15, laranja_escuro)
    setTile(tilemap, 10, 15, laranja_escuro)
    setTile(tilemap, 11, 15, laranja_escuro)

    setTile(tilemap, 10, 6, preto)


