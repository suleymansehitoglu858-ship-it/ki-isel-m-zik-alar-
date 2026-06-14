import ctypes
from mutagen.mp3 import MP3

class MusicPlayer:
    def __init__(self):
        self.state = {"path": "", "index": 0, "length": 0}

    def mci(self, cmd):
        try:
            res = ctypes.create_unicode_buffer(128)
            ctypes.windll.winmm.mciSendStringW(cmd, res, 128, None)
            return res.value
        except Exception:
            return ""

    def get_duration(self, path):
        try:
            audio = MP3(path)
            return int(audio.info.length * 1000)
        except:
            return 0
