import ctypes
import os

class MusicPlayer:
    def __init__(self):
        self.state = {"path": "", "playing": False}

    def mci(self, cmd):
        try:
            res = ctypes.create_unicode_buffer(128)
            ctypes.windll.winmm.mciSendStringW(cmd, res, 128, None)
            return res.value
        except Exception as e:
            print(f"MCI Hatası: {e}")
            return ""

    def play(self, dosya_yolu):
        try:
            self.state["path"] = os.path.abspath(dosya_yolu)
            self.mci('close sarki')
            self.mci(f'open "{self.state["path"]}" alias sarki')
            self.mci('play sarki')
            self.state["playing"] = True
        except Exception as e:
            print(f"Oynatma hatası: {e}")
