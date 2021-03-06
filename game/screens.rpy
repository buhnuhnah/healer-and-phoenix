 ################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say
style centeredTextbox:
    background Image("gui/textbox/centeredTextbox.png")

screen say(who, what):
    style_prefix "say"

    window:
        if centerTextbox == True:
            style "centeredTextbox"

            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who" color "#cf5d2b" size 24 font "gui/fonts/OpenSans-SemiBoldItalic.ttf" underline True xpos 406 ypos 450
            text what id "what" color "#383838" size 30 font "gui/fonts/OpenSans-SemiBold.ttf" xmaximum 1116 xpos 406 ypos 500
        else:
            id "window"
            style "window"

            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who" color "#cf5d2b" size 24 font "gui/fonts/OpenSans-SemiBoldItalic.ttf" underline True xpos 406 ypos 57

            text what id "what" color "#383838" size 30 font "gui/fonts/OpenSans-SemiBold.ttf" xmaximum 1116 xpos 406 ypos 105


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    yoffset -30

    background Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0)


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            button:
                xysize (1562, 99)
                background "gui/choice/choice.png"

                text i.caption font "gui/fonts/OpenSans-SemiBold.ttf" yalign 0.5 color "000000"
                action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    default buttons = [
        ["auto", 605, 968, Preference("auto-forward", "toggle")],
        ["skip", 776, 969, Skip()],
        ["save", 945, 968, ShowMenu('save')],
        ["load", 1114, 969, ShowMenu('load')],
        ["history", 1275, 969, ShowMenu('history')],
    ]

    if quick_menu:
        for im, x, y, act in buttons:
            imagebutton:
                idle "gui/textbox/" + im + ".png"
                hover "gui/textbox/hover_" + im + ".png"
                selected_idle "gui/textbox/hover_" + im + ".png"

                action act
                xpos x
                ypos y


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    default buttons = [
        ["New Game", 94, 106, Start()],
        ["load game", 376, 107, ShowMenu("load")],
        ["gallery", 658, 97, NullAction()],
        ["settings", 1138, 107, ShowMenu("preferences")],
        ["credits", 1382, 107, ShowMenu("credit")],
        ["help", 1616, 106, ShowMenu("help")],
        ["exit", 1843, 24, Quit(confirm=True)],
    ]

    add "gui/main_menu/bg.png"
    add "gui/main_menu/logo.png" xpos 807 ypos 43

    for im, x, y, act in buttons:
        imagebutton:
            idle "gui/main_menu/Deafaut/" + im + ".png"
            hover "gui/main_menu/hover/hover_" + im + ".png"

            hovered Play("sound", "audio/sfx/mouse_hover.ogg")
            action [Play("sound", "audio/sfx/on_mouse_button_down.ogg"), act]
            xpos x
            ypos y

            at mm_button_hover


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    on "show":
        action Function(renpy.show_layer_at, blur_bg_show, layer='master')
    on "hide":
        action Function(renpy.show_layer_at, blur_bg_hide, layer='master')
    add "gui/load/white.png"

    use file_slots(_("Save"))


screen load():

    tag menu

    if main_menu:
        on "show":
            action Play("sound", "audio/sfx/screen_changes_.ogg")
        add "gui/bg.png"
    else:
        on "show":
            action Function(renpy.show_layer_at, blur_bg_show, layer='master')
        on "hide":
            action Function(renpy.show_layer_at, blur_bg_hide, layer='master')
        add "gui/load/white.png"

    use file_slots(_("Load"))


screen file_slots(title):

    if title == "Load":
        add "gui/load/Load Game.png" xpos 849 ypos 60

    ## The grid of file slots.
    vpgrid:
        id "saveload"
        cols 1
        rows 12
        xpos 440
        ypos 268

        ysize 585

        yspacing 84

        for i in range(12):

            $ slot = i + 1

            button:
                xysize (1041, 139)

                idle_background "gui/load/1.png"
                hover_background "gui/load/1_hover.png"
                insensitive_background "gui/load/1.png"

                action FileAction(slot)

                if title == "Load" or FileTime(slot):
                    if FileTime(slot):
                        add "gui/load/Rectangle 58.png" xpos 319 ypos 49
                        add "gui/load/Rectangle 58.png" xpos 493 ypos 49
                        add "gui/load/Rectangle 58.png" xpos 664 ypos 49

                        fixed:
                            xysize (140, 40)
                            xpos 179
                            ypos 49
                            text str(FileJson(slot, "name", empty="", missing="")):
                                color "#383838"
                                size 20
                                xalign 0.5
                                yalign 0.5

                        fixed:
                            xysize (170, 40)
                            xpos 323
                            ypos 49
                            text FileTime(slot, format=_("{#file_time}%d/%m/%Y"), empty=_("empty slot")):
                                color "#383838"
                                size 20
                                xalign 0.5
                                yalign 0.5

                        fixed:
                            xysize (166, 40)
                            xpos 497
                            ypos 49
                            text "Chapter " + str(FileJson(slot, "chapter", empty="", missing="")):
                                color "#383838"
                                size 20
                                xalign 0.5
                                yalign 0.5

                        fixed:
                            xysize (166, 40)
                            xpos 668
                            ypos 49
                            $ minutes, seconds = divmod(FileJson(slot, "playtime", empty="", missing=""), 60)
                            $ hours, minutes = divmod(minutes, 60)
                            text str(str(int(hours)) + "h: " + str(int(minutes)) + "min"):
                                color "#383838"
                                size 20
                                xalign 0.5
                                yalign 0.5

                else:
                    add "gui/load/Component 45 ??? 2.png" xalign 0.5 yalign 0.5

                key "save_delete" action FileDelete(slot)

    vbar value YScrollValue("saveload"):
        xpos 1620
        ypos 228
        xsize 19
        ysize 625

        left_gutter 54
        right_gutter 54

        base_bar "gui/load/scroll1.png"
        thumb "gui/load/scroll2.png"
        thumb_offset 51

    imagebutton:
        idle "gui/history/Back to menu.png"
        hover "gui/history/hover_Back to menu.png"

        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action Return()
        xpos 878
        ypos 904

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    default page = "system"

    if main_menu:
        on "show":
            action Play("sound", "audio/sfx/screen_changes_.ogg")
        add "gui/bg.png"
    else:
        on "show":
            action Function(renpy.show_layer_at, blur_bg_show, layer='master')
        on "hide":
            action Function(renpy.show_layer_at, blur_bg_hide, layer='master')
        add "gui/settings/white.png"

    add "gui/settings/frame.png" xalign 0.5 yalign 0.5
    add "gui/settings/Setting.png" xpos 892 ypos 130

    imagebutton:
        idle "gui/settings/Component 5 ??? 3.png"
        hover "gui/settings/Component 5 ??? 1.png"
        selected_idle "gui/settings/Component 5 ??? 1.png"

        selected page == "system"
        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action SetScreenVariable("page", "system")
        xpos 580
        ypos 264
    add "gui/settings/Rectangle 62.png" xpos 860 ypos 267

    imagebutton:
        idle "gui/settings/Component 6 ??? 1.png"
        hover "gui/settings/Component 6 ??? 3.png"
        selected_idle "gui/settings/Component 6 ??? 3.png"

        selected page == "sound"
        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action SetScreenVariable("page", "sound")
        xpos 944
        ypos 264
    add "gui/settings/Rectangle 62.png" xpos 1156 ypos 267

    imagebutton:
        idle "gui/settings/Component 7 ??? 1.png"
        hover "gui/settings/Component 7 ??? 4.png"
        selected_idle "gui/settings/Component 7 ??? 4.png"

        selected page == "voice"
        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action SetScreenVariable("page", "voice")
        xpos 1217
        ypos 264

    if page == "system":
        default buttons = [
            ["Fullscreen.png", 296, 528, Preference("display", "fullscreen")],
            ["Window.png", 524, 528, Preference("display", "window")],
            ["Stop skipping.png", 805, 529, Preference("after choices", "stop")],
            ["Keep skipping.png", 1053, 529, Preference("after choices", "skip")],
            ["All.png", 296, 783, Preference("transitions", "all")],
            ["None.png", 524, 783, Preference("transitions", "none")],
            ["Read messages.png", 806, 783, Preference("skip", "seen")],
            ["All messages.png", 1053, 783, Preference("skip", "all")],
        ]

        add "gui/settings/Display.png" xpos 385 ypos 435
        add "gui/settings/After Choices.png" xpos 899 ypos 425
        add "gui/settings/Text Speed.png" xpos 1453 ypos 418
        add "gui/settings/Transitions.png" xpos 358 ypos 673
        add "gui/settings/Skip.png" xpos 956 ypos 674
        add "gui/settings/Auto Text Speed.png" xpos 1416 ypos 671

        for im, x, y, act in buttons:
            imagebutton:
                idle "gui/settings/Rectangle 14.png"
                hover "gui/settings/Rectangle 15.png"
                selected_idle "gui/settings/Rectangle 15.png"

                action act
                xpos x - 30
                ypos y + 7

            imagebutton:
                idle "gui/settings/" + im
                hover "gui/settings/" + im

                action act
                xpos x
                ypos y

        bar:
            left_bar "gui/settings/scrollbar2.png"
            right_bar "gui/settings/scrollbar.png"
            value Preference("text speed")
            thumb None
            xpos 1377
            ypos 540
        bar:
            left_bar "gui/settings/scrollbar2.png"
            right_bar "gui/settings/scrollbar.png"
            value Preference("auto-forward time")
            thumb None
            xpos 1377
            ypos 793

    elif page == "sound":
        add "gui/settings/Music Volume.png" xpos 882 ypos 436
        add "gui/settings/Global Voice Volume.png" xpos 837 ypos 557
        add "gui/settings/SFX Volume.png" xpos 893 ypos 677

        bar:
            left_bar "gui/settings/scrollbar2.png"
            right_bar "gui/settings/scrollbar.png"
            value Preference("music volume")
            thumb None
            xpos 809
            ypos 507
        bar:
            left_bar "gui/settings/scrollbar2.png"
            right_bar "gui/settings/scrollbar.png"
            value Preference("voice volume")
            thumb None
            xpos 809
            ypos 625
        bar:
            left_bar "gui/settings/scrollbar2.png"
            right_bar "gui/settings/scrollbar.png"
            value Preference("sound volume")
            thumb None
            xpos 809
            ypos 744

    elif page == "voice":
        default volumes = [
            ["avatar_catalina", "Catalina", 329, 471, "catalina"],
            ["avatar_max", "Max", 789, 471, "max"],
            ["avatar_valencia", "Valencia", 1248, 471, "valencia"],
            ["avatar_edmundo", "Edmundo", 329, 587, "edmundo"],
            ["avatar_diedriech", "Diedriech", 789, 587, "diedriech"],
            ["avatar_other", "Other", 1248, 587, "other"],
        ]

        for a_im, t_im, x, y, v_tag in volumes:
            frame:
                background None
                xysize (420, 98)
                xpos x
                ypos y

                add "gui/avatar/" + a_im + ".png"
                add "gui/settings/" + t_im + ".png" xpos 120 ypos 20
                #imagebutton:
                #    idle "gui/settings/Icon metro-volume-mute-5.png"
                #    hover "gui/settings/Icon metro-volume-mute-5.png"

                #    action ToggleVoiceMute(v_tag)
                #    xpos 246
                #    ypos 31

                bar:
                    xysize (300, 15)
                    left_bar "gui/settings/scrollbar2.png"
                    right_bar "gui/settings/scrollbar.png"
                    value SetCharacterVolume(v_tag)
                    thumb None
                    xpos 120
                    ypos 76

    imagebutton:
        idle "gui/history/Back to menu.png"
        hover "gui/history/hover_Back to menu.png"

        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action Return()
        xalign 0.5
        ypos 903

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False
    add "gui/history/frame.png" xalign 0.5 yalign 0.5
    add "gui/history/white.png"
    add "gui/history/History.png" xpos 897 ypos 130

    on "show":
        action Function(renpy.show_layer_at, blur_bg_show, layer='master')
    on "hide":
        action Function(renpy.show_layer_at, blur_bg_hide, layer='master')

    vpgrid:
        id "history"
        xpos 257
        ypos 252
        xsize 1360
        ysize 625
        cols 1

        vbox:
            spacing 25
            for i, h in enumerate(_history_list):
                if i % 2 == 0:
                    hbox:
                        xsize 1400

                        if h.who == "Catalina":
                            add "gui/avatar/avatar_catalina.png" xpos 46
                        elif h.who == "Max":
                            add "gui/avatar/avatar_max.png" xpos 46
                        elif h.who == "Valencia":
                            add "gui/avatar/avatar_valencia.png" xpos 46
                        elif h.who == "Edmundo":
                            add "gui/avatar/avatar_edmundo.png" xpos 46
                        elif h.who == "Diedriech":
                            add "gui/avatar/avatar_diedriech.png" xpos 46
                        else:
                            add "gui/avatar/avatar_other.png" xpos 46

                        fixed:
                            xsize 1187
                            ysize 80
                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what font "gui/fonts/OpenSans-Regular.ttf" size 25 xmaximum 1187 substitute False yoffset 8 xalign 0.0

                else:
                    hbox:
                        xsize 1400
                        spacing 30

                        fixed:
                            xsize 1187
                            ysize 80
                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what font "gui/fonts/OpenSans-Regular.ttf" size 25 xmaximum 1187 substitute False yoffset 8 xalign 1.0

                        if h.who == "Catalina":
                            add "gui/avatar/avatar_catalina.png" xpos 05
                        elif h.who == "Max":
                            add "gui/avatar/avatar_max.png" xpos 05
                        elif h.who == "Valencia":
                            add "gui/avatar/avatar_valencia.png" xpos 05
                        elif h.who == "Edmundo":
                            add "gui/avatar/avatar_edmundo.png" xpos 05
                        elif h.who == "Diedriech":
                            add "gui/avatar/avatar_diedriech.png" xpos 05
                        else:
                            add "gui/avatar/avatar_other.png"

    vbar value YScrollValue("history"):
        xpos 1620
        ypos 228
        xsize 19
        ysize 625

        left_gutter 54
        right_gutter 54

        base_bar "gui/load/scroll1.png"
        thumb "gui/load/scroll2.png"
        thumb_offset 51

    imagebutton:
        idle "gui/history/Back to menu.png"
        hover "gui/history/hover_Back to menu.png"

        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action Return()
        xpos 879
        ypos 903


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"
    on "show":
        action Play("sound", "audio/sfx/text_slides.ogg")

    on "show":
        action Function(renpy.show_layer_at, blur_bg_show, layer='master')
    on "hide":
        action Function(renpy.show_layer_at, blur_bg_hide, layer='master')

    if message == "Are you sure you want to quit?":
        frame:
            xysize (723, 320)
            xalign 0.5
            yalign 0.5
            background "gui/confirm/quit/Rectangle 37.png"

            add "gui/confirm/quit/Are You Sure You Want To Exit.png" xpos 137 ypos 90

            imagebutton:
                idle "gui/confirm/quit/yes.png"
                hover "gui/confirm/quit/yes_hover.png"

                action yes_action
                xpos 202
                ypos 151
            imagebutton:
                idle "gui/confirm/quit/no.png"
                hover "gui/confirm/quit/no_hover.png"

                action no_action
                xpos 372
                ypos 150

    elif "Loading will lose unsaved progress" in message:
        frame:
            xysize (575, 412)
            xalign 0.5
            yalign 0.5
            background Solid("#ffffff")

            add "gui/confirm/load/frame_exit.png" xalign 0.5 yalign 0.5
            add "gui/confirm/load/Are you sure you want to continueAll unsaved progress will be lost.png" xpos 106 ypos 143

            imagebutton:
                idle "gui/confirm/load/yes.png"
                hover "gui/confirm/load/yes_hover.png"

                action yes_action
                xpos 129
                ypos 241
            imagebutton:
                idle "gui/confirm/load/no.png"
                hover "gui/confirm/load/no_hover.png"

                action no_action
                xpos 299
                ypos 241

    elif "return to the main menu" in message:
        frame:
            xysize (575, 412)
            xalign 0.5
            yalign 0.5
            background Solid("#ffffff")

            add "gui/confirm/load/frame_exit.png" xalign 0.5 yalign 0.5
            text "Are you sure you want to return to the main menu?\nThis will lose unsaved progress." font "gui/fonts/OpenSans-Regular.ttf" color "#383838" size 20 text_align 0.5 xalign 0.5 ypos 130

            imagebutton:
                idle "gui/confirm/load/yes.png"
                hover "gui/confirm/load/yes_hover.png"

                action yes_action
                xpos 129
                ypos 241
            imagebutton:
                idle "gui/confirm/load/no.png"
                hover "gui/confirm/load/no_hover.png"

                action no_action
                xpos 299
                ypos 241
    elif "overwrite your save" in message:
        frame:
            xysize (575, 412)
            xalign 0.5
            yalign 0.5
            background Solid("#ffffff")

            add "gui/confirm/load/frame_exit.png" xalign 0.5 yalign 0.5
            text "Are you sure you want to overwrite your save?" font "gui/fonts/OpenSans-Regular.ttf" color "#383838" size 20 text_align 0.5 xalign 0.5 ypos 130

            imagebutton:
                idle "gui/confirm/load/yes.png"
                hover "gui/confirm/load/yes_hover.png"

                action yes_action
                xpos 129
                ypos 241
            imagebutton:
                idle "gui/confirm/load/no.png"
                hover "gui/confirm/load/no_hover.png"

                action no_action
                xpos 299
                ypos 241
    else:
        frame:
            background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
            padding gui.confirm_frame_borders.padding
            xalign .5
            yalign .5

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 150

                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "???" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "???" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "???" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

screen pause_menu():
    tag menu
    add "gui/game_menu/white.png"

    on "show":
        action Function(renpy.show_layer_at, blur_bg_show, layer='master')
    on "hide":
        action Function(renpy.show_layer_at, blur_bg_hide, layer='master')

    add "gui/game_menu/frame_menu.png" xpos 785 ypos 311

    vbox:
        xpos 811
        ypos 337
        spacing 2

        imagebutton:
            idle "gui/game_menu/Setting_menu_in_game.png"
            hover "gui/game_menu/hover_Setting_menu_in_game.png"

            action ShowMenu("preferences")

        imagebutton:
            idle "gui/game_menu/Exit to menu in game.png"
            hover "gui/game_menu/hover_Exit to menu in game.png"

            action MainMenu()

        imagebutton:
            idle "gui/game_menu/exit to desktop.png"
            hover "gui/game_menu/hover_exit to desktop.png"

            action Quit()

    imagebutton:
        idle "gui/game_menu/setting.png"
        hover "gui/game_menu/hover_setting.png"

        action ShowMenu("preferences")
        xpos 1859
        ypos 16

screen credit():
    tag menu
    add "gui/bg.png"

    text "Credits" size 50 font "gui/fonts/Satisfy-Regular.ttf" color "#383838" xalign 0.5 ypos 60

    vpgrid:
        xysize (1538, 714)
        cols 1
        draggable True
        mousewheel True

        xpos 390#192
        ypos 164

        vbox:

            text "Publisher" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Playway" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Supervisors" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Tomasz Sosnowski and Maria Koz??owska of Hyper Studio" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Creative Director and Writer" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Anna ???Lavinnia??? Ko??czak of Transparent Games" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Editor" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Eleanor Anwen" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Artists" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Paulina ???Nokari??? Janusz" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Yui" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Joanna Moskwa" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Adam Biszewski" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Mariam Babunashvili" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "UI/UX Designer, Graphic Designer" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Mateusz Mazur" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Trailer" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Dan Stan" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Music" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Geoff Moore" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Sound Design" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Julia Konarczak" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Game Design" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Piotr Osi??ski" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "M. Sal" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Programmers" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Dipesh Aggarwal" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Ana Nguyen" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            null height 20
            text "Voice Actors" color "#383838" size 30 bold True font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Catalina - Savy Des-Etages" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Valencia, Flockto - Ginger Sue" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Maximiano - Nick Chang" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Diedriech - Brandon P. Jenkins" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Edmundo - Juwan Royal" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "The Oracle - Josh Portillo" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Lumberjack, Trailer Narrator, Animal Sounds - Rob Schwarb" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Graciella, Flockto???s Owner - Jenna Rose Geiser" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Wonsh???s Owner, Extra - Ty Coker" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            text "Lemurin???s Owner - Shakyra Dunn" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5


    imagebutton:
        idle "gui/history/Back to menu.png"
        hover "gui/history/hover_Back to menu.png"

        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action Return()
        xpos 879
        ypos 903

screen help():
    tag menu
    add "gui/bg.png"

    text "Help" size 50 font "gui/fonts/Satisfy-Regular.ttf" color "#383838" xalign 0.5 ypos 60

    imagebutton:
        idle "gui/history/Back to menu.png"
        hover "gui/history/hover_Back to menu.png"

        hovered Play("sound", "audio/sfx/mouse_hover.ogg")
        action Return()
        xpos 879
        ypos 903

    vpgrid:
        xysize (1538, 714)
        cols 1
        draggable True
        mousewheel True

        xpos 390#192
        ypos 164

        vbox:
            spacing 10
            xsize 1100
            xalign 0.5

            text "Keyboard" color "#383838" size 40 font "gui/fonts/OpenSans-SemiBold.ttf" xalign 0.5
            hbox:
                label _("Enter ")
                text _("Advances dialogue and activates the interface.")

            hbox:
                label _("Space ")
                text _("Advances dialogue without selecting choices.")

            hbox:
                label _("Arrow Keys ")
                text _("Navigate the interface.")

            hbox:
                label _("Escape ")
                text _("Accesses the game menu.")

            hbox:
                label _("Ctrl ")
                text _("Skips dialogue while held down.")

            hbox:
                label _("Tab ")
                text _("Toggles dialogue skipping.")

            hbox:
                label _("Page Up ")
                text _("Rolls back to earlier dialogue.")

            hbox:
                label _("Page Down ")
                text _("Rolls forward to later dialogue.")

            hbox:
                label "H "
                text _("Hides the user interface.")

            hbox:
                label "S "
                text _("Takes a screenshot.")

            hbox:
                label "V "
                text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

            hbox:
                label "Shift+A "
                text _("Opens the accessibility menu.")
