def on_button_pressed_a():
    music.play_melody("C5 B B C5 B A C5 B ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Kitronik_Move_Motor.stop()
    music.play_melody("C5 B B C5 B A C5 B ", 120)
    radio.send_string("hi")
input.on_button_pressed(Button.B, on_button_pressed_b)

Kitronik_Move_Motor.set_ultrasonic_units(Kitronik_Move_Motor.Units.CENTIMETERS)

def on_forever():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    if Kitronik_Move_Motor.measure() <= 15:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE, 30)
        basic.show_leds("""
            # # . # #
                        # # . # #
                        . . . . .
                        . # # # .
                        # . . . #
        """)
        basic.pause(2000)
        Kitronik_Move_Motor.stop()
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.LEFT, 25)
        basic.pause(2000)
    else:
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 50)
basic.forever(on_forever)
