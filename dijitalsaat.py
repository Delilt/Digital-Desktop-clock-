from tkinter import Label,Tk as tk
import time


app_windows = tk()
app_windows.title("dijital masautu saati")
app_windows.geometry("280x170")
app_windows.resizable(0,0)
app_windows.config(bg="gray4")

text_font = ("boulder",24,'bold')
background = "gray4"
forground = "white"
border_width = 10


#saat etiketi
label = Label(app_windows,font=text_font, bg=background,fg=forground)
label.grid(row = 0 ,column = 1, padx = border_width , pady = border_width)

#tarih etiketi
date_label = Label(app_windows,font=text_font,bg=background,fg=forground)
date_label.grid(row = 1 ,column = 1, padx = border_width , pady = border_width)


def dijital_saat():
    #saat alani
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    #tarih alani
    date_live = time.strftime("%d %B %Y")
    date_label.config(text=date_live)
    label.after(1,dijital_saat)

dijital_saat()

app_windows.mainloop()