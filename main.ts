input.onButtonPressed(Button.A, function () {
    music.playMelody("C5 B B C5 B A C5 B ", 120)
})
input.onButtonPressed(Button.B, function () {
    Kitronik_Move_Motor.stop()
    music.playMelody("C5 B B C5 B A C5 B ", 120)
    radio.sendString("hi")
})
Kitronik_Move_Motor.setUltrasonicUnits(Kitronik_Move_Motor.Units.Centimeters)
basic.forever(function () {
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    if (Kitronik_Move_Motor.measure() <= 15) {
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Reverse, 30)
        basic.showLeds(`
            # # . # #
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            `)
        basic.pause(2000)
        Kitronik_Move_Motor.stop()
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.Left, 25)
        basic.pause(2000)
    } else {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 35)
    }
})
