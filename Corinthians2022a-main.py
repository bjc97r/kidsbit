from   microbit import *
import music
import random

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

msg = ['THEREFORE',
       'IF ANYONE IS IN CHRIST',
       'THE NEW CREATION HAS COME',
       'THE OLD HAS GONE',
       'THE NEW IS HERE!',
       '2 CORINTHIANS 5:17']

snd  = [Sound.TWINKLE, Sound.HAPPY, Sound.HELLO,
        Sound.SOARING, Sound.SPRING, Sound.SLIDE ]
song = [music.DADADADUM, music.ENTERTAINER, 
        music.FUNK, music.CHASE, music.PUNCHLINE, music.WAWAWAWAA ]
img  = [Image.SMILE, Image.RABBIT, Image.DUCK, 
        Image.GIRAFFE, Image.COW, Image.XMAS]
n    = len(msg)

s1  = ["C5:4", "C:2", "C:2", "C:4", "D:4", "F:16"];
s2  = ["A:4", "A:2", "A:2", "A:4", "G:4", "F:16"];
s3  = ["D:4", "F:2", "F:2", "F:4", "G:4", "F:16"];
s4  = ["F:4", "F:2", "F:2", "F:4", "D:4", "C:16"];
s2a = ["A:4", "A:2", "A:2", "A:4", "G:4", "F:8"];
s5  = ["F:4", "G:4", "A:8", "A:4", "A:4", "G:8"];
s6  = ["A:4", "G:4", "F:16"];
little_light = s1+s2+s3+s4+s1+s2a+s5+s6;

music.play(music.POWER_UP,wait=False)
display.show(flash, delay=100)
display.show(flash, delay=50)
display.scroll('JESUS')
display.show(Image.HEART)
sleep(500)
display.show(Image.HEART_SMALL)
sleep(500)
display.show(Image.HEART)
sleep(500)
display.show(Image.HEART_SMALL)
sleep(500)
display.scroll('ME')
sleep(500)

music.play(music.PRELUDE,wait=False)
for i in range(5):
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
display.show(Image.HEART)
sleep(500)

music.play(music.ENTERTAINER,wait=False)
display.show(Image.ARROW_W)

d = 200
i = 0
v = 1
while True:
    if pin_logo.is_touched():
        v = v ^ 1;
        display.show(Image.HAPPY)
        audio.play(Sound.GIGGLE)
        display.show(img[i])

    if button_a.is_pressed():
        display.show(img[i])
        sleep(500)
        display.scroll(msg[i], delay=d, wait=False)
        if v==1:
            music.play(song[i],wait=False)
        j = len(msg[i])
        sleep(j*d)

    if button_b.is_pressed():
        audio.play(snd[i], wait=False)
        i = (i+1) % n
        if i==0:
            music.set_tempo(bpm=200)
            music.play(little_light, wait=False)
            music.set_tempo(bpm=120)
        sleep(200)
        display.show(img[i])
    
    if accelerometer.is_gesture('shake'):
        audio.play(Sound.TWINKLE,wait=False)
        for k in range(40):
            r = random.randint(1,6)
            display.show(r, wait=False)
            sleep(50)
    