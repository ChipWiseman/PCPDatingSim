

label morningClassDayOne:
    ### Scene 2 ###
    play music memeclass3
    scene hall1ant
    with Fade(3.0,0.0,1.0)
    pause 1.0
    show hippo at ease(offscreenright, right, 1.0)
    #with dis
    "Hippo and I wander the halls of the university. Hippo seems to know where he is going, but I feel completely lost. Suddenly a
        powerful voice booms from behind us."

    #nate silhouete
    Nate "Hello puny students!"

    show nate at ease(offscreenleft, left, 1.0)
    with dis
    Nate campuspapers campushappy1 glasses "Oh, I haven’t seen you around before. Are you new here?"

    "You:" "Yeah, this is my first day here."

    Nate "Hello and welcome to The Pro Crastinators… University! First up, just know that if you aren’t willing to put in the effort
        to succeed at this school, I WILL end you. So tell me..."

    show nate campusstanding campusangry1:
        yalign 0.01
        xalign 0.0
        ease .5 zoom 1.5
    with Dissolve(0.5)
    show hippo at ease(right, offscreenright, 1.0)
    with dis
    "The man steps closer to me. All of a sudden his once captivating muscles become intimidating, and his voice shifts to a serious tone."

    show nate
    with dis
    Nate campusangry2 "Do you plan to excel at this university? As a teacher, I want to see all my students become the greatest version of
    themselves. And I will do everything in my power to see that through to the end."
    hide hippo

    "I suddenly find myself having flashbacks to my last school. I cannot help but remember all the unfinished homework assignments,
        all the failed tests..."

    "You:" "Uhh… Yeah…"

    show nate campuspapers campussad1:
        yalign 1
        xalign 0.0
        ease .5 zoom 1
    with dis
    Nate "You don’t sound so sure of yourself. Oh well, just know that if you fail to meet standards I will not hesitate to take
        action. I HAVE principles!"

    "Great…"

    show ag campusb campussad at ease(offscreenright, right, 1.0)
    with Dissolve(0.5)
    "A cool looking giraffe catches the teachers attention."

    show nate
    with dis
    Nate campusstanding campusshock1 "Oh hey Action Giraffe, how’s it going?"

    show ag
    with dis
    AG campusa campushappy "I have AIDS."

    show nate
    with dis
    Nate campussmoking campushappy1 "Yeah, it’s pretty inspirational that despite your disease, you still strive towards your dreams."

    show nate
    with dis
    Nate campuspointing campushappy2 "See, new guy? Be more like Action Giraffe here and realize your dreams to their fullest. I won’t accept anything less."

    show nate at ease(left, offscreenleft, 1.0)
    with dis


    "You:" "Who was that?"
    hide nate

    show ag at ease (right,left,1.0)
    with Dissolve(.5)
    show hippo campusgrabby campushappy2 at ease(offscreenright, right,1.0)
    with dis

    $ Nate = Character("{color=#7bff00}Professor Bestman{/color}", what_color = "#7bff00", image = "nate")
    Hippo "That was Professor Bestman, he teaches the Memes and Philosophy classes."

    #maybe the player should note how they felt in his presence?
    "You:" "Those sure sound interesting. And the giraffe?"

    Hippo "That’s Action Giraffe. He’s just reaaaally cool."

    "Hippo turns to Action Giraffe."

    show hippo
    with dis
    Hippo campushandsup campusneutral "Hey AG, what class do you have first?"

    show ag
    with dis
    AG campusc campusshock "I have AIDS."

    show hippo
    with dis
    Hippo campusstanding campushappy2 "Hey, what a coincidence! We all start the day with the same class."

    "You:" "Wait, is ‘AIDS’ a class? I thought we had Music..."

    show hippo
    with dis
    Hippo campusgrabby campusshock1 "Hm? What was that?"

    "You:" "Uhh, nevermind…"

    scene digifull
    with fade
    $ renpy.pause (1.0)

    scene digiback
    show digifront:
        xalign 1.0
        yalign 1.0

    "We reach the music classroom. Hippo and I sit down adjacent to one another. A scruffy man enters the room, obviously drunk."

    show digi campushappy3 behind digifront at ease(offscreenright, center, 1.0)
    with dis
    Digibro "Heyyy everybody! Welcome to Music Class!"

    $ Digibro = Character("{color=#ff007d}Professor Digibro{/color}", what_color = "#ff007d", image = "digi")
    show digi
    with dis
    Digibro "I’m Professor Digibro, and well, I have no plan for this lesson whatsoever. But I guess you’re all here for the
        authentic After Dark experience, so LET’S GOOOOO!"

    "The Professor takes an elongated swig of his beverage then slams it down on his desk."
    show digi
    with dis
    Digibro campusstanding campushappy3 "As you all know, I am one of the progenitors of the cyberpunk horrorcore rap genre. Can anyone here tell me what
        that means?"

    "As is to be expected, no one was paying enough attention to raise their hand."

    show digi
    with dis
    Digibro campusleaning campusangry1 "Speak up, pussies! I’ll just call on someone. Let’s see …"

    "Professor Digibro scans the room tentatively."
    show digi
    with dis
    Digibro campusstanding campushappy2 "You, the cool looking one with the sunglasses."

    show ag campusb campusshock at ease(offscreenleft, left, 1.0)
    with dis

    AG "I have AIDS."

    show digi campusconfused1
    with Dissolve(0.5)
    "Digibro rubs his chin, deep in thought."

    Digibro "Hmm… I guess that’s a pretty good way to describe my music."

    show ag at ease(left, offscreenleft, 1.0)
    with dis

    show digi
    with dis
    Digibro campusshrugging campushappy1 "Anyway, I’ve listed my bandcamp in the course outline sheet, so I highly recommend y’all check it out."
    hide ag

    show digi
    with dis
    Digibro campusstanding campusconfused1  "Hopefully you’ve all heard of Sturgeon’s Revelation, but for those of you who remain uninformed, it states that 90
        percent of everything is crap. Luckily, I consider my music to be in that gifted 10 percent..."

    "Professor Digibro went on and on for what felt like hours. Most of what he was saying didn’t even seem like it was about music."
    "All he talked about was anime soundtrack composers, youtube marketing and being an autistic \"Devilman.\" I soon find my
        mind drifting off…"

    scene black
    with Fade(3.0,0.0,0.0)
    $ renpy.pause (3)

    Digibro "Hey! Hey you. New kid."

    scene digifull
    with fade
    $ renpy.pause (0.5)

    scene digiback
    show digifront:
        xalign 1.0
        yalign 1.0
    show digi campusleaning campusconfused2 behind digifront

    "I snap back to reality. Great. It’s my first day and I’m already zoning out in class."

    show digi
    with dis
    Digibro "Are you getting any of this?"

    "You:" "Yeah. Music and stuff right?"

    show digi
    with dis
    Digibro campusstanding campushappy3 "Good. There’s gonna be a quiz on all that stuff I just told you next Friday. Your homework is to watch ten Anthony Fantano
        videos. Class dismissed."

    show digi
    with dis
    Digibro campuspeace campusneutral "See you in the next one!"

    hide digi
    with dis

    menu:
        "Finally class is over. Hmm… Looks like I have a few minutes before lunch. Who should I talk to?"

        "Talk to Digi.":
            jump scene2Digi
        "Talk to Hippo.":
            jump scene2Hippo

label scene2Digi:
    "I approach Digi. The closer I get to him, the more details I can see of his slovenly yet strangely handsome appearance. He looks a
        bit like Jesus, in a way."

    show digi campusstanding behind digifront
    with dis
    Digibro campushappy1 "Oh, hey new kid, how do you like the class so far? I hope you enjoyed the subject, because you’re going to be hearing a
        lot more about it."

    "You:" "Yeah it was… interesting."

    show digi
    with dis
    Digibro campushappy3 "Well if you found that interesting you’re really going to like those Fantano videos I assigned you for homework. You
        know, it’s nice to have someone who actually takes interest in my class."

    show digi
    with dis
    Digibro campusangry2 "Some people say I ‘unnecessarily insert my opinion into things.’ I don’t really see the point of ‘objective’ teaching
        to begin with."

    show digi
    with dis
    Digibro campusfolded campushappy1 "Anyway, I’ve got motherfuckin’ shit to do that’s bigger than yo’ kiddie pool. If you want to talk more, I’ll be in the
        library after school. Nice meeting ya, new kid."

    show digi at ease(center, offscreenright, 1.0)
    with dis

    "At first I thought Digi was a self centered guy, but now that I’ve talked to him, I’m starting to realize that he’s pretty sweet.
        I think I’ll enjoy this class."
    hide digi

    show hippo campusstanding campusneutral behind digifront at ease(offscreenleft, center, 1.0)
    with dis
    Hippo "It’s getting pretty close to lunch, we should get going."

    "You:" "Sure thing, lets go."
    show hippo campusstanding campusneutral behind digifront at ease(center, offscreenright, 1.0)
    with dis

    jump breakDayOne

label scene2Hippo:

    show hippo campusstanding campusneutral behind digifront at ease(offscreenright, center, 1.0)
    with dis
    Hippo "So how did you feel about your first class here?"

    "You:" "Well, it was… interesting."

    show hippo
    with dis
    Hippo campushandsup campushappy1 "Yeah, most people tend to feel that way at first. But don’t worry about it. You’ll warm up to the folk here eventually.
        They’re like prickly pears: hard on the outside, but if you crack ‘em open they’re full of juicy red bits."

    show hippo
    with dis
    Hippo campusgrabby campusconfused1 "If you wanna know more about Professor Digibro, he usually hangs out in the library after school. I dunno what he actually
        does there though."

    show hippo
    with dis
    Hippo campusstanding campusneutral"Anyway, it’s getting pretty close to lunch, we should get going."

    show hippo campusstanding campusneutral behind digifront at ease(center, offscreenright, 1.0)
    with dis

    "I was kind of afraid of this whole university thing at first. It’s good to know that someone as nice as Hippo is here. I think I’ll
    enjoy my time in this place after all."

    hide hippo
    with dis

    jump breakDayOne
