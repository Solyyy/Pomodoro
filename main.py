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
    start_button.config(state="normal")
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    timer_header.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_header.config(text="Break", fg=RED, bg=YELLOW)
    # If it's the 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_header.config(text="Break", fg=PINK, bg=YELLOW)
    # If it's the 1st/3rd/5th/7th rep
    else:
        count_down(work_sec)
        timer_header.config(text="Work", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_txt, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Timer text
timer_header = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_header.grid(row=0, column=1)

# Start and Reset Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0, bg=GREEN)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, bg=GREEN)
reset_button.grid(column=2, row=2)

# Checkmarks label
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmarks.grid(column=1, row=3)

window.mainloop()
