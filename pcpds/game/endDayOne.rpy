label endDayOne:
    ### Scene #6 ###
    stop music fadeout 3.0
    scene homenight
    with fade
    play music homenight fadein 1.0
    pause .5

    "Finally home. What an exhausting day!"
    "Not that it was a particularly bad day, au contraire."
    "I experienced a lot of pretty exciting things."

    "I had my doubts about this new school, this new city, questioned if it was the right choice to come here."

    "But I don’t regret it. The subjects in this university actually interested me, and the professors show real passion and excitement!"

    stop music fadeout 1.5
    scene bathroom
    with fade

    "I already found new friends. And maybe one of these friendships could become something more …"

    "Maybe I finally found the place where I belong."

    play music toilet noloop
    scene bathroommirror1
    with Dissolve(0.5)
    $ renpy.pause(3)

    scene bathroommirror2
    with Dissolve(0.5)

    "PCP Guy" "God I look horrible."

    jump credits
