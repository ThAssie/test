input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . # # # #
        . # # . #
        . . # . #
        . . # # #
        . . # # #
        `)
})
makeyMakey.onPressEvent(makeyMakey.MakeyMakeyPressEventTypes.MouseClicked, function () {
    radio.sendString("Coeur")
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        . . . . .
        `)
})
makeyMakey.onPressEvent(makeyMakey.MakeyMakeyPressEventTypes.KeyPressed, function () {
    radio.sendString("Croix")
    basic.showIcon(IconNames.No)
    basic.showLeds(`
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        . . . . .
        `)
})
makeyMakey.sx1509Init()
