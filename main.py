"""     _   _ __   ___   _    ___        ___  ______   __     __
    | | / \\ \ / / | | |  / \ \      / / |/ / ___|  \ \   / /
 _  | |/ _ \\ V /| |_| | / _ \ \ /\ / /| ' /\___ \   \ \ / /
| |_| / ___ \| | |  _  |/ ___ \ V  V / | . \ ___) |   \ V /
 \___/_/   \_\_| |_| |_/_/   \_\_/\_/  |_|\_\____/     \_/

 _   _    _    ____ _  _______ ____  ____
| | | |  / \  / ___| |/ / ____|  _ \/ ___|
| |_| | / _ \| |   | ' /|  _| | |_) \___ \
|  _  |/ ___ \ |___| . \| |___|  _ < ___) |
|_| |_/_/   \_\____|_|\_\_____|_| \_\____/


Original program by Lucas Frias and Trey Campbell

Rewritten in Python by Lucas Frias

MIT License 2.0 (make cool stuff!!
"""

import pygame

from src.graphics import MainWindow

if __name__ == "__main__":
    mw = MainWindow()
    while True:
        mw.update()
