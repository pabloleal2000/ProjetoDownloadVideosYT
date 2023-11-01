#Desenvolvido por Pablo Borba Leal

from tkinter import*
from pytube import YouTube
import os

def mp3():	#Função para baixar o link do YT em MP3

    user = os.getenv('USERNAME')	#Pega o Username do usuario
    url = url1.get()# Recebe o link do video qual o usuario deseja baixar
    video = YouTube(url).streams.get_audio_only()	#Responsavel por pegar apenas o audio na url fornecida pelo usuario
    video.download(rf'C:\Users\{user}\Desktop\Youtube Downloads\MP3')
    title = str(video.title)  #Pega o titulo do video
    clip = mp.AudioFileClip(
        rf'C:\Users\{user}\Desktop\Youtube Downloads\MP3\{title}.mp4')  #A biblioteca força baixar os 2 arquivos ENTAO Local onde e salvo o MP4
    clip.write_audiofile(
        rf'C:\Users\{user}\Desktop\Youtube Downloads\MP3\{title}.mp3')	#Local onde e salvo o MP3 mudando nome de usuario e usando o proprio nome do video para nomear o arquivo
    os.remove(
        rf'C:\Users\{user}\Desktop\Youtube Downloads\MP3\{title}.mp4')  #Responsavel por deletar o MP4 pois nesse caso o usuario escolheu apenas o MP3
    print('Obrigado por aguardar Download Concluido :D')	#Indica finalizaçao do Download no terminal 



def mp4():# Função para baixar o link do YT em MP4

    user = os.getenv('USERNAME')  #Pega o Username do usuario
    url = url1.get() #Recebe o link do video qual o usuario deseja baixar
    video = YouTube(url)
    video = video.streams.get_highest_resolution()  #Responsavel em converter o arquivo para que o usuario deseja nesse caso Audio e Video
    video.download(rf'C:\Users\{user}\Desktop\Youtube Downloads\MP4')  #Local onde e salvo o MP4
    print('Obrigado por aguardar Download Concluido :D') #Indica finalizaçao do Download no terminal 



#Parte visual do projeto
janela = Tk() #Definindo uma janela
janela.title('Conversor YT By Pablo Borba') #Definindo titulo para janela
janela.geometry('372x120') #Definindo tamanho que a janela deve abrir
janela.resizable(False, False) #Definindo permissão para o usuario não redimencionar a janela
janela.iconbitmap('Youtube_icon.ico') #Definindo ico para a janela
janela.config(background="#000000") #Definindo coloração da janela nesse caso preta

url1=Entry(janela) #Definindo uma entrada para a janela
url1.insert(0,'Insira a Url Aqui!') #Inserindo text de ajuda no input para ajudar o usuario a intender melhor o funcionamento
url1.place(x=10, y=15, width=350, height=20) #Definindo local onde ira ficar na janela

mp3 = Button(janela, text='MP3',bg='#ff0000', font='bold' , command=mp3) #Definindo botao e ligando ele a função MP3
mp3.place(x=10, y=40, width=350, height=30) #Definindo local onde ira ficar na janela

mp4 = Button(janela, text='MP4',bg='#ff0000', font='bold' , command=mp4) #Definindo botao e ligando ele a função MP4
mp4.place(x=10, y=75, width=350, height=30) #Definindo local onde ira ficar na janela

janela.mainloop() #Criando um loop para a janela