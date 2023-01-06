from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK =      "#e2979c"
RED =       "#e7305b"
GREEN =     "#9bdeac"
YELLOW =    "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 20
TIMER_SETS = 0
timer = None



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global TIMER_SETS
    TIMER_SETS += 1

    if TIMER_SETS % 8 == 0:
        count_down(LONG_BREAK_MIN*5)
        pomodoro_title.config(text="LONG BREAK")
    elif TIMER_SETS % 2 == 0:
        count_down(SHORT_BREAK_MIN*2)
        pomodoro_title.config(text="BREAK")
    else:
        pomodoro_title.config(text="WORK")
        count_down(WORK_MIN*2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    global TIMER_SETS
    global timer
    # Configuring time to be displayed in minutos and seconds
    count_min = floor(time/60)
    count_sec = time % 60
    mark_checks = ""

    time_text = f"{count_min:02d}:{count_sec:02d}"
    if time > 0:
        canvas.itemconfig(timer_text, text = time_text)
        timer = window.after(1000, count_down, time - 1)
    else:
        mark = "✓ "
        start_timer()
        for _ in range(floor(TIMER_SETS / 2)):
            mark_checks = mark_checks + mark
        check_marks.config(text = mark_checks)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global TIMER_SETS
    TIMER_SETS = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = f"00:00")
    check_marks.config(text = "")


# ---------------------------- UI SETUP ------------------------------- #





# Main window
window = Tk()
window.title("Pomodoro Widget")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 138, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))

# Tomato position
canvas.grid(row=1, column=1)

# Title of pomodoro's timer
pomodoro_title = Label(text = "Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME, 30, "bold"))
pomodoro_title.grid(row=0, column=1)

##  General config for buttons
BUTTON_DEFAULT = {"font": (FONT_NAME, 15, "bold"), "padx":10, "pady":5, "highlightthickness":0}

# Start button (listening to the counting down command)
start_button = Button(text="Start", **BUTTON_DEFAULT, command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", **BUTTON_DEFAULT, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check marks
check_marks = Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"), pady=10)
check_marks.grid(row=3, column=1)

window.mainloop()