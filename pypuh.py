import pytube
url=input("")
youtube = pytube.YouTube(url).streams.filter(res="360p").first().download()
print("indirme tamamlandı. izleyebilirsiniz")
