from pytube import YouTube
import os

# input of video details
link = input("\nplease paste your link:\n")
print("_______________________________________________________________________")
dirt= input("\nenter a valid title:\n")
print("_______________________________________________________________________")

root= "C:\\Users\\hunak\\Desktop\\"
path= os.path.join(root,dirt)
clear_link = link.strip("https://")

#https://www.youtube.com/watch?v=xSrLIoF_dnU
print("\nSearching.........\n")
yt_term = YouTube(clear_link)
typ = input("\nenter the format video | audio |  Check both: \n")
print("_______________________________________________________________________")

if typ == "video":
    resl = input("\nplease enter resolution 1080 | 720 | 480 | 360: \n")
    print("_______________________________________________________________________")
    results = yt_term.streams.filter(mime_type=typ+"/mp4",res= resl+"p", type=typ )
elif typ == "audio":
    results = yt_term.streams.filter(type=typ)
else:
    results = yt_term.streams


j=1
for i in results:
    print("\nSerial No.: {} \n {}\n".format(j,i))
    j+=1
    
print("_______________________________________________________________________")
selection = int(input("\nenter the serial no. : \n"))
video = results[selection - 1]
print("_______________________________________________________________________")


try:
    print("\nvideo downloading....\n")
    os.mkdir(path)
    print(dirt," directry created.....\n")
    video.download(path)
    print("download complete!")
except:
    print("path already exists or invalid path!!\n")

