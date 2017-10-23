from moviepy.editor import *

my_clip = VideoFileClip("resources/video/video_add_music.mp4", audio=True).subclip(0,10)

txt = TextClip("Test Titolo", font='resources/fonts/IndieFlower.ttf', color='white',fontsize=120)
txt_col = txt.on_color(size=(960,1080), color=(0,0,0), pos=('center','center'), col_opacity=0.6)

final = CompositeVideoClip([my_clip,txt_col])
final.duration = 10
final.write_videofile("output/video_title1/video_title1.mp4",fps=24,codec='libx264')