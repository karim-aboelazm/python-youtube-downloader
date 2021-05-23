class Youtube_Downloader(object):
    def one_video(self):
        from pytube import YouTube
        url = input("Enter Video URL : ")
        video = YouTube(url)
        download = video.streams.get_highest_resolution()
        print("Downloading...")
        print("Title : ",video.title)
        download.download(output_path='E:\PythonProjects\youtube-downloader\YTDownloader')
        print("Download Completed !!")
    def more_videos(self):
        from pytube import Playlist
        playlist_link = input("Enter Playlist URL : ")
        Playlist = Playlist(playlist_link)
        i = 0
        for video in Playlist.videos:
            video.streams.get_highest_resolution().download(output_path='E:\PythonProjects\youtube-downloader\YTDownloader')
            video.register_on_complete_callback(lambda: print(end=''))
            i += 1
            print("Video number : ", i)
if __name__ == '__main__':
    while True:
        def start():
            print("Which you wanna Download..\n1) One Video.\n2) PlayList.\n3) Quit.")
            x = int(input("Choose One Of Choice : "))
            if x==1:
                Youtube_Downloader().one_video()
            elif x==2:
                Youtube_Downloader().more_videos()
            elif x==3:
                quit()
            else:
                print("Make Sure Your Choice Please")
                print("-"*29)
                start()
        start()