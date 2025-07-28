def on_button_pressed_a():
    makeyMakey.press_key(makeyMakey.KeyPress.A)
    basic.show_leds("""
        . # # # #
        . # # . #
        . . # . #
        . . # # #
        . . # # #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_press_makey_types_mouse_clicked():
    radio.send_string("Coeur")
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        . . . . .
        """)
makeyMakey.on_press_event(makeyMakey.MakeyMakeyPressEventTypes.MOUSE_CLICKED,
    on_press_makey_types_mouse_clicked)

def on_press_makey_types_key_pressed():
    radio.send_string("Croix")
    basic.show_icon(IconNames.NO)
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        . . . . .
        """)
makeyMakey.on_press_event(makeyMakey.MakeyMakeyPressEventTypes.KEY_PRESSED,
    on_press_makey_types_key_pressed)

makeyMakey.sx1509_init()