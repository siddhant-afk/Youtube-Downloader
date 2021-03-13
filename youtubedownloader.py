from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


#--------------------------------------------------Back End---------------------------------------------------

folderName=""

def openLocation():
    global folderName
    folderName=filedialog.askdirectory()
    if(len(folderName)>1):
        locationError.config(text=folderName,fg="green")
    else:
        locationError.config(text="Please choose a file location",fg="red")  

def downloadVideo():
    quality=qualityChoices.get()
    url=urlEntry.get()

    if len(url)>1:
        urlError.config(text="")
        youtube=YouTube(url)

        if quality==choices[0]:
            select = youtube.streams.filter(progressive=True).first()
        elif quality==choices[1]:
            select = youtube.streams.filter(progressive=True,file_extension='mp4').last()    
        elif quality==choices[2]:
            select = youtube.streams.filter(only_audio=True).first()  
        else:
            urlError.config(text="Paste the link again",fg="red")  


    select.download(folderName) 
    urlError.config(text="Download Completed!",fg="green") 



#-------------------------------x-------Back End----------------------------x--------------------------
#--------------------------------------Front End------------------------------------------------------------------
root=Tk()
root.title("Youtube Downloader")
root.geometry("350x400")
root.columnconfigure(0,weight=1)

#------------------------Youtube Downloader link labels--------------------
youtubeLabel =Label(root,text="Enter the URL of the video",font=("monospace",15))
youtubeLabel.grid()


#----------------------Text Box---------------------------------------------
urlTextBox = StringVar()
urlEntry= Entry(root,width=50,textvariable=urlTextBox)
urlEntry.grid()


#-------------------------Error Message---------------------

urlError= Label(root,text="Invalid url",font=("monospace",10),fg="red")
urlError.grid()

#------------------Inquiry for File Location-----------------------------
LocationLabel=Label(root,text="Select download location",font=("monospace",15))
LocationLabel.grid()
choosePath=Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
choosePath.grid()

#-----------------------Location Error Message-----------------------------
locationError=Label(root,text="Invalid Path",font=("monospace",10),fg="red")
locationError.grid()

#----------------------Combo Box---------------------------------------
choices=["720p","144p","Audio Only"]
qualityChoices=ttk.Combobox(root,values=choices)
qualityChoices.grid()

#-------------------------Download Button--------------------------------
downloadButton= Button(root,text="Download",bg="red",fg="white",width=10,command=downloadVideo)
downloadButton.grid()


root.mainloop()
#----------------------x--------------------Front End-------------------------------x-------------------------------
