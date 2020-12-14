from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('sample1.mp3')
play(sound)