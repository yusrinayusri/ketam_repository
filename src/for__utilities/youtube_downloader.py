import tkinter as tk
import customtkinter
from pytube import YouTube
from PIL import Image

#https://www.youtube.com/watch?v=-lyGaojvmB0

#function to download the youtube video
def start_download():
    try:
        youtube_link = yt_link.get()
        youtube_object = YouTube(youtube_link, on_progress_callback=on_progress)
        youtube_video = youtube_object.streams.get_highest_resolution()
        youtube_object.streams()

        title_app.configure(text=youtube_object.title, text_color="white")
        finished_label.configure(text="")

        youtube_video.download()
        finished_label.configure(text="Download Complete!", text_color="green")
    except Exception as e:
        print("Error: ", e)
        finished_label.configure(text="Download Failed!", text_color="red")
    print("Tasks Complete.") #CLI print

#function to calculate download progress
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    perc = str(int(percentage_of_completion))
    pPercentage.configure(text=perc + '%')
    pPercentage.update()

    #update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("500x500")
app.title("Python YouTube Downloader")

#app Image
img = "src/for__utilities/2621053.png"
my_image = customtkinter.CTkImage(light_image=Image.open(img), size=(100,100))
image_label = customtkinter.CTkLabel(app, image=my_image, text="")
image_label.grid(row=0, column=0, padx=100, pady=30)

#adding UI elements
#app title
title_app = customtkinter.CTkLabel(app, text="Insert a youtube link", font=('Arial', 16))
title_app.grid(row=1, column=0, padx=100, pady=5)

#input link
url_var = tk.StringVar()
yt_link = customtkinter.CTkEntry(app, width=300, height=5, textvariable=url_var)
yt_link.grid(row=3, column=0, padx=100, pady=5)

#finished download label
finished_label = customtkinter.CTkLabel(app, text="")
finished_label.grid(row=4, column=0, padx=100, pady=5)

#download progress bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.grid(row=5, column=0, padx=100, pady=5)

progressBar = customtkinter.CTkProgressBar(app, width=300)
progressBar.set(0)
progressBar.grid(row=6, column=0, padx=100, pady=5)

#download button
vid_download = customtkinter.CTkButton(app, text="Download", command=start_download)
vid_download.grid(row=7, column=0, padx=100, pady=5)

#run app
app.mainloop()
