from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip

video1_cut = VideoFileClip("resources/video/video1.mp4").subclip(2, 8)
video1_cut.write_videofile("output/video_cut/video1_cut.mp4", fps=25)

video2_cut = VideoFileClip("resources/video/video2.mp4").subclip(0, 10)
video2_cut.write_videofile("output/video_cut/video2_cut.mp4", fps=25)