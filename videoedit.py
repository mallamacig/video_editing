import PIL
from PIL import Image
import json
import moviepy.audio.fx.all as afx
from moviepy.editor import *
import moviepy.video.fx.all as vfx
from moviepy.video.io.VideoFileClip import VideoFileClip
import os.path
from pydub import AudioSegment

def converti_timestamp(timestamp):
    """Convert la timestamp in secondi"""
    timestamp = timestamp.strip()
    chunk, millis = timestamp.split('.')
    hours, minutes, seconds = chunk.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    seconds = seconds + hours * 60 * 60 + minutes * 60 + float(millis) / 1000
    return seconds

def CreaVideo(item):
    esegui = False
    if (os.path.isfile(item["file_out"])):
        if (item["overwrite"]==True):
            esegui=True
    else:
        esegui=True

    if (esegui):
        speedx=1
        if (item["effetti"] is not None):
            if (item["effetti"]["speedx"] is not None):
                speedx=item["effetti"]["speedx"]

        clip = (VideoFileClip(item["origine"]).subclip(converti_timestamp(item["inizio"]), converti_timestamp(item["fine"])))
        newclip = (clip.fx(vfx.fadein, duration=item["fade_in"])
                     .fx(vfx.fadeout, duration=item["fade_out"])
                     .fx( vfx.resize, width=item["width"], height=item["height"])
                     .fx( vfx.speedx, factor=speedx)
                     )
        newclip.write_videofile(item["file_out"], fps=25)

def CreaTitolo(item):
    esegui = False
    if (os.path.isfile(item["file_out"])):
        if (item["overwrite"]==True):
            esegui=True
    else:
        esegui=True

    if (esegui):
        screensize = (item["width"], item["height"])
        txtClip = TextClip(item["testo"], color=item["color"], font=item["font"], fontsize=item["font_size"])
        audio = AudioFileClip("audio_no.mp3")
        cvc = CompositeVideoClip( [txtClip.set_pos('center')], size=screensize).set_audio(audio).set_duration(item["durata"])
        newclip = (cvc.fx(vfx.fadein, duration=item["fade_in"])
                     .fx(vfx.fadeout, duration=item["fade_out"])
                     .fx( vfx.resize, width=item["width"], height=item["height"])
                     )

        newclip.write_videofile(item["file_out"], fps=25)

def CreaImmagine(item):
    img = Image.open(item["origine"])

    img = img.resize((item["width"], item["height"]), PIL.Image.ANTIALIAS)
    img.save(item["origine"])
    esegui = False
    if (os.path.isfile(item["file_out"])):
        if (item["overwrite"]==True):
            esegui=True
    else:
        esegui=True

    if (esegui):
        print(item["origine"])
        clip = ImageClip((item["origine"].encode('utf-8')), duration=item["durata"])
        audio = AudioFileClip("audio_no.mp3")
        cvc = CompositeVideoClip([clip], (item["width"], item["height"])).set_audio(audio).set_duration(item["durata"])
        newclip = (cvc.fx(vfx.fadein, duration=item["fade_in"])
            .fx(vfx.fadeout, duration=item["fade_out"]))

        newclip.write_videofile(item["file_out"], fps=25)

def CreaColore(item):
    esegui = False
    if (os.path.isfile(item["file_out"])):
        if (item["overwrite"]==True):
            esegui=True
    else:
        esegui=True

    if (esegui):
        screensize = (item["width"], item["height"])
        clip = ColorClip(screensize, duration=item["durata"], col=(item["colore_r"], item["colore_g"], item["colore_b"]))
        audio = AudioFileClip("audio_no.mp3")
        cvc = CompositeVideoClip([clip], clip.size).set_audio(audio).set_duration(item["durata"])
        newclip = (cvc.fx(vfx.fadein, duration=item["fade_in"])
             .fx(vfx.fadeout, duration=item["fade_out"]))
        newclip.write_videofile(item["file_out"], fps=25)
        #clip.write_videofile(item["file_out"], fps=25)

def Concatena(item):
    esegui = False
    if (os.path.isfile(item["file_out"])):
        if (item["overwrite"]==True):
            esegui=True
    else:
        esegui=True

    if (esegui):


        #output = file_audio - 17.5
        clips=[]
        durata =0
        contatore=0
        for clip_item in item["file_in"]:
             clip = VideoFileClip(clip_item)
             clip.set_position = contatore
             clip.set_duration(clip.duration)
             clip.w= item["width"]
             clip.h= item["height"]
             clips.append(clip)
             durata = durata + clip.duration
             #print(clip_item)
             ffmpeg_tools.ffmpeg_extract_audio(clip_item, 'audio_video_' + str(contatore) + '.mp3')
             contatore = contatore + 1

        contatore=0
        audio_items=[]
        for clip_item in item["file_in"]:
            file_audio_video = AudioSegment.from_mp3('audio_video_' + str(contatore) + '.mp3')
            audio_items.append(file_audio_video)
            contatore= contatore + 1

        contatore=0
        for audio_item in audio_items:
            if contatore==0:
                audio_video = audio_item
            else:
                audio_video = audio_video + audio_item
            contatore = contatore+1
        audio_video = audio_video + item["piu_db_volume_video_main"]
        audio_video = audio_video - item["meno_db_volume_video_main"]
        audio_video.export("audio_video_main.mp3", format="mp3")

        file_audio = AudioFileClip(item["file_audio"]).subclip(0, durata)
        new_file_audio = (file_audio.fx(afx.volumex, item["volume_file_audio"])
            .fx(afx.audio_fadein, duration=item["volume_file_audio_fade_in"])
            .fx(afx.audio_fadeout, duration=item["volume_file_audio_fade_out"]))
        new_file_audio.write_audiofile("file_audio_elab.mp3")

        audio_video = AudioSegment.from_file("audio_video_main.mp3", format="mp3")
        audio_colonna_sonora = AudioSegment.from_file("file_audio_elab.mp3", format="mp3")
        output = audio_video.overlay(audio_colonna_sonora, position=0000)
        output.export("output_audio.mp3", format="mp3")

        audio = AudioFileClip("output_audio.mp3").subclip(0, durata)
        new_audio = (audio.fx(afx.volumex, item["volume_audio"])
            .fx(afx.audio_fadein, duration=item["fade_in"])
            .fx(afx.audio_fadeout, duration=item["fade_out"]))

        cvc =  concatenate_videoclips(clips).set_duration(durata)
        newclip = (cvc.fx(vfx.fadein, duration=item["fade_in"])
             .fx(vfx.fadeout, duration=item["fade_out"])).set_audio(new_audio)
        newclip.write_videofile(item["file_out"], fps=25)

with open('video_saggio_test.json') as data_file:
    data = json.load(data_file)
    for item in data:
        print(item)
        if (item["tipologia"] == "video"):
            CreaVideo(item)
        if (item["tipologia"] == "titolo"):
            CreaTitolo(item)
        if (item["tipologia"] == "immagine"):
            CreaImmagine(item)
        if (item["tipologia"] == "colore"):
            CreaColore(item)
        if (item["tipologia"] == "concatena"):
            Concatena(item)
