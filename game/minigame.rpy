default graciella_purrbear = SickAnimal(
                                name="Graciella",
                                image="Graciella/graciella",
                                sickness=[
                                    ["", ["Click on the vial of medicine, and then on Graciella to begin her treatment."], ["tutorial/CatalinaMinigame1"]],
                                    ["medicine", ["It seems Graciella has an upset stomach. She must have eaten something bad. Valencia please prepare the poltari medicine.", "Wait! She’s very bad at taking medicine through her mouth! She spits it out all the time! Isn’t there some other way to heal her?"], ["tutorial/Catalina_021_take1", "tutorial/Max_005_take1"]],
                                    ["syringe", ["I can give the medicine through injections, but you will need to return to the clinic for the next three days.", "That’s okay, please do that!"], ["tutorial/Catalina_022_take2", "tutorial/Max_006_take1"]]],
                                healthy_sfx="gracie_happy",
                                hurt_sfx="gracie_hurt",
                                x=92,
                                y=366,
                                icon_x=220,
                                icon_y=574)
default wonsh = SickAnimal(
                    name="Wonsh",
                    image="Wonsh/w1",
                    sickness=[
                        ["", ["It seems as though there is something stuck in Mateo’s underbelly. That’s why he can’t slither properly"], ["Scene 3a wonsh/Catalina_034_take1"]],
                        ["tweezers", ["Now I need to clean the wound and secure the injured area."], ["Scene 3a wonsh/Catalina_035_take2"]],
                        ["cotton", []]
                    ],
                    healthy_sfx="woonsh_happy",
                    hurt_sfx="woonsh_hurt",
                    x=170,
                    y=264,
                    icon_x=269,
                    icon_y=581)
default flocto = SickAnimal(
                    name="Flocto",
                    image="Flocto/pastel",
                    sickness=[
                        ["", ["Now that I can look at Leonardo closely, it seems they have a bad rash.", "Must have eaten something they shouldn’t have - like chocolate."], ["Scene 3b flockto/Catalina_039_take2", "Scene 3b flockto/Catalina_040_take1"]],
                        ["cooling-lotion", ["It would be best to give them something to clear their digestive system too."], ["Scene 3b flockto/Catalina_041_take1"]],
                        ["medicine", []]
                    ],
                    healthy_sfx="flockto_happy",
                    hurt_sfx="flockto_hurt",
                    x=165,
                    y=209,
                    icon_x=388,
                    icon_y=295)
default lemurin = SickAnimal(
                    name="Lemurino",
                    image="Lemurino/orange",
                    sickness=[
                        ["", ["First we need to calm Emilia down."], ["Scene 3c lemurin/Catalina_048_take1"]],
                        ["herbs", ["Yes! By burning the calming herbs we can sedate the lemurin!", "Now she will let us look at her!", "A patch of fur is stuck together with blood. I can’t see what’s below it."], ["Scene 3c lemurin/Catalina_049_take1", "Scene 3c lemurin/Catalina_050_take1", "Scene 3c lemurin/Catalina_051_take1"]],
                        ["scissors", ["Now that the fur isn’t in the way I see an open wound. I have to clean it first, sew it up and then dress the wound."], ["Scene 3c lemurin/Catalina_052_take1"]],
                        ["cotton", []],
                        ["needle-set", []],
                        ["band-aid", []]
                    ],
                    healthy_sfx="lemurin_happy",
                    hurt_sfx="lemurin_pain",
                    x=196,
                    y=290,
                    icon_x=327,
                    icon_y=367)
default phoenix = SickAnimal(
                    name="Phoenix",
                    image="Phoenix/phoenix",
                    sickness=[
                        ["", ["Time to examine the phoenix and see how we can heal it!"], ["Scene 7/Catalina_091_take1"]],
                        ["herbs", ["Oh no, it’s not working! Let’s try again!"], ["Scene 7/Catalina_092"]],
                        ["scissors", ["The traditional methods are useless. I guess I have to try healing magic!"], ["Scene 7/Catalina_093_take2"]],
                        ["jewel", ["No! I’m not strong enough!", "Maybe I can help?", "Let’s try together!"], ["Scene 7/Catalina_094_take1", "Scene 7/Valencia_030_take2", "Scene 7/Catalina_095_take2"]],
                        ["jewel", ["Noooo!"], ["Scene 7/Catalina_096_take1"]]
                    ],
                    healthy_sfx="phoenix_happy",
                    hurt_sfx="phoenix_pain",
                    x=0,
                    y=80,
                    icon_x=750,
                    icon_y=490,
                    can_win=False)
default phoenix_2 = SickAnimal(
                        name="Phoenix",
                        image="Phoenix/phoenix",
                        sickness=[
                            ["", ["Let’s get started."], ["Scene 10/Catalina_136_take2"]],
                            ["jewel", ["Again!"], ["Scene 10/Diedriech_028_take1"]],
                            ["jewel", ["Once again!"], ["Scene 10/Valencia_048_take1"]],
                            ["jewel", ["Now we have to finish the treatment."], ["Scene 10/Catalina_137_take2"]],
                            ["band-aid", [], [""]]
                        ],
                        healthy_sfx="phoenix_happy",
                        hurt_sfx="phoenix_pain",
                        x=0,
                        y=80,
                        icon_x=750,
                        icon_y=490)

default seen_minigame = []
default viewing_item = ""

init python:

    class SickAnimal():

        def __init__(self, name, image, sickness, healthy_sfx, hurt_sfx, x, y, icon_x, icon_y, can_win=True):
            self.name = name
            self._image = image
            self.sickness = sickness
            self.steps = len(self.sickness)
            self.correct = 0
            self.incorrect = 0
            self.current = 0
            self.healthy_sfx = healthy_sfx
            self.hurt_sfx = hurt_sfx
            self.x = x
            self.y = y
            self.icon_x = icon_x
            self.icon_y = icon_y
            self.can_win = can_win

            self.text_token = 0
            self.last_sumbitted = ""
            self.is_correct = False

        def submit(self, item):
            self.last_sumbitted = item

            if self.sickness[self.current][0] == item:
                self.correct += 1
                self.is_correct = True
                self.current += 1
                renpy.play("audio/minigame/correct.ogg", "sound")
                if self.can_win:
                    renpy.play("audio/minigame/sfx/" + self.healthy_sfx + ".ogg", "audio")
                else:
                    renpy.play("audio/minigame/sfx/" + self.hurt_sfx + ".ogg", "audio")
            else:
                self.is_correct = False
                self.incorrect += 1
                renpy.play("audio/minigame/wrong.ogg", "sound")
                renpy.play("audio/minigame/sfx/" + self.hurt_sfx + ".ogg", "audio")
                renpy.show_layer_at([shake_screen], layer="screens")

            if self.incorrect == 3:
                renpy.jump("loss")
            self.text_token = 0

        def advance(self):
            self.text_token += 1

            if self.current == 0:
                self.current += 1
                self.correct += 1

        @property
        def image(self):
            if self.correct == self.steps and self.can_win:
                return "gui/minigame/pets/" + self._image + "-healthy.png"
            return "gui/minigame/pets/" + self._image + "-sick.png"

        @property
        def sound(self):
            if self.correct == self.steps:
                return "audio/minigame/sfx/" + self.healthy_sfx + ".ogg"
            return "audio/minigame/sfx/" + self.hurt_sfx + ".ogg"

        @property
        def icon(self):
            if self.current == 0:
                return None

            if len(self.sickness) >= self.current + 1:
                return "gui/minigame/icons/" + self.sickness[self.current][0] + ".png"

        @property
        def text(self):
            if self.current == 0 and self.sickness[0][1]:
                if self.sickness[0][2]:
                    renpy.play("audio/minigame/voice/" + self.sickness[0][2][0] + ".ogg", "sound")
                return self.sickness[0][1][0]
            elif self.current == 0 and not self.sickness[0][1]:
                self.current += 1
                self.correct += 1
                return ""

            if self.is_correct == False and self.current > 0:
                return ""

            if self.text_token < len(self.sickness[self.current-1][1]) and self.current != 0:
                if self.sickness[self.current-1][2][self.text_token]:
                    renpy.play("audio/minigame/voice/" + self.sickness[self.current-1][2][self.text_token] + ".ogg", "sound")
                return self.sickness[self.current-1][1][self.text_token]
            return ""

        @property
        def done_with_minigame(self):
            if self.correct == self.steps and self.text_token >= len(self.sickness[self.current-1][1]):
                return True
            return False

        @property
        def reset(self):
            self.correct = 0
            self.incorrect = 0
            self.current = 0
            self.text_token = 0
            self.last_sumbitted = ""
            self.is_correct = False

screen minigame(animal, dramatic_music=False):
    predict False

    on "show":
        action If(dramatic_music, true=Play("music", "general drama.ogg"), false=Play("music", "minigame mayhem.ogg"))
    on "replace":
        action If(dramatic_music, true=Play("music", "general drama.ogg"), false=Play("music", "minigame mayhem.ogg"))
    on "replaced":
        action If(dramatic_music, true=Play("music", "general drama.ogg"), false=Play("music", "minigame mayhem.ogg"))
    default holding = ""
    default items = [
        ["herbs", 725, -2],
        ["medicine", 881, 43],
        ["tweezers", 1019, 36],
        ["scissors", 1205, 31],
        ["jewel", 1397, 32],
        ["needle-set", 816, 375],
        ["syringe", 836, 536],
        ["cooling-lotion", 1051, 392],
        ["band-aid", 1354, 319],
        ["cotton", 1308, 526],
    ]

    add "gui/minigame/background.png"
    add "gui/minigame/briefcase.png"
    add "gui/minigame/lancuszek.png" xpos 1548 ypos 50

    imagebutton:
        idle Solid("#00000000")
        hover Solid("#00000000")

        action Function(animal.advance)

    button:
        background animal.image
        focus_mask True

        sensitive animal.text == ""
        action If(holding, true=[Function(animal.submit, item=holding), SetScreenVariable("holding", "")], false=Play("sound", animal.sound))

        xpos animal.x
        ypos animal.y

    if animal.icon and animal.text == "":
        add animal.icon xpos animal.icon_x ypos animal.icon_y:
            xysize (60, 60)

    for im, x, y in items:
        imagebutton:
            idle "gui/minigame/items/" + im + ".png"
            hover "gui/minigame/items/" + im + "-light.png"

            focus_mask True

            action Play("sound", "audio/minigame/" + im + ".ogg"), SetScreenVariable("holding", im)
            xpos x
            ypos y

    text animal.text xmaximum 1700 outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] size 30 font "gui/fonts/OpenSans-SemiBold.ttf" text_align 0.5 xalign 0.5 yalign 0.95

    if animal.done_with_minigame:
        add Solid("#00000050")

        if animal.can_win:
            if animal.incorrect == 0:
                add "gui/minigame/badges/" + animal.name + " green sticker.png" xalign 0.5 yalign 0.5
            elif animal.incorrect == 1:
                add "gui/minigame/badges/" + animal.name + " yellow sticker.png" xalign 0.5 yalign 0.5
            elif animal.incorrect == 2:
                add "gui/minigame/badges/" + animal.name + " red sticker.png" xalign 0.5 yalign 0.5
        else:
            add "gui/minigame/badges/" + animal.name + " red sticker.png" xalign 0.5 yalign 0.5

        imagebutton:
            idle Solid("#00000000")
            hover Solid("#00000000")

            action Return()


screen minigame_tutorial(animal):
    default items = [
        ["herbs", "herbs_minigame", 725, -2],
        ["medicine", "medicine_minigame", 881, 43],
        ["tweezers", "tweezers_minigame", 1019, 36],
        ["scissors", "scissors_minigame", 1205, 31],
        ["jewel", "jewel_minigame", 1397, 32],
        ["needle-set", "needle_set_minigame", 816, 375],
        ["syringe", "syringe_minigame", 836, 536],
        ["cooling-lotion", "cooling_lotion_minigame", 1051, 392],
        ["band-aid", "band_aid_minigame", 1354, 319],
        ["cotton", "cotton_minigame", 1308, 526],
    ]

    add "gui/minigame/background.png"
    add "gui/minigame/briefcase.png"
    add "gui/minigame/lancuszek.png" xpos 1548 ypos 50

    if viewing_item:
        add "gui/minigame/icons/" + viewing_item + ".png" xpos animal.icon_x ypos animal.icon_y:
            xysize (60, 60)

    button:
        background animal.image
        focus_mask True

        action Jump("animal_minigame")

        xpos animal.x
        ypos animal.y

    for im, l, x, y in items:
        imagebutton:
            idle "gui/minigame/items/" + im + ".png"
            hover "gui/minigame/items/" + im + "-light.png"

            focus_mask True

            action Jump(l)
            xpos x
            ypos y

screen choose_animal():
    add Solid("#00000050")

    hbox:
        xalign 0.5
        yalign 0.5

        if not flocto.done_with_minigame:
            imagebutton:
                idle "gui/minigame/pets/Flocto/pastel-sick.png"
                hover "gui/minigame/pets/Flocto/pastel-sick.png"

                action Jump("ch1_s3_2")

        if not wonsh.done_with_minigame:
            imagebutton:
                idle "gui/minigame/pets/Wonsh/w1-sick.png"
                hover "gui/minigame/pets/Wonsh/w1-sick.png"

                action Jump("ch1_s3_1")

        if not lemurin.done_with_minigame:
            imagebutton:
                idle "gui/minigame/pets/Lemurino/orange-sick.png"
                hover "gui/minigame/pets/Lemurino/orange-sick.png"

                action Jump("ch1_s3_3")

label tutorial:
    $ minigame_animal = 'graciella'
    image failAnimal = "gui/minigame/pets/Graciella/graciella-sick.png"
    image failBadge = "gui/minigame/badges/Graciella red sticker.png"
    show screen minigame_tutorial(graciella_purrbear)

    voice "audio/minigame/voice/tutorial/Catalina_005_take1.ogg"
    c "In this mini-game you will be able to heal the many mythical animals my friends and I encounter."

    voice "audio/minigame/voice/tutorial/Catalina_006_take1.ogg"
    c "The first mini-game is a tutorial. Your task is to find out what Graciella’s problem is and use the right tool to heal her."

    voice "audio/minigame/voice/tutorial/Catalina_007_take1.ogg"
    c "First let me show you what tools I have available. On Graciella you can see what symbol each tool corresponds to."

    jump minigame_screen_label

label herbs_minigame:
    $ viewing_item = "herbs"
    if "herbs" not in seen_minigame:
        $ seen_minigame.append("herbs")
    voice "audio/minigame/voice/tutorial/Catalina_008_take2.ogg"
    "The herbs can be burned and their smoke is useful to lessen the pain of animals when inhaled."
    jump minigame_screen_label

label medicine_minigame:
    $ viewing_item = "medicine"
    if "medicine" not in seen_minigame:
        $ seen_minigame.append("medicine")
    voice "audio/minigame/voice/tutorial/Catalina_012_take1.ogg"
    "The medicine can be given through the pet’s mouth. The liquid form makes it easier to take in. Valencia will prepare the right medicine when requested."
    jump minigame_screen_label

label tweezers_minigame:
    $ viewing_item = "tweezers"
    if "tweezers" not in seen_minigame:
        $ seen_minigame.append("tweezers")
    voice "audio/minigame/voice/tutorial/Catalina_011_take1.ogg"
    "The pincers can be used to remove foreign objects from wounds."
    jump minigame_screen_label

label scissors_minigame:
    $ viewing_item = "scissors"
    if "scissors" not in seen_minigame:
        $ seen_minigame.append("scissors")
    voice "audio/minigame/voice/tutorial/Catalina_009_take2.ogg"
    "The scissors can be used to cut out clumps of fur to see the wounds better."
    jump minigame_screen_label

label jewel_minigame:
    $ viewing_item = "jewel"
    if "jewel" not in seen_minigame:
        $ seen_minigame.append("jewel")
    voice "audio/minigame/voice/tutorial/Catalina_013_part1.ogg"
    "This is the amulet with a magical crystal I use to channel my magic into healing power."
    voice "audio/minigame/voice/tutorial/Catalina_013_part2.ogg"
    "However, healing pets with magic is very invasive. We should only do it when there is no other choice."
    jump minigame_screen_label

label needle_set_minigame:
    $ viewing_item = "needle-set"
    if "needle_set" not in seen_minigame:
        $ seen_minigame.append("needle_set")
    voice "audio/minigame/voice/tutorial/Catalina_010_take2.ogg"
    "If we are dealing with an open wound, the needle and thread should be used to sew it closed!"
    jump minigame_screen_label

label syringe_minigame:
    $ viewing_item = "syringe"
    if "syringe" not in seen_minigame:
        $ seen_minigame.append("syringe")
    voice "audio/minigame/voice/tutorial/Catalina_014_take2.ogg"
    "The syringe is used to give medicine via injections. Sometimes this is the best way for an animal to receive treatment."
    jump minigame_screen_label

label cooling_lotion_minigame:
    $ viewing_item = "cooling-lotion"
    if "cooling_lotion" not in seen_minigame:
        $ seen_minigame.append("cooling_lotion")
    voice "audio/minigame/voice/tutorial/Catalina_016_take1.ogg"
    "The jar has ointment in it, which can be applied to the animal’s skin. It helps with rashes and other common skin diseases."
    jump minigame_screen_label

label band_aid_minigame:
    $ viewing_item = "band-aid"
    if "band_aid" not in seen_minigame:
        $ seen_minigame.append("band_aid")
    voice "audio/minigame/voice/tutorial/Catalina_015_take1.ogg"
    "The bandage is used for covering up wounded areas, so no outside contagion can damage them further."
    jump minigame_screen_label

label cotton_minigame:
    $ viewing_item = "cotton"
    if "cotton" not in seen_minigame:
        $ seen_minigame.append("cotton")
    voice "audio/minigame/voice/tutorial/Catalina_017_take1.ogg"
    "This jar has cotton pads in it, which can be used to clean wounds."
    jump minigame_screen_label

label animal_minigame:
    voice "audio/minigame/voice/tutorial/Catalina_018_part1.ogg"
    "This is the pet we are healing currently. Right now we have Graciella, a purrbear on the surgery table."
    voice "audio/minigame/voice/tutorial/Catalina_018_part2.ogg"
    "Her owner is Maximiano Rozario and they’ve been coming to my clinic for a year now."
    jump minigame_screen_label

label minigame_screen_label:
    $ viewing_item = ""
    if len(seen_minigame) == 10:
        voice "audio/minigame/voice/tutorial/Catalina_020_take2.ogg"
        "Is everything clear? Are you ready to start healing Graciella?"

        menu:
            "Yes":
                jump first_minigame
            "No":
                $ seen_minigame = []
                jump tutorial

    show screen minigame_tutorial(graciella_purrbear)
    window hide
    while True:
        pause

label first_minigame:
    $ minigame_animal = 'graciella'
    image failAnimal = "gui/minigame/pets/Graciella/graciella-sick.png"
    image failBadge = "gui/minigame/badges/Graciella red sticker.png"
    hide screen minigame
    $ quick_menu = False
    $ graciella_purrbear.reset
    call screen minigame(graciella_purrbear)
    $ renpy.transition(dissolve)
    hide screen minigame_tutorial
    $ quick_menu = True
    hide screen minigame
    jump ch1_s2a

label animal_choice:
    if wonsh.done_with_minigame and flocto.done_with_minigame and lemurin.done_with_minigame:
        jump ch1_s4
    call screen choose_animal

label second_minigame:
    $ minigame_animal = 'wonsh'
    $ wonshMinigame = True
    $ quick_menu = False
    $ renpy.transition(dissolve)
    call screen minigame(wonsh)
    $ renpy.transition(dissolve)
    $ quick_menu = True
    hide screen minigame
    jump ch1_s3_1a

label third_minigame:
    $ minigame_animal = 'flocto'
    image failAnimal = "gui/minigame/pets/Flocto/pastel-sick.png"
    image failBadge = "gui/minigame/badges/Flocto red sticker.png"
    $ quick_menu = False
    $ renpy.transition(dissolve)
    call screen minigame(flocto)
    $ renpy.transition(dissolve)
    $ quick_menu = True
    hide screen minigame
    jump ch1_s3_2a

label fourth_minigame:
    $ minigame_animal = 'lemurin'
    image failAnimal = "gui/minigame/pets/Lemurino/orange-sick.png"
    image failBadge = "gui/minigame/badges/Lemurino red sticker.png"
    $ quick_menu = False
    $ renpy.transition(dissolve)
    call screen minigame(lemurin)
    $ renpy.transition(dissolve)
    $ quick_menu = True
    hide screen minigame
    jump ch1_s3_3a

label post_animal_choice:
    $ results = wonsh.incorrect + flocto.incorrect + lemurin.incorrect

    if results < 3:
        voice "audio/minigame/voice/Scene 4/Catalina_055_take2.ogg"
        c "Today was a great day!"
        "I can’t help the bright smile that appears on my face. I love my job and it brings me a lot of satisfaction."
        voice "audio/minigame/voice/Scene 4/Valencia_012_take1.ogg"
        v "Yes, and no major surgeries-"
        "Our happiness is interrupted by loud banging on the entrance door. It’s past opening hours, but that’s not the first time we find ourselves in this situation."
        "I can’t say I’m surprised. Everything has gone too smoothly today."
    else:
        voice "audio/minigame/voice/Scene 4/Catalina_056_take1.ogg"
        c "Today could have been better, but at least we made no major mistakes."
        "I smile at her softly. It certainly hasn’t been the best day in the history of the clinic, but still, I love my job."
        voice "audio/minigame/voice/Scene 4/Valencia_013_take2.ogg"
        v "Yes, and no major surgeries-"
        "Our conversation is interrupted by loud banging on the entrance door. It’s past opening hours, but that’s not the first time we find ourselves in this situation."
        "I can’t say I’m surprised."

    jump fifth_minigame

label fifth_minigame:
    $ minigame_animal = 'phoenix'
    image failAnimal = "gui/minigame/pets/Phoenix/phoenix-sick.png"
    image failBadge = "gui/minigame/badges/Phoenix red sticker.png"
    $ quick_menu = False
    $ phoenix.reset
    $ renpy.transition(dissolve)
    call screen minigame(phoenix)
    $ renpy.transition(dissolve)
    $ quick_menu = True
    hide screen minigame
    jump ch1_s7a

label sixth_minigame:
    $ first_phoenix = False
    $ minigame_animal = 'phoenix'
    image failAnimal = "gui/minigame/pets/Phoenix/phoenix-sick.png"
    image failBadge = "gui/minigame/badges/Phoenix red sticker.png"
    $ quick_menu = False
    $ phoenix_2.reset
    $ renpy.transition(dissolve)
    call screen minigame(phoenix_2, dramatic_music=True)
    $ renpy.transition(dissolve)
    $ quick_menu = True
    hide screen minigame
    jump ch1_s11

label loss:
    $ renpy.transition(dissolve)
    hide screen minigame
    if minigame_animal == 'phoenix':
        scene bg vet day with fade
    else:
        scene bg road day with fade

    if minigame_animal == 'graciella':
        image failGracie = "gui/minigame/pets/Graciella/graciella-sick.png"
        image gracieBadge = "gui/minigame/badges/Graciella red sticker.png"

        "Do you want to try again?"

        menu:
            "Yes":
                jump first_minigame
            "No":
                return
        show failGracie at offscreenleft
        show failGracie at offscreenright with MoveTransition(1.0)
        "Oh no! The injured animal escaped!"
        show gracieBadge at trueCenter with dissolve
        pause 2.0
        scene black with dissolve

    elif minigame_animal == "wonsh":
        image failWonsh = "gui/minigame/pets/Wonsh/w1-sick.png"
        image wonshBadge = "gui/minigame/badges/Wonsh red sticker.png"

        show failWonsh at offscreenleft
        show failWonsh at offscreenright with MoveTransition(1.0)
        "Oh no! The injured animal escaped!"
        show wonshBadge at trueCenter with dissolve
        pause 2.0
        scene black with dissolve
        return

    elif minigame_animal == 'flocto':
        image failFlocto = "gui/minigame/pets/Flocto/pastel-sick.png"
        image floctoBadge = "gui/minigame/badges/Flocto red sticker.png"

        show failFlocto at offscreenleft
        show failFlocto at offscreenright with MoveTransition(1.0)
        "Oh no! The injured animal escaped!"
        show floctoBadge at trueCenter with dissolve
        pause 2.0
        scene black with dissolve

    elif minigame_animal == 'lemurin':
        image failLemurin = "gui/minigame/pets/Lemurino/orange-sick.png"
        image lemurinBadge = "gui/minigame/badges/Lemurino red sticker.png"

        show failLemurin at offscreenleft
        show failLemurin at offscreenright with MoveTransition(1.0)
        "Oh no! The injured animal escaped!"
        show lemurinBadge at trueCenter with dissolve
        pause 2.0
        scene black with dissolve

    elif minigame_animal == 'phoenix':
        if first_phoenix:
            if phoenix.incorrect > 2:
                "Do you want to try again?"

                menu:
                    "Yes":
                        jump fifth_minigame
                    "No":
                        return

            jump ch1_s7a
        else:
            if phoenix_2.incorrect > 2:
                "Do you want to try again?"

                menu:
                    "Yes":
                        jump sixth_minigame
                    "No":
                        return

    return
