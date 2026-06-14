from mutagen.mp3 import MP3
import flet as ft
import ctypes
import os
import threading
import time

def main(page: ft.Page):
    page.title = "S-Player | Final"
    page.theme_mode = "dark"
    page.bgcolor = "#121212"
    page.window_width = 400
    page.window_height = 800

    state = {
        "path": "",
        "index": 0,
        "length": 0
    }

    zaman_yazisi = ft.Text("00:00 / 00:00", size=14, color="gray")

    def get_mci_data(cmd):
        res = ctypes.create_unicode_buffer(128)
        ctypes.windll.winmm.mciSendStringW(cmd, res, 128, None)
        return res.value

    def format_zaman(ms):
        if not ms or not ms.isdigit():
            return "00:00"

        s = int(ms) // 1000
        dakika = s // 60
        saniye = s % 60
        return f"{dakika:02d}:{saniye:02d}"

    def ses_takip():
        while True:
            if state["path"]:
                try:
                    pos = get_mci_data("status sarki position")
                    length = str(state["length"])
                    print("POS:", pos, "LEN:", state["length"])

                    if pos.isdigit() and length.isdigit():
                        slider.max = float(length)
                        slider.value = float(pos)

                        zaman_yazisi.value = (
                            f"{format_zaman(pos)} / {format_zaman(length)}"
                        )

                        if int(pos) >= state["length"] - 1000:
                            sonraki(None)

                        page.update()
                except:
                    pass

            time.sleep(0.2)

    def ses(cmd, dosya=""):
      if cmd == "play":

        state["path"] = os.path.abspath(f"assets/sounds/{dosya}")

        try:
            audio = MP3(state["path"])
            state["length"] = int(audio.info.length * 1000)
            print("SÜRE:", state["length"])
        except Exception as e:
            print("HATA:", e)
            state["length"] = 0

        ctypes.windll.winmm.mciSendStringW(
            "close sarki",
            None,
            0,
            None
        )

        ctypes.windll.winmm.mciSendStringW(
            f'open "{state["path"]}" type mpegvideo alias sarki',
            None,
            0,
            None
        )

        ctypes.windll.winmm.mciSendStringW(
            "set sarki time format milliseconds",
            None,
            0,
            None
        )

        ctypes.windll.winmm.mciSendStringW(
            "play sarki",
             None,
             0,
             None
        )

        slider.value = 0
        zaman_yazisi.value = "00:00 / " + format_zaman(str(state["length"]))

        page.update()
    def slider_degisti(e):
        if state["path"]:
            ctypes.windll.winmm.mciSendStringW(
                f"seek sarki to {int(e.control.value)}",
                None,
                0,
                None
            )

            ctypes.windll.winmm.mciSendStringW(
                "play sarki",
                None,
                0,
                None
            )

    klasor = "assets/sounds"

    sarkilar = (
        [f for f in os.listdir(klasor) if f.endswith(".mp3")]
        if os.path.exists(klasor)
        else []
    )

    def sonraki(e):
        if not sarkilar:
            return

        state["index"] = (state["index"] + 1) % len(sarkilar)
        ses("play", sarkilar[state["index"]])

    def onceki(e):
        if not sarkilar:
            return

        state["index"] = (state["index"] - 1) % len(sarkilar)
        ses("play", sarkilar[state["index"]])

    def MyButton(label, action):
        return ft.Container(
            content=ft.Text(
                label,
                size=24,
                weight="bold",
                text_align="center"
            ),
            bgcolor="#333333",
            padding=15,
            border_radius=20,
            on_click=action
        )

    slider = ft.Slider(
        min=0,
        max=100000,
        value=0,
        on_change_end=slider_degisti
    )

    liste = ft.Column(
        [
            ft.ElevatedButton(
                s.replace(".mp3", ""),
                on_click=lambda e, d=s, i=i: (
                    state.update({"index": i}),
                    ses("play", d)
                )
            )
            for i, s in enumerate(sarkilar)
        ],
        scroll="auto",
        height=300
    )

    page.add(
        ft.Text(
            "S-Player",
            size=30,
            weight="bold",
            color="#1DB954"
        ),

        zaman_yazisi,

        slider,

        liste,

        ft.Row(
            [
                MyButton("⏮", onceki),

                MyButton(
                    "▶",
                    lambda e: ctypes.windll.winmm.mciSendStringW(
                        "play sarki",
                        None,
                        0,
                        None
                    )
                ),

                MyButton(
                    "⏸",
                    lambda e: ctypes.windll.winmm.mciSendStringW(
                        "pause sarki",
                        None,
                        0,
                        None
                    )
                ),

                MyButton("⏭", sonraki),
            ],
            alignment="center"
        )
    )

    threading.Thread(
        target=ses_takip,
        daemon=True
    ).start()

ft.run(main)
