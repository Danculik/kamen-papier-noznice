def on_button_pressed_a():
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
    basic.pause(2000)
    ukaz_skore()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
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
    basic.pause(2000)
    ukaz_skore()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
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
    basic.pause(2000)
    ukaz_skore()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    global pocitac, clovek
    basic.show_string("NOVA HRA")
    pocitac = 0
    clovek = 0
    for index in range(5):
        pass
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def ukaz_skore():
    basic.show_string("TY")
    basic.show_number(clovek)
    basic.show_string("JA")
    basic.show_number(pocitac)
    basic.pause(2000)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                . # . # .
    """)
pocitac_vybral = 0
clovek = 0
pocitac = 0
pocitac = 0
clovek = 0
basic.show_string("K P N")
basic.show_leds("""
    # . . . #
        . # . # .
        . . # . .
        . # . # .
        . # . # .
""")