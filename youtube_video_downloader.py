from pytube import YouTube
link = input("Please Enter the link of Your Desired Youtube video: ")

link = YouTube(link)
video = link.streams.get_highest_resolution()
video.download()
print("Downloaded !!!")