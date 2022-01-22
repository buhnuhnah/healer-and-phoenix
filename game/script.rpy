transform shake_screen:
    linear 0.1 xoffset -2 yoffset 2
    linear 0.1 xoffset 3 yoffset -3
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0

label start1:
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    "Text"

    # These display lines of dialogue.
    jump tutorial

    call screen minigame(graciella_purrbear)
    call screen minigame(wonsh)
    call screen minigame(flocto)
    call screen minigame(lemurin)
    call screen minigame(phoenix)
    call screen minigame(phoenix_2)

    d "You've created a new Ren'Py game."

    d "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "1":
            pass
        "Hey you":
            pass
    c "Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world!"
    m "Once you add a story, pictures, and music, you can release it to the world!"
    v "Once you add a story, pictures, and music, you can release it to the world!"
    m "Once you add a story, pictures, and music, you can release it to the world!"
    v "Once you add a story, pictures, and music, you can release it to the world!"
    m "Once you add a story, pictures, and music, you can release it to the world!"
    v "Once you add a story, pictures, and music, you can release it to the world!"
    m "Once you add a story, pictures, and music, you can release it to the world!"
    v "Once you add a story, pictures, and music, you can release it to the world!"
    m "Once you add a story, pictures, and music, you can release it to the world!"
    v "Once you add a story, pictures, and music, you can release it to the world!"
    e "Once you add a story, pictures, and music, you can release it to the world!"
    e "Once you add a story, pictures, and music, you can release it to the world!"
    e "Once you add a story, pictures, and music, you can release it to the world!"
    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
