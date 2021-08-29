import os
import pafy


class Downloader:
    def __init__(self):
        self.limit = 20
        self.download_path = "C:/Adithya/fy-project/downloads"
        self.replaceable_chars = ['/', '|', ':']
        self.allowed_char_rgx = '[\\w\\s-!#.]'

    # noinspection PyMethodMayBeStatic
    def check_if_downloaded(self, title):
        print(title)
        filenames = os.listdir(self.download_path)
        if len(filenames) == 0:
            return False
        filenames = [os.path.splitext(s)[0] for s in filenames]
        for char in self.replaceable_chars:
            title = title.replace(char, "_")
        return title in filenames

    def download_from_url(self, url):
        video = pafy.new(url)
        if self.check_if_downloaded(video.title):
            print(f"\"{video.title}\" has already been downloaded!")
            folder_name = os.path.basename(self.download_path)
            print(f"Please check the \"{folder_name}\" folder\n")
        else:
            best = video.getbest()
            print("Downloading...")
            best.download(filepath="downloads/")
            print(f"\"{video.title}\" downloaded!\n")

    def download_from_url_file(self):
        f = open("urls.txt", "r")
        list_of_urls = f.read().split(sep='\n')
        print("downloaded videos' list:")
        print(list_of_urls)
        f.close()
        for url in list_of_urls:
            self.download_from_url(url=url)
        print(os.listdir(self.download_path))
