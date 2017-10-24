from moviepy.editor import *
from pydub import AudioSegment

ffmpeg_tools.ffmpeg_extract_audio("output/video_cut/video1_cut.mp4", "output/audio_mix1/audio_video1.mp3")
ffmpeg_tools.ffmpeg_extract_audio("output/video_cut/video2_cut.mp4", "output/audio_mix1/audio_video2.mp3")


audio_video1 = AudioSegment.from_mp3("output/audio_mix1/audio_video1.mp3")
audio_video2 = AudioSegment.from_mp3("output/audio_mix1/audio_video2.mp3")

#Crea un solo audio estratti dai due video che devono essere uniti
audio_video_mix = audio_video1 + audio_video2
audio_video_mix.export("output/audio_mix1/audio_video_mix.mp3", format="mp3")


colonna_sonora = AudioSegment.from_mp3("resources/audio/Bumper_Tag.mp3")
audio_video_mix = AudioSegment.from_mp3("output/audio_mix1/audio_video_mix.mp3")

#il volume dell'audio della musica viene aumentato di 10db
colonna_sonora_audio_alto = colonna_sonora + 10

#all'audio dei due video viene aggiunta la musica  e viene creato il file .mp3 relativo
audio_video = audio_video_mix.overlay(colonna_sonora_audio_alto, position=0000)
audio_video.export("output/audio_mix1/audio_video.mp3", format="mp3")


#recupera il file mp3 con il mix audio video + nuova musica
audio_video = AudioFileClip("output/audio_mix1/audio_video.mp3")


#seleziona il video
video1 = (VideoFileClip("output/video_cut/video1_cut.mp4"))
video2 = (VideoFileClip("output/video_cut/video2_cut.mp4"))
durata_video1= video1.duration
durata_video2= video2.duration

nuovo_video =  concatenate_videoclips([video1, video2]).set_audio(audio_video).set_duration(durata_video1 + durata_video2)
        

#esporta il nuovo video
nuovo_video.write_videofile("output/audio_mix1/audio_mix1.mp4", fps=25)