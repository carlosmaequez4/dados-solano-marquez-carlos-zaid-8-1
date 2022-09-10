valor = 0

def on_gesture_shake():
    global valor
    basic.clear_screen()
    valor = randint(0, 6)
    if valor == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif valor == 2:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
        """)
    elif valor == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    elif valor == 4:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    elif valor == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    elif valor == 6:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
