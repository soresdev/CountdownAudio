import time
from pygame import mixer

# Init our mixer to play our audio
mixer.init()
mixer.music.load("audio.mp3")

# Init some variables
volume_message = "What should the volume be? "
countdown_time = 10
volume = 100


# Set variables from user
def setup():
    global countdown_time
    global volume

    countdown_time = int(input("How many seconds would you like to countdown? "))
    volume = int(input(volume_message))

    # If they try to set volume lower than zero, make them retry
    if volume < 0:
        print("The volume cannot be less than zero.")
        print('\n')
        volume = int(input(volume_message))

    # If they try to set volume more than 100, make them retry
    elif volume > 100:
        print("The volume cannot be greater than 100.")
        print('\n')
        volume = int(input(volume_message))


def playsound(vol):
    # Set volume to 100 & play the sound
    mixer.music.set_volume(vol)
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
    playsound(volume)


setup()

tick(countdown_time)
