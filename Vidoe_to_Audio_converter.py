import os
import moviepy.editor
from tkinter.filedialog import *

start = "/home/abdullah/Study/JOB/PythonFun/"

vdo = askopenfilename()
relative_path = os.path.relpath(vdo, start)

audio_name = relative_path.replace('.mp4','')+".mp3"

video = moviepy.editor.VideoFileClip(vdo)
ado = video.audio
ado.write_audiofile(audio_name)
print("Video to Audio conveted Successfully")
