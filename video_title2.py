from moviepy.editor import *

my_clip = VideoFileClip("resources/video/video_add_music.mp4", audio=True).subclip(0,10) 

txt = TextClip("Testo Testo", font='resources/fonts/Pacifico.ttf', color='white',fontsize=100)

txt_col = txt.on_color(size=(1920,200), color=(0,0,0), pos=('center', 'center'), col_opacity=0.6)
txt_mov = txt_col.set_pos(("center","bottom") )
final = CompositeVideoClip([my_clip,txt_mov])
final.duration = 10
final.subclip(0,10).write_videofile("output/video_title2/video_title2.mp4",fps=24,codec='libx264')