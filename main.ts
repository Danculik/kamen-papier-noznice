function papier () {
    pocitac_vybral = randint(0, 2)
    if (1 == pocitac_vybral) {
        basic.showIcon(IconNames.Asleep)
    } else if (2 == pocitac_vybral) {
        basic.showIcon(IconNames.Happy)
        pocitac += 1
    } else {
        basic.showIcon(IconNames.Sad)
        clovek += 1
    }
    basic.pause(1000)
    ukaz_skore()
}
input.onButtonPressed(Button.A, function () {
    auto = 1
})
function kamen () {
    pocitac_vybral = randint(0, 2)
    if (0 == pocitac_vybral) {
        basic.showIcon(IconNames.Asleep)
    } else if (1 == pocitac_vybral) {
        basic.showIcon(IconNames.Happy)
        pocitac += 1
    } else {
        basic.showIcon(IconNames.Sad)
        clovek += 1
    }
    basic.pause(1000)
    ukaz_skore()
}
function noznice () {
    pocitac_vybral = randint(0, 2)
    if (2 == pocitac_vybral) {
        basic.showIcon(IconNames.Asleep)
    } else if (0 == pocitac_vybral) {
        basic.showIcon(IconNames.Happy)
        pocitac += 1
    } else {
        basic.showIcon(IconNames.Sad)
        clovek += 1
    }
    basic.pause(1000)
    ukaz_skore()
}
input.onButtonPressed(Button.AB, function () {
    auto = 1
})
input.onButtonPressed(Button.B, function () {
    auto = 1
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    auto = 0
    pocitac = 0
    clovek = 0
    basic.showString("NOVA HRA")
    for (let index = 0; index < 5; index++) {
        while (auto == 0) {
            if (input.buttonIsPressed(Button.A)) {
                kamen()
                auto = 0
            } else if (input.buttonIsPressed(Button.B)) {
                papier()
                auto = 0
            } else if (input.buttonIsPressed(Button.AB)) {
                noznice()
                auto = 0
            }
        }
        basic.showIcon(IconNames.Heart)
        basic.pause(2000)
    }
    while (0 == 0) {
        basic.showString("TY")
        basic.showNumber(clovek)
        basic.showString("JA")
        basic.showNumber(pocitac)
        basic.showLeds(`
            . # # # .
            # . . . #
            # # . # #
            # . . . #
            . # # # .
            `)
    }
})
function ukaz_skore () {
    basic.showString("TY")
    basic.showNumber(clovek)
    basic.showString("JA")
    basic.showNumber(pocitac)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        . # . # .
        `)
}
let auto = 0
let pocitac_vybral = 0
let clovek = 0
let pocitac = 0
pocitac = 0
clovek = 0
basic.showString("K P N")
basic.showLeds(`
    . # # # .
    # . . . #
    # # . # #
    # . . . #
    . # # # .
    `)
