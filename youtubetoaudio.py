import whisper
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

video_url = input("enter url of the video: ")
# video_url = 'https://www.youtube.com/watch?v=u-pP_dCenJA'
yt = YouTube(video_url)
audio_stream = yt.streams.filter(only_audio=True).first()


audio_stream.download(output_path='path_to_save_audio')

import os
original_file = 'path_to_save_audio/' + audio_stream.default_filename
new_file = 'path_to_save_audio/' + 'audio.mp3'
os.rename(original_file, new_file)

model = whisper.load_model("base")
result = model.transcribe(new_file)
with open("hello.txt","w") as f:
  f.write(result["text"])