from moviepy.editor import *

my_clip = VideoFileClip("video_test.mp4", audio=True) 

txt = TextClip("Testo Testo", font='Pacifico.ttf', color='white',fontsize=100)

txt_col = txt.on_color(size=(1920,200), color=(0,0,0), pos=('center', 'center'), col_opacity=0.6)
txt_mov = txt_col.set_pos(("center","bottom") )
final = CompositeVideoClip([my_clip,txt_mov])

final.subclip(0,5).write_videofile("video_title6.mp4",fps=24,codec='libx264')