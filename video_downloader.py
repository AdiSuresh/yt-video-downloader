import os
import pafy


class Downloader:
    # noinspection PyMethodMayBeStatic
    def check_if_downloaded(self, title):
        filenames = os.listdir("C:/Adithya/fy-project/downloads")
        return title in filenames

    def download_from_url(self, url):
        video = pafy.new(url)
        print(os.listdir("C:/Adithya/fy-project/downloads"))
        print(type(os.listdir("C:/Adithya/fy-project/downloads")))
        if self.check_if_downloaded(url):
            print(f"\"{video.title}\" has already been downloaded!")
            print("Please check the \"downloads\" folder")
            print(f"{video.title}")
        else:
            best = video.getbest()
            best.download(filepath="downloads/")
            print(f"\"{video.title}\" downloaded!")

    def download_from_url_file(self):
        f = open("urls.txt", "r")
        list_of_urls = f.read().split(sep='\n')
        print("downloaded videos' list:")
        print(list_of_urls)
        f.close()
        for url in list_of_urls:
            self.download_from_url(url=url)
