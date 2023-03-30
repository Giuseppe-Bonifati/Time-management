# TIME MANAGEMENT :alarm_clock:

<a href="https://twitter.com/giuseppewdev"> <img src = "https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fgiuseppewdev"> </a> <a href="https://dev.to/giuseppewdev"><img src="https://img.shields.io/badge/-DEV-black?logo=dev.to"></a>

#### Description 

I use the Pomodoro technique to build a time management tool to break the work in small intervals of 55 minutes.

The Pomodoro Technique is a TIME MANAGEMENT method developed by Francesco Cirillo in the late 1980s. It uses a kitchen timer to break work into intervals, typically 25 minutes in length (in this toll we changed for 55 minutes), separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato.

<a href="https://en.wikipedia.org/wiki/Pomodoro_Technique"><img src="https://img.shields.io/badge/-Wikipedia-grey?logo=wikipedia"></a>  


## Installation :package: 

<a href=https://www.python.org/ ><img src="https://img.shields.io/badge/-Python-white?logo=python"></a>  <a href="https://code.visualstudio.com/"> <img src="https://img.shields.io/badge/-Visual%20Studio%20Code-0098ff?logo=visualstudiocode" ></a>  <a href="https://pixabay.com/"><img src="https://img.shields.io/badge/-Pixabay-white?logo=pixabay"></a> <a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/-Tkinter-white?logo=python"></a>

##### Mp3 Sound Pygame :sound:

I downloaded the Mp3 from pixabay and then to play it I installed pygame:

```sql
pip install pygame
```
Pygame plays the mp3  sound each time the user should take 5 minutes breaks

##### Import

Then in the file main.py import the following:

```python
import tkinter
import math
import pygame
```

##### Imagine :tomato:

tomato.png is the img used inside the tkinter window



## Design

To Build this tool i use Tkinter with 4 different functions:

### Functions

#### play

Used to play the mp3 sound

```python
pygame.mixer.init()

def play():
    '''function that play the sound on the 1.mp3 file'''
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=0)
```

#### reset

I use the function to reset the label , the time and the reps (reps is global var used to count the breaks , each 2 times 1 break).

#### start

Each time start will be called , the time of work/break will start to count_down(), the function check when to be on break and how many breaks the user took it.
Everytimes the user haft to take a break, the function play() will play the mp3 sound and the label will change status from "Work" to "Break".


#### count_down

Shows the time of work and when the time get to zero the function will call the function start()
The function count_down will add a marks ✅ each time that will have a break

:bangbang: Important

To get and to show to the user the correct time, we use floor from the math library:

```python
import math
```
Example how to use floor from the math library:

```python
min = math.floor(230 / 60) # result 3 min
sec = math.floor(230 % 60) # result 50 sec
```

<img width="474" alt="image" src="https://user-images.githubusercontent.com/110894389/225368371-54dabf5f-8c32-4152-bc92-323e8b34322f.png">


So the function count_down() take as arguments count(seconds) and each 1 second we count -1, like this we keep counting down and we display to the user the correct time, once the time get to zero will call the function start()

```python
if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1) 

#Timer is a global variable used also in the function reset() to reset the time
        
```


The function count_down() will interact with the label check mark, and each 2 times that count get to zero, then the start() function will be called and will add a check mark to the label check_marks.


## GUI


<p align="center">
<img width="348" alt="image" src="https://user-images.githubusercontent.com/110894389/220589451-d0ad5ba3-d964-408c-b4fd-17171bceccd8.png">
</p>



## License

<a href="https://github.com/Giuseppe-Bonifati/Time-management/blob/main/LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue"></a>
