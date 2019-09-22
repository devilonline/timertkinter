import tkinter as tk

class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        self.state = False
        self.minutes = 30
        self.seconds = 0

        self.mins = 25
        self.secs = 0

        self.display = tk.Label(master, height=10, width=10, textvariable="")
        self.display.config(text="30:00")
        self.display.grid(row=0, column=0, columnspan=2)

        self.start_button = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start", width=8, height=4, command=self.start)
        self.start_button.grid(row=1, column=0)

        self.pause_button = tk.Button(master, bg="Red", activebackground="Dark Red", text="Pause", width=8, height=4, command=self.pause)
        self.pause_button.grid(row=1, column=1)

    def countdown(self):


        if self.state == True:

            if (self.mins == 0) and (self.secs == 0):
                self.display.config(text="Done!")
                self.state = False
            else:
                self.display.config(text="%02d:%02d" % (self.mins, self.secs))

                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)

    def start(self):
        if not self.state:
            self.state = True
            self.mins = self.minutes
            self.secs = self.seconds
            self.countdown()

    def pause(self):
        if self.state:
            self.state = False





root = tk.Tk()
my_timer = Timer(root)

root.mainloop()
"{:02} : {:02}".format(10, 0)
