from sys import exception
import sys
import tkinter
import password
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import customtkinter as CTk
from  PIL import Image


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Password generator")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("img.png"), size=(460, 150))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate", width=100,
                                          command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_lenght_slider = CTk.CTkSlider(master = self.settings_frame, from_= 0, to = 100, number_of_steps=100,
                                                     command=self.slider_event) 
        self.password_lenght_slider.grid(row=1, column=0, columnspan = 3, pady=(20, 20), sticky="ew")

        self.password_lenght_enrty = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_lenght_enrty.grid(row=1, column=3, padx=(20, 10), sticky="we")
         
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master = self.settings_frame, text="0-9", variable=self.cb_digits_var,
                                         onvalue=digits, offvalue="").grid(row = 2, column = 0)
        
        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master = self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                         onvalue=ascii_lowercase, offvalue="").grid(row = 2, column = 1)
        
        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master = self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                         onvalue=ascii_uppercase, offvalue="").grid(row = 2, column = 2)
        
        self.cb_symbols_var = tkinter.StringVar()
        self.cb_symbols = CTk.CTkCheckBox(master = self.settings_frame, text="@#$%*", variable=self.cb_symbols_var,
                                         onvalue=punctuation, offvalue="").grid(row = 2, column = 3)
        
        self.appereance_mode_options_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                              values=["Dark","Light","green","System"],
                                                              command =self.appereance_mode_option_event).grid(row = 3, column = 0, columnspan = 4, pady = (10,10))
        self.password_lenght_slider.set(12)
        self.password_lenght_enrty.insert(0, 12)

    def appereance_mode_option_event(self, new_appereance_mode):
        CTk.set_appearance_mode(new_appereance_mode)
        
    def slider_event(self,value):
        self.password_lenght_enrty.delete(0,"end")
        self.password_lenght_enrty.insert(0, int(value))

    def get_chracters(self):
        try:
            chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + 
                        self.cb_symbols_var.get())
            return chars
        except:
            pass

    def set_password(self):
        self.entry_password.delete(0,"end")
        try:
            self.entry_password.insert(0, password.create_new_password(lenght=int(self.password_lenght_slider.get()),
                                                                   characters=self.get_chracters()))

        except:
            print(exception())
            pass

if __name__=="__main__":
    app = App()
    app.mainloop()