import watchdog.events
import watchdog.observers
import time
import shutil
import zipfile

download_folder = "D:\Downloads"


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(
            self,
            patterns=["*.zip"],
            ignore_directories=True,
            case_sensitive=False,
        )
        print("Watching Downloads folder...")

    def on_modified(self, event):
        print("Modified:", event.src_path)
        format = event.src_path.split(".")[-1]
        name = event.src_path.split("\\")[-1].split(".")[0]
        try:
            shutil.unpack_archive(
                event.src_path, download_folder + "\\" + name, format=format
            )
            print(f"Unpacked {event.src_path}")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    path = download_folder
    handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(
        handler,
        path,
        recursive=True,
    )
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
