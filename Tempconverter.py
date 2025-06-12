#11/06/2025
#Temperature Converter
from tkinter import *
from tkinter import messagebox


class Converter:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Temperature Converter")
        self.root.rowconfigure(0,weight = 1)
        self.root.columnconfigure(0,weight = 1)
        self.container = Frame(self.root)
        self.container.grid(row=0,column=0,sticky="news")
        self.container.rowconfigure(0,weight=1)
        self.container.columnconfigure(0,weight=1)
        self.frames = {}
        self.frames["Main_Frame"] = self.create_main_frame()
        self.frames["temp_frame"] = self.create_temp_frame("temp_frame")
        self.frames["Main_Frame"].grid(row=0,column=0,sticky="news")

        self.show_frame("Main_Frame",None)



        pass
    def create_main_frame(self):
        frame = Frame(self.container)
        frame.rowconfigure([0],weight=1)
        frame.columnconfigure([0,1],weight=1)
        self.to_f_button = Button(frame,text="To Farenheit",bg="Yellow",font="Verdana 12 bold",command= lambda: self.show_frame("temp_frame","f"))
        self.to_c_button = Button(frame,text="To Centigrade",bg="Yellow",font="Verdana 12 bold",command= lambda: self.show_frame("temp_frame","c"))
        self.to_c_button.grid(row=0,column=0,sticky="news")
        self.to_f_button.grid(row=0,column=1,sticky="news")
    
        frame.grid()
        return frame
    
    def create_temp_frame(self,name):
        self.temp_type = None
        frame = Frame(self.container)
        frame.rowconfigure([0,1],weight=1)
        frame.columnconfigure([0,1],weight=1)
        self.display_text = StringVar()
        self.display_label = Label(frame,textvariable=self.display_text)
        self.display_label.grid(row = 0,column=1,sticky="news")
        self.input_field = Entry(frame)
        self.input_field.insert(0,0)
        self.input_field.grid(row=0,column=0,sticky="news")
        self.calculate_button = Button(frame,text="Calculate",bg="Yellow",font="Verdana 12 bold",command= lambda: self.calculate(float(self.input_field.get())))
        self.back_button = Button(frame,text="Back",bg="Yellow",font="Verdana 12 bold",command= lambda: self.show_frame("Main_Frame",None))
        self.calculate_button.grid(row=1,column=0,sticky="news")
        self.back_button.grid(row=1,column=1,sticky="news")

        frame.grid(row=0,column=0,sticky="news")
        self.input_field.bind("<FocusOut>", self.allow_numbers)
        self.root.bind_all("<Button-1>", lambda event: event.widget.focus_set())
        return frame
    def show_frame(self,name,temp_type):
        self.temp_type = temp_type
        for i in self.frames:
            if name != i:
                self.frames[i].grid_remove()
            else:
                self.frames[i].grid()
        self.input_field.delete(0,END)
        self.display_text.set(0)
    def calculate(self,val):
        temp = 0
        if self.temp_type == "f":
            temp = val *(9/5)+32
        elif self.temp_type == "c":
            temp = (val-32)*5/9
        self.display_text.set(round(temp,2))
        
    def allow_numbers(self):
        #Prevents error message from calling if window is minimised
        if self.root.focus_get() is None:
            return
        val = self.input_field.get()
        try:
            val = float(val)
        except ValueError:
            messagebox.showerror("Invalid Input","Value must be a number")
            self.root.after(0,lambda: self.input_field.focus_set())
            pass
convert = Converter()
convert.root.mainloop()