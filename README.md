<h1 align="center">TIME MANAGEMENT</h1>

#### Description 🏁

I use the Pomodoro technique to build a time management tool to break the work in small intervals of 55 minutes.

The Pomodoro Technique is a TIME MANAGEMENT method developed by Francesco Cirillo in the late 1980s. It uses a kitchen timer to break work into intervals, typically 25 minutes in length (in this toll we changed for 55 minutes), separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato.

**_@wikipedia https://en.wikipedia.org/wiki/Pomodoro_Technique_**

**_Library tkinter tk:  https://docs.python.org/3/library/tk.html_** 

**_Mp3:  https://pixabay.com/_**  🔸 play a sound each time the user should take 5 min break

**_Img: tomato.png_** 🔸 used inside the tkinter window



## main.py required

To work with the main function it's important to import some library and install pygame to play the mp3 sound

pip install pygame 

import tkinter

import math

import pygame




## main.py 

The main.py has 4 functions :

_play()_

_reset()_

_start()_

_count_down()_


In the file main.py I build a GUI using tkinter library and I use 4 function to interact with GUI.

I used grid layout for the label, buttons and img.


### play()

It is used to play the mp3 sound

```
pygame.mixer.init()

def play():
    '''function that play the sound on the 1.mp3 file'''
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=0)
```

### reset()

I used the function  reset the label , the time and the reps , so the time will be 00:00 , the label "Timer" and reps again to zero (reps is global var used to count the breaks , each 2 times 1 break)

### start()

Each time start will be called , the time of work will start to count_down() and with an if else statement and the reps var , the function check when to be on break and how many breaks the user took it .
if the user should take a break the play function will play the mp3 sound and the label will change status from "Work" to "Break".


### count_down()

Shows the time of work  ( count down ) and each time that time get to zero the function will call the function start()
The function count_down will add a marks ✅ each time that will have a break

**To get and show to the user the correct time we use floor from the math library:**

**ex 5*60 = 300 seconds so to get the minutes we need to divide 300/60  so in this case is fine 5 but we if we in our countdown  230 seconds so then  how many minutes** **do we have ? so the answer is :**

**230/60 = 3.8  so to have the correct minutes we used floor to round to the min bigger number 3.**


**For the second we use % to get know how many seconds remain**

**ex 230 % 60 = 50 seconds**

_So the function count_down() take as arguments count and each 1 second we count -1 like this we keep counting the minutes and the second and we display to the user_ _the correct time and when the time get to zero will call the function  start()_

```
if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1) 
```

Timer is a global variable used in the function reset to reset the time

The function count_down() will interact with the label check mark and each 2 times get to zero then the start() function will be called and willadd a check mark to the label check_marks

## Usage
GUI

<p align="center">
<img width="348" alt="image" src="https://user-images.githubusercontent.com/110894389/220589451-d0ad5ba3-d964-408c-b4fd-17171bceccd8.png">
</p>



