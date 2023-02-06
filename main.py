import tkinter 
import math
import pygame # type: ignore


#  Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 55
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#global variables
reps = 0
timer = None

#initialization  pygame
pygame.mixer.init()

def play():
    '''function that play the sound on the 1.mp3 file'''
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=0)




def reset():
    '''when click on reset button will reset the label the time and the reps'''
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig( time, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

    

def start(): 
    '''when press start the program start to work. 
    The function get called also by the function count_down and each time reps will increase +1
    The function (start) keep track of the breaks and the time of work'''
    global reps

    reps += 1
    sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        play()
        #in case user hide the widow when will be the break the  window will show up again 
        window.after(0,window.deiconify())
        count_down(long_break_sec)
        label .config(text = "Break", fg= RED)
    elif reps % 2 == 0:
        play()
        #in case user hide the widow when will be the break the  window will show up again 
        window.after(0,window.deiconify())
        count_down(short_break_sec)
        label .config(text = "Break", fg = PINK)
    else:
        count_down(sec)   
        label .config(text = "Work", fg= GREEN)
         



def count_down(count):
    '''Shows the time on work  ( count down ) and each time that time get to zero will call the function start
    that shows the breaks time , the function count_down will add a marks each time that will have a break'''
    #ex 5*60 = 300 seconds so to get the minutes we need to divide 300/60 but to get the right minutes when the second are for 240 then we need to round to the min bigger number 
    minute = math.floor(count / 60)
    #count how many seconds is left
    second = math.floor(count % 60)
    
    #to show the minutes and the seconds in a correct format
    if second < 10:
        second = f"0{second}"
    if minute < 10:
        canvas.itemconfig(time, text=f"0{minute}:{second}")
    else:
        canvas.itemconfig(time, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)

    else:
        start()
        session = math.floor(reps/ 2)
        marks = "".join("✔" for _ in range(session))
        check_marks.config(text = marks)
        



#Creating the window GUI
window  = tkinter.Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

# Canvas add img to the window
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_ing =  tkinter.PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image=tomato_ing)
time  = canvas.create_text(100, 130, text = "00:00", fill="white", font = (FONT_NAME, 28, "bold") )
canvas.grid(row= 1, column = 1)



#Creating the label ""TIMER" 
label = tkinter.Label(text= "TIMER", fg= GREEN, font = (FONT_NAME, 35, "bold"), bg = YELLOW)
label.grid(row= 0, column = 1)

#Create the button start down on the left side
button_start = tkinter.Button(text = "Start", highlightthickness=0, command=start)
button_start.grid(row = 2, column = 0)

#Create the button reset down on the right side
button_reset = tkinter.Button(text = "Reset", highlightthickness=0, command=reset)
button_reset.grid(row = 2, column = 2)


check_marks = tkinter.Label( fg = GREEN, bg = YELLOW, highlightthickness=0, font= ("bold"))
check_marks.grid(row=3, column = 1)



#Keep the window open 
window.mainloop()


