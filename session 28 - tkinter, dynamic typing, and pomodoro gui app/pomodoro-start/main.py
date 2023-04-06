from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="25:00")
    timer_title.config(text='timer')
    check_marks.config(text='')
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_title.config(text='Breaklong', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text='breakShort', fg=PINK)
    else:
        count_down(work_sec)
        timer_title.config(text='work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    # if count_sec == '00':
    #     count_sec = '00'
    # if count_sec>-1 and count_sec < 10:
    #     count_sec = f'0{count_sec}'
    #
    # if count_min == '00':
    #     count_min = '00'
    # if count_min>-1 and count_min < 10:
    #     count_min = f'0{count_min}'

    #alt
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('pomodoro')
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
timer_title = Label(text="timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(103, 111, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='25:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start_button = Button(text='start', font=FONT_NAME, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='reset', font=FONT_NAME, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text='', font=(FONT_NAME, 35), fg=GREEN)
check_marks.grid(column=1, row=3)


window.mainloop()
