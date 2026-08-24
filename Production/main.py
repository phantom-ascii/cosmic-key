#Currently the board only prints abcd, space and volume controls but once i get the xiao i will do some testing and try to add full macros to each key

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.direct import DirectPins
from kmk.modules.encoder import EncoderHandler


keyboard = KMKKeyboard()

# key stuf
keyboard.matrix = DirectPins(
    pins=(
        board.D0,
        board.D1,
        board.D2,
        board.D3,
        board.D4,
    )
)

# key binds
keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.SPACE,
    ]
]

# knob stuff
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# knob pin
encoder.pins = (
    (board.D5, board.D6, board.D7),
)

# knob binds
encoder.map = [
    (
        (KC.VOLD, KC.VOLU),
    ),
]

keyboard.go()
