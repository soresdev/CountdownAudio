import time
from pygame import mixer

# Init our mixer to play our audio
mixer.init()
mixer.music.load("audio.mp3")


def playsound():
    # Set volume to 100 & play the sound
    mixer.music.set_volume(100)
    mixer.music.play()

    # Allow time for sound to play & end
    time.sleep(3)


def tick(ti):
    while ti:
        minutes, seconds = divmod(ti, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end='\n')
        time.sleep(1)
        ti -= 1

    # When timer runs out, send a message and play the sound.
    print('Here comes the audio!')
    playsound()


countdown_time = int(input('How many seconds would you like to countdown? '))

tick(countdown_time)
