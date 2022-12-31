input.onButtonPressed(Button.A, function () {
    pocitac_vybral = randint(0, 2)
    if (0 == pocitac_vybral) {
        basic.showIcon(IconNames.Asleep)
    } else if (1 == pocitac_vybral) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    basic.pause(2000)
    basic.showString("K P N")
})
input.onButtonPressed(Button.AB, function () {
    pocitac_vybral = randint(0, 2)
    if (2 == pocitac_vybral) {
        basic.showIcon(IconNames.Asleep)
    } else if (0 == pocitac_vybral) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    basic.pause(2000)
    basic.showString("K P N")
})
input.onButtonPressed(Button.B, function () {
    pocitac_vybral = randint(0, 2)
    if (1 == pocitac_vybral) {
        basic.showIcon(IconNames.Asleep)
    } else if (2 == pocitac_vybral) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    basic.pause(2000)
    basic.showString("K P N")
})
let pocitac_vybral = 0
basic.showString("K P N")
basic.forever(function () {
	
})
