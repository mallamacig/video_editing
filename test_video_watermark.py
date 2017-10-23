from moviepy.editor import *

my_clip = VideoFileClip("1.mp4", audio=True)  #  The video file with audio enabled

w,h = my_clip.size  # size of the clip

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

txt = TextClip("THE WATERMARK TEXT", font='Anton.ttf',
                   color='white',fontsize=120)

txt_col = txt.on_color(size=(1000,300), color=(0,0,0), pos=(200,'center'), col_opacity=0.6)

# This example demonstrates a moving text effect where the position is a function of time(t, in seconds).
# You can fix the position of the text manually, of course. Remember, you can use strings,
# like 'top', 'left' to specify the position
# txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),
#                                   max(5*h/6,int(100*t))) )
#txt_mov = txt_col.set_pos( 100, 100 )
# Write the file to disk
final = CompositeVideoClip([my_clip,txt_col])
final.duration = 10
final.write_videofile("test_video_watermark.mp4",fps=24,codec='libx264')