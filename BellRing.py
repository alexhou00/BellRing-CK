from pygame import mixer
from datetime import datetime
#from time import sleep

mixer.init()

mixer.music.load("./bell_CK.mp3")

times = (( 7,20), ( 8, 0), ( 8,10), ( 9, 0), ( 9,10), (10, 0), (10,10), (11, 0), (11,10), (12, 0),
         (13, 0), (13,50), (14, 0), (14,50), (15,10), (16, 0), (16,10), (17, 0))
print("\nProgram running...")
while True:
    h = datetime.now().time().hour
    m = datetime.now().time().minute
    s = datetime.now().time().second
    if (h, m) in times and s <= 10 and s >= 1:
        mixer.music.play()
        while mixer.music.get_busy(): pass
