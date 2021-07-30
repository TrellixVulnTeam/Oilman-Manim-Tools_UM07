import threading
from tkinter import *
from tkinter import ttk


class progress():
    def __init__(self, parent):
        toplevel = Toplevel(tk)
        self.progressbar = ttk.Progressbar(toplevel, orient=HORIZONTAL, mode='indeterminate')
        self.progressbar.pack()
        self.t = threading.Thread()
        self.t.__init__(target=self.progressbar.start, args=())
        self.t.start()
        # if self.t.isAlive() == True:
        #       print 'worked'

    def end(self):
        if not self.t.is_alive():
            self.progressbar.stop()
            self.t.join()


def printmsg():
    print('proof a new thread is running')


tk = Tk()
new = progress(tk)
but1 = ttk.Button(tk, text='stop', command=new.end)
but2 = ttk.Button(tk, text='test', command=printmsg)
but1.pack()
but2.pack()
tk.mainloop()
