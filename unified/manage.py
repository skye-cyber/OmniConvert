from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
import time


class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".kv") or event.src_path.endswith(".py"):
            print(
                f"\033[35mFile \033[0;1m{event.src_path}\033[33m changed, reloading...\033[0m"
            )
            os.execv(sys.executable, ["python"] + sys.argv)


print("\033[1;94mWatchdog Running..\033[0m")


observer = Observer()
event_handler = ReloadHandler()
observer.schedule(event_handler, path=".", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
