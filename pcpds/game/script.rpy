transform ease(start, end, time):
    subpixel True
    start
    easein time end

define dis = { "master" : Dissolve(0.5) }
transform ease(start, end, time):
    subpixel True
    start
    easein time end

label start:
    #jump credits
    ### Scene 1 ###
    stop music fadeout 1
    $renpy.pause(1)
    play music homemorning
    "Wow. My first day at PCP University!"
    "My last school threw me out for being too retarded and not being able to finish my assignments."
    "Will this place be any better? Who knows, I might finally find some friends or even …Love?"

    scene way2scl
    with fade
    pause 1.0

    "A cool breeze greets me this morning."

    "As I pass by the entrance to a dinky alley on my way to campus, a slim guy with fluffy hair nearly walks straight into me."

    show hippo campushandsup campusshock1
    with dis
    with vpunch

    show hippo
    with dis
    Hippo "Oh whoops, I didn't see you there. Are you on your way to school too?"

    "\"Too\"? He's a student then?"

    "You" "Yeah, PCP University. Do you go there?"

    $ Hippo = Character("{color=#61ffe0}Hippo{/color}", what_color = "#61ffe0", image = "hippo")
    show hippo
    with dis
    Hippo campusgrabby campushappy2 "Well given how it’s the only school in the city, yeah. Oh uh, the name's Hippo by the way."

    python:
        player_name = renpy.input("Oh my name's uhhhhhhhhh\n(say something cool and hit enter, bitch)")
        player_name = player_name.strip()

        if not player_name:
            nameFlag = True
            player_name = "Li'l Shit"
        else:
            nameFlag = False
    if nameFlag:
        "You" "Uhhh... Lil..."
        "Wait that's not a cool name!"
        "You" "Lil... Li'l... [player_name]."
        show hippo
        with dis
        Hippo campusgrabby campusconfused2 "[player_name]?"
        "God, I'm so retarded."
        "You" "...Y-yeah."
        "I desperately try to change the topic."
    else:
        "You" "I’m [player_name]!"
    "You" "But, aren't you going the wrong way? I’m new to Boston, but I thought the university was...
        wait shit, maybe I was looking at the Newgle Maps app upside-down..."

    show hippo
    with dis
    Hippo campusstanding campushappy1 "Well yeah, it is over that way, if you wanna take the main roads. But I like this shortcut through the alleyways.
        Actually, you wanna walk with me? I could show you around the neighbourhood and tell you about the school and stuff."

    "I fail to see how backtracking through the alleys is a shortcut. But this guy seems friendly enough, and I set out early on
        purpose. Eh, what's the harm?"

    "You" "Sure! We can get to know each other too. Maybe we're in some of the same classes! So, what do you study...?"

    show hippo at ease(left, offscreenleft, 1.0)
    with Dissolve(0.5)
    "As we walk and talk we both learn that we have the same class schedule for today, so he offers to show me around campus."
    "At this point though I’m worried we won't make it without being mugged, this place definitely doesn’t seem safe. I swear I saw
        a disheveled man lurking in the shado-"
    hide hippo

    scene way2sclwjs
    with Dissolve(1.0)
    pause 1.0

    "Ah!"

    "There he is! What's he doing crouching over a manhole cover?"

    "He screams desperately into the sewers."

    Jesse "DONATELLO! Come back to me! Come on, dude!"

    "You" "Is... is that guy okay, Hippo?"

    $ Jesse = Character("{color=#ffe300}Sewer Priest{/color}", what_color = "#ffe300")
    show hippo campushandsup at ease(offscreenleft, left, 1.0)
    with dis
    Hippo "Oh don't mind the Sewer Priest, he's always like that."

    show hippo at ease(left, offscreenleft, 1.0)
    with Dissolve(0.5)
    "I take Hippo at his word and turn my attention away from the loud ‘Priest’. I can't help but feel sorry for him though, if this
        is normal. The government should do something about the homeless."
    hide hippo
    "As the alleyway opens back up, I see the silhouette of the University peeking out from behind the houses, etching its bizarre shape
        into the skyline."

    scene uniout
    with Dissolve(3)

    show hippo campusclenched campushappy2 at ease(offscreenleft, center, 1.0)
    with dis
    "Hippo:" "Anyways, welcome to PCP University!"

    show hippo at ease(center, offscreenright, 1.0)
    with dis
    $renpy.pause(5.0)
    hide hippo

    jump morningClassDayOne
