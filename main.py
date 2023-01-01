def papier():
    global pocitac_vybral, pocitac, clovek
    pocitac_vybral = randint(0, 2)
    if 1 == pocitac_vybral:
        basic.show_icon(IconNames.ASLEEP)
    elif 2 == pocitac_vybral:
        basic.show_icon(IconNames.HAPPY)
        pocitac += 1
    else:
        basic.show_icon(IconNames.SAD)
        clovek += 1
    basic.pause(1000)
    ukaz_skore()

def on_button_pressed_a():
    global auto
    auto = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def kamen():
    global pocitac_vybral, pocitac, clovek
    pocitac_vybral = randint(0, 2)
    if 0 == pocitac_vybral:
        basic.show_icon(IconNames.ASLEEP)
    elif 1 == pocitac_vybral:
        basic.show_icon(IconNames.HAPPY)
        pocitac += 1
    else:
        basic.show_icon(IconNames.SAD)
        clovek += 1
    basic.pause(1000)
    ukaz_skore()
def noznice():
    global pocitac_vybral, pocitac, clovek
    pocitac_vybral = randint(0, 2)
    if 2 == pocitac_vybral:
        basic.show_icon(IconNames.ASLEEP)
    elif 0 == pocitac_vybral:
        basic.show_icon(IconNames.HAPPY)
        pocitac += 1
    else:
        basic.show_icon(IconNames.SAD)
        clovek += 1
    basic.pause(1000)
    ukaz_skore()

def on_button_pressed_ab():
    global auto
    auto = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global auto
    auto = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    global auto, pocitac, clovek
    auto = 0
    pocitac = 0
    clovek = 0
    basic.show_string("NOVA HRA")
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                . # . # .
    """)
    for index in range(5):
        while auto == 0:
            if input.button_is_pressed(Button.A):
                kamen()
            elif input.button_is_pressed(Button.B):
                papier()
            elif input.button_is_pressed(Button.AB):
                noznice()
        auto = 0
    while 0 == 0:
        basic.show_string("TY")
        basic.show_number(clovek)
        basic.show_string("JA")
        basic.show_number(pocitac)
        basic.show_leds("""
            . # # # .
                        # . . . #
                        # # . # #
                        # . . . #
                        . # # # .
        """)
        basic.pause(1000)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def ukaz_skore():
    basic.show_string("TY")
    basic.show_number(clovek)
    basic.show_string("JA")
    basic.show_number(pocitac)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                . # . # .
    """)
auto = 0
pocitac_vybral = 0
clovek = 0
pocitac = 0
pocitac = 0
clovek = 0
basic.show_string("K P N")
basic.show_leds("""
    . # # # .
        # . . . #
        # # . # #
        # . . . #
        . # # # .
""")