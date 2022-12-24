# источник видео на ютуб 
# https://youtu.be/uFzNc7D44HI
from watchdog.observers import Observer
import watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_modefied(self, event):
        for filename in os.listdir(folder_track):
            file = folder_track + "/" + filename
            new_path = folder_dest + "/" + filename
            os.rename(file, new_path)

folder_track = '/home/yuri4/1'
folder_dest = '/home/yuri4/2'
observe.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()