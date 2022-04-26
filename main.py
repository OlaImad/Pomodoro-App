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
check_mark1 = "✔"
check_mark2 = "✔ ✔"
check_mark3 = "✔ ✔ ✔"
check_mark4 = "✔ ✔ ✔ ✔"
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")







# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # count = 0
    # if reps % 2 != 0:
    #     count = work_sec
    # elif reps % 2 == 0 and reps != 8:
    #     count = short_break_sec
    # elif reps == 8:
    #     count = long_break_sec
    # count_down(count)
    # OR ANOTHER WAY
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()

        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Create Buttons
start_button = Button(text="Start",bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

# Create Label Timer

timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)








window.mainloop()
