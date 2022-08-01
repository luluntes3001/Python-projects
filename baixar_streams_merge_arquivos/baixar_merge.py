from moviepy.editor import *
from pytube import YouTube
#Como mostrado acima deve-se instalar e importar duas bibliotecas para está atividade

#O comando abaixo serve para descobrir quais arquivos você gostaria de baixar
print(YouTube('link').streams.filter())
#Após escolhido é só substituit o itagnumber pelo número do arquivo escolhido
YouTube('link').streams.get_by_itag(itagnumber).download('C:/seu-diretório-de-escolha')

#Agora vamos fazer de conta que foram baixados arquivos de
#audio e video separados e você gostaria de juntá-los
clip = VideoFileClip("video.mp4")  #só colocar no nome caso esteja na pasta, senão colocar o diretórico de escolha
audioclip = AudioFileClip("audio.mp3")
videoclip = clip.set_audio(audioclip)

#Criar o arquivo com:
videoclip.write_videofile("final.mp4")