from tkinter import *
import time
from tkinter import messagebox

clk = Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0")
clk.config(bg="#0C1E28")

def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    
    if int(hr) > 12 and int(mn) > 0:
        lb_dn.config(text="PM")
    if int(hr) > 12:
        hr = str(int(int(hr) - 12))
    
    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)

    check_alarm(hr, mn)  # Check the alarm

    lb_hr.after(200, clock)

def check_alarm(current_hr, current_mn):
    alarm_hr = alarm_hour.get()
    alarm_mn = alarm_minute.get()

    if current_hr == alarm_hr and current_mn == alarm_mn:
        messagebox.showinfo("Alarm", "It's time to wake up!")

def start_timer():
    timer_minutes = int(timer_minute.get())
    timer_seconds = int(timer_second.get())
    total_seconds = timer_minutes * 60 + timer_seconds
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        clk.update()
        time.sleep(1)
        total_seconds -= 1
    messagebox.showinfo("Timer", "Time's up!")

alarm_hour = StringVar()
alarm_minute = StringVar()
timer_minute = StringVar()
timer_second = StringVar()

alarm_label = Label(clk, text="Set Alarm (HH:MM):", font=("Times 20 bold", 20, "bold"), bg="#0C1E28", fg="white")
alarm_label.place(x=350, y=500, width=250, height=50)

alarm_entry = Entry(clk, textvariable=alarm_hour, bg="black", fg="white", font=("Helvetica", 14))
alarm_entry.place(x=600, y=500, width=50, height=50)

colon_label = Label(clk, text=":", font=("Times 20 bold", 20, "bold"), bg="#0C1E28", fg="white")
colon_label.place(x=655, y=500, width=20, height=50)

alarm_entry2 = Entry(clk, textvariable=alarm_minute, bg="black", fg="white", font=("Helvetica", 14))
alarm_entry2.place(x=675, y=500, width=50, height=50)

# Timer
timer_label = Label(clk, text="00:00", font=("Times 20 bold", 24), bg="#0C1E28", fg="white")
timer_label.place(x=350, y=580, width=100, height=40)

timer_label_text = Label(clk, text="Set Timer (MM:SS):", font=("Times 20 bold", 20, "bold"), bg="#0C1E28", fg="white")
timer_label_text.place(x=470, y=580, width=250, height=50)

timer_minute_entry = Entry(clk, textvariable=timer_minute, bg="black", fg="white", font=("Helvetica", 14))
timer_minute_entry.place(x=720, y=580, width=50, height=50)

colon_label2 = Label(clk, text=":", font=("Times 20 bold", 20, "bold"), bg="#0C1E28", fg="white")
colon_label2.place(x=775, y=580, width=20, height=50)

timer_second_entry = Entry(clk, textvariable=timer_second, bg="black", fg="white", font=("Helvetica", 14))
timer_second_entry.place(x=795, y=580, width=50, height=50)

start_timer_button = Button(clk, text="Start Timer", command=start_timer, font=("Helvetica", 14))
start_timer_button.place(x=870, y=580, width=100, height=40)

lb_hr = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#087587", fg="white")
lb_hr.place(x=350, y=200, width=150, height=150)

lb_hr_txt = Label(clk, text="HOUR", font=("Times 20 bold", 20, "bold"), bg="#087587", fg="white")
lb_hr_txt.place(x=350, y=360, width=150, height=50)

lb_mn = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#008EA4", fg="white")
lb_mn.place(x=520, y=200, width=150, height=150)

lb_mn_txt = Label(clk, text="MINUTE", font=("Times 20 bold", 20, "bold"), bg="#008EA4", fg="white")
lb_mn_txt.place(x=520, y=360, width=150, height=50)

lb_sc = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#06B4B8", fg="white")
lb_sc.place(x=690, y=200, width=150, height=150)

lb_sc_txt = Label(clk, text="SECONDS", font=("Times 20 bold", 20, "bold"), bg="#06B4B8", fg="white")
lb_sc_txt.place(x=690, y=360, width=150, height=50)

lb_dn = Label(clk, text="AM", font=("Times 20 bold", 70, 'bold'), bg="#9F0646", fg="white")
lb_dn.place(x=860, y=200, width=150, height=150)

lb_dn_txt = Label(clk, text="NOON", font=("Times 20 bold", 20, "bold"), bg="#9F0646", fg="white")
lb_dn_txt.place(x=860, y=360, width=150, height=50)

clock()
clk.mainloop()
