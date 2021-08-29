import pafy

url = "https://www.youtube.com/watch?v=Ns4LCeeOFS4&t=320s"
video = pafy.new(url=url)
print(video.title)
print(video.rating)
print(video.viewcount)
print(video.author, video.length)
print(video.duration, video.likes, video.dislikes, video.description)
