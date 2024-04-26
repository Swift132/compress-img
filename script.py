from PIL import Image
import os

def otimizar_imagens(pasta_origem, pasta_destino, largura_max=800, qualidade=85):
    # Verifica se a pasta de destino existe, se não, cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Percorre todas as imagens na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            caminho_origem = os.path.join(pasta_origem, arquivo)
            caminho_destino = os.path.join(pasta_destino, arquivo)

            # Abre a imagem
            imagem = Image.open(caminho_origem)

            # Redimensiona a imagem mantendo a proporção
            largura, altura = imagem.size
            proporcao = largura / altura
            nova_largura = min(largura, largura_max)
            nova_altura = int(nova_largura / proporcao)
            imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.ANTIALIAS)

            # Salva a imagem otimizada
            imagem_redimensionada.save(caminho_destino, optimize=True, quality=qualidade)

            print(f"Imagem otimizada: {caminho_destino}")

pasta_origem = './'
pasta_destino = './resultado'

# Chama a função para otimizar as imagens
otimizar_imagens(pasta_origem, pasta_destino)
