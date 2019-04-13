label artClassDayOne:
    ### Scene #4 ###

    show hippo campusclenched campushappy2
    with dis
    Hippo "Art Class! I reeaally like art, and the Professor’s pretty fun too."
    stop music

    play music memeclass1
    scene munchyclass
    with fade
    pause .5

    show hippo campusstanding campushappy1 at ease(offscreenleft, left, 1.0)
    with Dissolve(0.5)
    show mage campus3 campushappy1 at ease(offscreenright, right, 1.0)
    with dis
    Mage "Hey Hippo! Hellew… eh… what was your name again?"

    if nameFlag:
        "You" "Oh yea, we never exchanged names. I’m..."
        "Oh no."

        show hippo
        with dis
        Hippo campusstanding campusconfused1 "[player_name], right?"

        show hippo
        with dis
        Hippo campusstanding campushappy1 "His mind trails off sometimes."
        "You" "Y-yeah... "

        show mage
        with dis
        Mage campus5 campusconfused1 "Ah... I See."
    else:
        "You" "Oh yea, we never exchanged names. I’m [player_name]! What should I call you, m'lady?"
        show mage
        with dis
        Mage campus5 campusangry1 "Please don’t do the \"m'lady\" thing… ever again."

    $ Mage = Character("{color=#d052ff}Mage{/color}", what_color = "#d052ff", image = "mage")
    show mage
    with dis
    Mage campus5 campushappy2 "I’m Lethal Aurora Mage, but you can call me Mage, just Mage. Some people call me \"Mom\" or \"Bro\", or both."

    show mage
    with dis
    Mage campus4 campusconfused1 "I really wonder how that happened …"

    show hippo at ease(left, offscreenleft, 1.0)
    with Dissolve(0.5)
    show mage at ease(right, offscreenright ,1.0)
    with Dissolve(0.5)
    scene munchyclass
    with vpunch
    "Before I was able to quip on how she might be a dude or something, the door to the classroom bursts open."

    show munchy campusstanding campusangry2 at ease(offscreenright, center, 1.0)
    with dis
    Munchy "HELLO CHILDREN! Listen! You may not know who I am, but you’re gonna find out WAY MORE, than you’ve ever DREAMED of knowing!"

    show munchy
    with dis
    Munchy campuscrossing campushappy3  "I’m gonna introduce you to the holy arts, BECAUSE"

    show munchy
    with dis
    Munchy campuscrossing campushappy2 "IF YOU HAVEN'T FIGURED IT OUT YET,"

    $ Munchy = Character("{color=#ff80d4}Professor Tinyhats{/color}", what_color = "#ff80d4", image = "munchy")
    show munchy
    with dis
    Munchy campussquatting squattingangry3 "I AM PROFESSOR TINYHATS VON MUNCHAUSEN, THIS IS THE ART CLASS - and there are exactly TWO artforms! Everything else is not
        art!"

    show munchy
    with dis
    Munchy campuscrossing campusangry1 "Books? Not art! Don’t even have pictures!"

    show munchy
    with dis
    Munchy campuscrossing campusangry2 "Music? Pretty okay I guess, but not REAL ART!"

    show munchy
    with dis
    Munchy campussquatting squattingangry3 "The first art form is DRAWING!"

    show munchy
    with dis
    Munchy campuscrossing campushappy3 "It’s pretty cool, I know. The only humans worth something, are the ones that can DRAW! Especially drawing quickly.
        Y’know like a real-ass cowboyyy!"

    "What’s that’s supposed to even mean!?"

    show munchy
    with dis
    Munchy campusstanding campushappy2 "I’ll be your mentor. Because having a great teacher is obviously better than not going to school and trying to learn
        everything by yourself! This is why I was educated here, in the PCP University, AND LOOK WHERE I AM NOW!"

    show munchy
    with dis
    Munchy campuscrossing campushappy3 "But let’s get to the second of the REAL ARTforms! Any guesses?"

    show munchy campuscrossing campushappy3 at ease(center, right, 1.0)
    with Dissolve(0.5)
    show mage campus4 campusneutral at ease(offscreenleft, left, 1.0)
    with dis
    Mage "Ahem… animation?"

    show munchy campussquatting squattingangry3 at ease(right, center, 1.0)
    with dis
    show mage campus5 campussad1 at ease(left, offscreenleft, 1.0)
    Munchy "WRONG! That WAS WRONG Mage! Animation is simply the exact SAME THING AS DRAWING, BUT MORE! Try
        better next time!"
    hide mage
    show munchy
    with dis
    Munchy campussquatting squattingangry3 "You IDIOTS I’m talking about COOKING! THE ANCIENT ART OF COOKING, TAUGHT TO OUR SPECIES BY THE GREATEST DUDE, Thoth
        HIMSELF, SIX THOUSAND YEARS AGO! COOKING IS SO MUCH OLDER THAN DRAWING; YOU CAN’T EVEN IMAGINE!"

    show munchy at ease(center, right, 1.0)
    with Dissolve(0.5)
    show tom campus1 campusangry2 at ease(offscreenleft, left, 1.0)
    with dis
    #I have a suggestion for alternative dialogue, cause this seems a bit stiff to me
    #"Fuck this shit! Cooking isn't art! It's a humancore meme that I REFUSE to associate with!"
    Tom "Fuck this shit. Cooking is too humancore for me."

    #Same
    #"What? Do you not cook your food?"
    "You" "What do you mean by that? I like cooked food."

    show munchy campusstanding campusangry3
    with Dissolve(0.5)
    #Feels like an "even" should be thrown between "can't" and "afford"
    show tom
    with dis
    Tom campusangry1 "If you ever have to live in a car for months, cooking takes you nowhere. How am I supposed to use Prof. Tinyhats’ recipes
        if I can’t afford the ingredients?"

    show tom
    with dis
    #I kinda wanna make this a skit where he actually makes a case for huel in an ad-like fashion
    Tom campusneutral "Huel is the perfect posthuman solution for all my nutritional needs. Hashtag not an ad, and all that."

    #Feel like this would be confusing without dialogue, should probably have munchy screaming "GET THE FUCK OUTA HERE"

    show munchy campussquatting squattingangry3 at ease(right, left, 1.0)
    with Dissolve(0.5)
    show tom campusangry2 at ease(left, offscreenleft, 1.0)
    with Dissolve(0.5)
    show munchy at ease(left, offscreenleft, 1.0)
    with Dissolve(0.5)
    show munchy at ease(offscreenleft, right, 1.5)
    with Dissolve(0.5)
    show mage campus3 campusangry1 at ease(offscreenleft, left, 1.0)
    with dis
    Mage "That’s mean! Just throwing him out like that ..."

    hide tom
    #"like" between "not" and "suicidal"
    "You" "Yeah, that was harsh. Hope he’s not suicidal or anything."

    show mage
    with dis
    Mage campus2 campushappy2 "Well, I’m still happy about the theme of this class. I’m not a great cook, but I just love flipping veggies!"

    show munchy
    with dis
    Munchy campussquatting squattinghappy3 "AND YOU’LL GET ENOUGH VEGGIES TO FLIP, MAGE!"

    show munchy
    with dis
    Munchy campuscrossing campusangry2 "We’re gonna do all the handmade shit here! Handmade pasta! Roll your own
        dough! YOU’RE GONNA COOK YOUR OWN DOUGH!"

    show munchy
    with dis
    Munchy campushappy3 "Rustic and authentic, like a real Italian boy! You know what the sacred white sauce
        is called?"

    show mage at ease(left, offscreenleft, 1.0)
    with Dissolve(1.0)
    #Feel like player should comment on how quickly Tom was forgotten
    show munchy
    with dis
    Munchy campussquatting squattingangry2 "YOU! New one! Answer my question!"

    "You" "I can barely understand what you are trying to tell me."

    show munchy
    with dis
    Munchy campussquatting squattingangry3 "ARE YOU FUCKING KIDDING ME! Wait a second."

    show munchy
    with dis
    with vpunch
    Munchy "THOTH! THOTH! THOTH! THOTH! THOTH! THOTH!"

    scene munchyclass
    with vpunch
    show munchy at right
    with Dissolve(0.5)

    show thoth at center
    with dis
    Thoth "What can I do for you, my dear Lemurians? Do you need my help again?"

    show munchy campuscrossing campusangry1
    with dis
    Munchy "These dumbfuck lowly pussies don’t have the Christ Consciousness to comprehend what I am saying! Can you do something
        about it buddy?"

    Thoth "Do not worry. I can manipulate their 4th-dimensional molecules and raise them to level 3!"

    show munchy
    with dis
    Munchy campusstanding campushappy1 "Much appreciated Thoth!"

    hide thoth
    with Dissolve(0.5)
    "You" "Wh… what was that?"

    show hippo campusstanding campushappy2 at ease(offscreenleft, left, 1.0)
    with dis
    Hippo "That was Thoth. He…"

    show hippo
    with dis
    Hippo campusstanding campusconfused1 "Actually I don’t know what his deal is."

    show hippo at ease(left, offscreenleft, 1.0)
    with Dissolve(0.5)

    show munchy at ease(right, center, 1.0)
    with dis
    Munchy campussquatting squattinghappy3 "THOTH! THOTH! THOTH! THOTH! THOTH! THOTH!"

    show munchy
    with dis
    Munchy campuscrossing campushappy2 "Are your chakras balanced now? Can we continue? Good!"

    "This incomprehensible talk of the flow of consciousness went on for another hour. I did not feel like I learned anything,
        but at the same time I felt strangely enlightened."

    "What a bizarre guy..."

    show munchy at ease(right, center, 1.0)
    with dis
    Munchy campuscrossing campushappy3 "So, my dear students! We arrived at the end of our journey! For now! FOR TODAY!  BUT DON’T WORRY, MY SWEET FELLOWS!
        WE WILL MEET AGAIN! Sooner than you think!"

    "You" "What is that supposed to mean?"

    show munchy
    with dis
    Munchy campuscrossing campussmitten1 "To all the new students: You can meet me in a EXCLUSIVE PRIVATE TUTORING! This afternoon! At the 7 Eleven down the street!"

    "You" "Wait, aren’t I the only new student here? Not sure if that’s a good idea."

    show munchy
    with dis
    Munchy campusstanding campushappy1 "I will be there anyways! The whole afternoon! Just come over, it’s impossible to miss me."

    show munchy at ease(center, offscreenright, 1.0)
    with Dissolve(0.5)
    "The professor bursts out the door in short order. I guess class is dismissed?"

    stop music

    scene uniout
    with fade
    play music homenight

    show hippo campuspress campushappy1 at ease(offscreenright, right, 1.0)
    with dis
    Hippo "And? What do you think?"

    "You" "That …. certainly was something."

    show hippo
    with dis
    Hippo campushandsup campushappy2 "Yeh. You’ll soon learn how to survive in this university. But for now, have yourself a chill afternoon."

    "You" "Thanks for all your help showing me around school. That was really nice, Hippo."
    show hippo
    with dis
    Hippo campusstanding campussmitten1 blushies "Ohh its nothing. ‘Til tomorrow, [player_name]!"

    show hippo at ease(right, offscreenleft, 1.0)
    with Dissolve(0.5)
    "I bid Hippo farewell."
    hide hippo

    jump scene5
