from desenho import desenhar

def setTile(tilemap, tileX, tileY, tileColor):
    tilemap[tileY][tileX] = tileColor

def render(width, height, framebuffer, TILE_SIZE, tilemap):
    for y in range(height):
        for x in range(width):
            ty = int(y // TILE_SIZE)
            tx = int(x // TILE_SIZE)
            # Checa se a tile atual é maior do que zero e menor do que o tilemap
            if 0 <= ty < len(tilemap) and 0 <= tx  < len(tilemap[0]):
                if tilemap[ty][tx] == None:
                    framebuffer[y * width + x] = (77, 182, 172)
                else:
                    framebuffer[y * width + x] = tilemap[ty][tx]

# Proporção NES
aspectRatio = 16/15

width = 256
height = int(width/aspectRatio)

# Configurando o tilemap
TILE_SIZE = height // 16 # 16 é meu número desejado de tiles

tiles_x = width // TILE_SIZE
tiles_y = height // TILE_SIZE

# "Tileset" com cores
fundo = (77, 182, 172)

cores = {
    "vermelho": (216, 67, 21),
    "vermelho_escuro": (191, 54, 12),
    "preto": (0,0,0),
    "amarelo_queimado": (245, 127, 23),
    "laranja": (251, 140, 0),
    "laranja_escuro": (239, 108, 0),
    "amarelo": (255, 238, 88),
    "marrom_claro": (167, 54, 12)
}

# Criando um tilemap
tilemap = []
for y in range(int(tiles_y)):
        row = []
        for x in range(int(tiles_x)):
            if y == tiles_y - 1:
                row.append(fundo)
            else:
                row.append(None)
        tilemap.append(row)

# Criando e preenchendo um framebuffer com cor sólida - Azul claro
framebuffer = [(77, 182, 172) for _ in range(width * height)]

desenhar(tilemap, setTile, cores)

render(width, height, framebuffer, TILE_SIZE, tilemap)

# Escrevendo nosso arquivo em PPM P3
f = open('result.ppm', 'w')

f.write(f'P3\n{width} {height}\n255\n')

# Escrevendo o framebuffer
for y in range(height):
    for x in range(width):
        fb = framebuffer[y * width + x]
        f.write(f'{fb[0]} {fb[1]} {fb[2]} ')
    f.write('\n')

# Nunca esqueça de FECHAR o seu arquivo!!
f.close()
