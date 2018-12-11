from __future__ import unicode_literals
import youtube_dl
import threading
stat=''

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    global stat
    if d['status'] == 'finished':
        stat='[Console]Done downloading, now converting ...'

ydl_opts_mp3 = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

ydl_opts_mp4 = {
    'format': 'bestvideo/best',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def downloadas(tp,url):
    if tp=='mp3':
        with youtube_dl.YoutubeDL(ydl_opts_mp3) as ydl:
            ydl.download([url])
            print("[Console]Downloading as mp3...")
    elif tp=='mp4':
        with youtube_dl.YoutubeDL(ydl_opts_mp4) as ydl:
            ydl.download([url])
            print("[Console]Downloading as mp4...")
    else:
        return "[Console]Invalid argument"
    
    return "[Console]Done."
	
def dl(a,b):
  print('thread starts')
  t = threading.Thread(target = downloadas,args = (a,b,))
  t.start()
  t.join()
