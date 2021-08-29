import os
import pafy


class VideoDownloader:
    def __init__(self):
        # self.limit = 20
        self.download_path = "C:/Adithya/fy-project/downloads"
        self.download_size = -1

    def callback(self, total, received, ratio, rate, eta):
        if self.download_size == -1:
            self.download_size = total
            print("Downloading...")
        if total == received:
            print("Finished downloading.")

    def download_from_url(self, url):
        video = pafy.new(url)
        best = video.getbest()
        print(f"Preparing to download...")
        try:
            best.download(filepath="downloads/", callback=self.callback)
        finally:
            pass
        if self.download_size == -1:
            print(f"\"{video.title}\" has already been downloaded!")
            f_name = os.path.basename(self.download_path)
            print(f"Please check the \"{f_name}\" folder\n")
        else:
            print(f"\"{video.title}\" was downloaded successfully!\n")
        self.download_size = -1

    def download_from_url_file(self):
        f = open("urls.txt", "r")
        urls = f.read().split(sep='\n')
        f.close()
        for url in urls:
            self.download_from_url(url=url)


class AudioDownloader:
    def __init__(self):
        # self.limit = 20
        self.download_path = "C:/Adithya/fy-project/downloads"
        self.download_size = -1

    def callback(self, total, received, ratio, rate, eta):
        if self.download_size == -1:
            self.download_size = total
            print("Downloading...")
        if total == received:
            print("Finished downloading.")

    def download_from_url(self, url):
        video = pafy.new(url)
        best = video.getbest()
        print(f"Preparing to download...")
        best.download(filepath="downloads/", callback=self.callback)
        if self.download_size == -1:
            print(f"\"{video.title}\" has already been downloaded!")
            f_name = os.path.basename(self.download_path)
            print(f"Please check the \"{f_name}\" folder\n")
        else:
            print(f"\"{video.title}\" was downloaded successfully!\n")
        self.download_size = -1

    def download_from_url_file(self):
        f = open("urls.txt", "r")
        urls = f.read().split(sep='\n')
        f.close()
        for url in urls:
            self.download_from_url(url=url)
