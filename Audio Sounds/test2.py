

from playsound import playsound
from pydub import AudioSegment


song = AudioSegment.from_wav("right_intro_wav.wav")

loud = song + 6

playsound(loud)
#save louder song
# louder_song.export("louder_song.mp3", format='mp3')
