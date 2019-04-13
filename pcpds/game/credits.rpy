label credits:
    scene grey
    with Fade(3.0,0.5,1.5)

    play music cred
    $ credits_speed = 130
    show creditsimage2:
        xpos 0
        ypos 1080
        linear credits_speed xpos 0 ypos -6550
    pause(credits_speed)
    $ renpy.pause()
    stop music fadeout 5.0
    scene black
    with Fade(5.0,0,0)
    "See you again in Fall 2019."
    return
