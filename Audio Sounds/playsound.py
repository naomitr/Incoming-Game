from pydub import AudioSegment #imports library to access audio files
from pydub.playback import play #imports library to play audio file
sound = AudioSegment.from_wav("left_intro_wav.wav") # sets variable as audio file
play(sound) # control sound; sound in its regular volume
two_second = 2 * 1000 #selects two seconds of the file
firstone= sound[:two_second] #sets it as a variable
beginning=firstone + 10 #increases volume
play(beginning) #plays the file with increased volume
beginning=firstone - 10 #decreases volume of audio file
play(beginning) #plays the file with decreased volume
