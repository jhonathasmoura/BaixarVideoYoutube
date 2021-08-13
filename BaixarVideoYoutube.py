try:
    from pytube import YouTube  #Importando o módulo
except:
    print('Instale o pytube -> pip install pytube')
else:
    link = input('Digite o link do vídeo: ')
    yt = YouTube(link)  #Cria uma instância da classe YouTube

    print('\n---INFORMAÇÕES DO VÍDEO---')
    print(f'Título: {yt.title}')
    print(f'Visualizações: {yt.views}')
    print(f'Canal: {yt.author}')
    print(f'Duração: {yt.length} segundos')

    diretorio = input('\nDigite o diretório onde o vídeo será salvo: ')
    
    video = yt.streams.get_highest_resolution()  #Obtendo a melhor resolução para o vídeo

    print('Baixando...')
    video.download(diretorio)  #Baixando o vídeo para o destino especificado
    print('Download concluído!')