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

# function to play sound everytime the user haft to take a break
def play():
    '''function that play the sound on the 1.mp3 file'''
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=0)



#function to reset the time
def reset():
    '''when click on reset button will reset the label the time and the reps'''
    # after_cancel from tkinter cancel the time, in this case timer is a global var
    window.after_cancel(timer)
    # congfig the label to Timer again , starting point
    label.config(text="Timer")
    # set the time to 00:00 
    canvas.itemconfig( time, text="00:00")
    # reset also the check mark ✅
    check_marks.config(text="")
    # reset the count repetition to zero
    global reps
    reps = 0

    

def start(): 
    '''when press start the program start to work. 
    The function get called also by the function count_down and each time reps will increase +1
    The function (start) keep track of the breaks and the time of work'''
    #every time start will be called , increase reps by 1
    global reps
    reps += 1
    # get the second of the working time 55
    sec = WORK_MIN * 60
    # get the second of the short break 5
    short_break_sec = SHORT_BREAK_MIN * 60
    # get the second of the long break 20
    long_break_sec = LONG_BREAK_MIN * 60
    
    # 8 becuase after 4 times of short breaks of 5 min and 4  times 55 min of work, start the long break of 20 min 
    if reps % 8 == 0:
        play()
        #in case user hide the window, when will be the break the window will show up again 
        window.after(0,window.deiconify())
        # call the function count_down with the long break 
        count_down(long_break_sec)
        # change the label from Work to Break
        label .config(text = "Break", fg= RED)
    # every 2 reps 1 of 55 min work then 5 min break , so every 2 reps 1 break     
    elif reps % 2 == 0:
        play()
        # in case user hide the widow when will be the break the  window will show up again 
        window.after(0,window.deiconify())
        # call the function count_down with the short break
        count_down(short_break_sec)
        # change the label from Work to Break
        label .config(text = "Break", fg = PINK)
    else:
        # else count down from the working time
        count_down(sec)
        # set label to Work
        label .config(text = "Work", fg= GREEN)
         


# function to count down the time
def count_down(count):
    '''Shows the time on work  ( count down ) and each time that time get to zero will call the function start
    that shows the breaks time , the function count_down will add a marks each time that will have a break'''
    
    #ex 5*60 = 300 seconds so to get the minutes we need to divide 300/60 but to get the right minutes when the second are for 238 then we need to round to the min bigger number that is 3 
    minute = math.floor(count / 60)
    #count how many seconds is left using the rest % ,  if 240 sec then will be 240 % 60  = 0 if 241 % 60 then we have 4 min and 1 second 
    second = math.floor(count % 60)
    
    #to show the minutes and the seconds in a correct format
    if second < 10:
        # format the int to a string
        second = f"0{second}"
    if minute < 10:
        # inside the canvas time form tkinter we add the min and second formated as a string
        canvas.itemconfig(time, text=f"0{minute}:{second}")
    else:
        # inside the canvas time form tkinter we add the min and second formated as a string
        canvas.itemconfig(time, text=f"{minute}:{second}")
    if count > 0:
        # if count is > 0 the timer will change every 1 second and every time will call the function count_down() , the values that get the function will be -1 , in this way we count down the time
        global timer
        timer = window.after(1000, count_down, count -1)

    else:
        # if count is 0 then we call the function start , to start again and we add a ✔ to the label check_marks
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

# create the label to add ✔
check_marks = tkinter.Label( fg = GREEN, bg = YELLOW, highlightthickness=0, font= ("bold"))
check_marks.grid(row=3, column = 1)



#Keep the window open 
window.mainloop()


