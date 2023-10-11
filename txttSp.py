import gtts
import vlc
import time

audio = gtts.gTTS("I Do not care if you're bored. If you have time to slouch around and claim that you're bored try helping your mum or visiting your grandma or getting a job!")

audio.save("try1.mp3")

file = vlc.MediaPlayer("try1.mp3")

file.play()
time.sleep(60)
file.stop()

exit()



