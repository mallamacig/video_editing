import PIL
from PIL import Image
import json
import moviepy.audio.fx.all as afx
from moviepy.editor import *
import moviepy.video.fx.all as vfx
from moviepy.video.io.VideoFileClip import VideoFileClip
import os.path
from pydub import AudioSegment

durata=10

#Estrae dal file video la traccia sonora e la salva in formato .mp3
ffmpeg_tools.ffmpeg_extract_audio("video_test.mp4", 'audio_video_test.mp3')

#seleziona la traccia audio della colonna sonora
#audio_colonna_sonora = AudioSegment.from_file("Raw_Deal.mp3", format="mp3")
audio_colonna_sonora = AudioSegment.from_file("Bumper_Tag.mp3", format="mp3")

#seleziona la traccia audio del video precedentemente estratta con ffmpeg_tools
audio_video = AudioSegment.from_file("audio_video_test.mp3", format="mp3")

#miscela in un solo mp3 l'audio originale del video + la colonna sonora
audio_add_music_mix = audio_video.overlay(audio_colonna_sonora, position=0000)
#salva in mp3 la colonna sonora + l'audio originale del video
audio_add_music_mix.export("audio_add_music.mp3", format="mp3")

#recupera il file mp3 con il mix audio video + nuova musica
audio_add_music = AudioFileClip("audio_add_music.mp3")

#seleziona il video
clip = (VideoFileClip("video_test.mp4"))
#crea una nuovo video con l'audio mix audio video+ nuova musica
newclip = (clip.fx(vfx.fadein, 2).fx(vfx.fadeout, 2).set_audio(audio_add_music))

#esporta il nuovo video
newclip.write_videofile("video_test_add_music.mp4", fps=25)