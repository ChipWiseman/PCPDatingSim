label scene5:
    menu:
        "Hmm, now what? School is done, so where should I spend the afternoon?"

        "Go to 7/11.":
            jump scene5Munchy
        "Go to the city park.":
            jump scene5Hippo
        "Go to the school library.":
            jump scene5Digi

label scene5Digi:
    ### Scene #5A ###

    play music lib
    scene library
    with fade
    pause .5

    "I enter the library, and am immediately overwhelmed by rows of books, manga, and games as far as the eye can see. But all of these
        forms of media mean nothing to me, I immediately find the aisle that is far more familiar; light novels."

    "I peruse the books for a bit before one catches my eye. It’s titled ‘The Asterisk War.’ I begin reading the book on the spot and soon
        get really invested in it, but then suddenly am overwhelmed by the scent of weed looming over me."

    show digi casualleaning casualhappy1 at ease(offscreenright, center, 1.0)
    with dis
    Digibro "Watcha reading?"

    "My eyes start burning as Professor Digibro takes a hit of his dab pen and proceeds to exhale marijuana smoke directly onto my face."
    "Wait, don't dab pens use vapor? How pure does this dank kush have to be that vapor burns my eyes?"
    "Once the cloud clears, I catch a glimpse of them; Digi’s titillating round sunglasses."

    "You" "Is smoking allowed in here?"

    show digi
    with dis
    Digibro casualshrugging casualhappy3 "I don’t give a fuck whether it is or not."

    show digi
    with dis
    Digibro "The professor snatches the book out of my hands. He looks the novel over and almost immediately winces in disgust."

    show digi
    with dis
    Digibro casualleaning casualblush3 "The Asterisk War fucking sucks. I can’t believe someone as cool as you would consume such garbage."

    "Digibro tosses ‘The Asterisk War’ away with such veracity that, upon colliding with the wall, it disintegrates instantly. He pulls
        another light novel out of his pocket, which I failed to notice due to the immense bagginess and spaciousness of his robe."

    show digi
    with dis
    Digibro casualpeace casualblush1 "Here, try this!"

    "Digibro shoves the small book into my arms. For a brief moment, I feel Digi’s soft tender skin brushing up against mine. I look this
        new light novel over. It is titled, \"Boogiepop and Others\""

    show digi
    with dis
    Digibro casualstanding casualhappy3 "Boogiepop and Others is really fuckin good, it’s easily my favorite Light Novel! You’re lucky I got here in time before
        you were subjected to the utter garbage that is Ass War. Here, sit down with me."

    show digi at center:
        ypos 1280
    with Dissolve(.5)

    "We sit down between the stuffed bookshelves, and Digi motions for me to read the Light Novel he gave me. He pulls out what appears
        to be a manga and starts reading it."

    "You" "So, what do you exactly do in here anyways?"

    show digi
    with dis
    Digibro casualshrugging casualhappy1 "Eh, whatever I feel like doing. Today I’m researching some new doujins for my good friend, the Hentai Samurai."

    "You" "Who is that?"

    show digi
    with dis
    Digibro casualstanding casualconfused1 "You’ve never heard of the Hentai Samurai? He reviews all the best 10/10 hentai. Just search him up on your favourite
        porn site!"

    show digi
    with dis
    Digibro casualstanding casualhappy1 "Anyways, you should start reading this book."

    "You" "Which book?"

    show digi
    with dis
    Digibro casualleaning casualangry1 "This book. This book!"

    "You" "Boogiepop and Others?"

    show digi
    with dis
    Digibro casualleaning casualblush2 "I think the audience knows what kinda book I’m talking about."

    "You" "What audience? What are you talking about?"

    show digi
    with dis
    Digibro casualshrugging casualangry2 "THIS BOOK. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book? This book. This book. This book. This book. This book. This book. This book ... This book. This book. This book. This book. This book. This book. This boOK. This book. This book. THIS book. This boooook. This book. This book. This book, This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book?! This book. This book. This book. This book! This book!. This book. THIS BOOK. This book. This book. This book. This book. This book. This book .... This book. This book. This book. This book. This book. This book. This book. This book. This book. THIS book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book! This book. This book. This book. This book. This book. This book. This BOOK. This book. This book. This book. This book. This book. This book. This b o o k. This book. This book. This BooK. This book. This book? This book. This book. This book. This book. This book. This book. This book. This book. This book. This book. This book!! This book. This book … This book. This book. This book. This book; This book. Thissss book. This book. This book. This book. This book! This book. This book. This book. This book. This book. This book. This book. This book!? This book, This book. This book. This book. This book? This book. This book. This book. T h i s book. This book. This book. This book. This book ... This book. This book. This book ..."

    "Utterly confused by what’s going on I just begin reading Boogiepop, and after a while Digi finally stops. He’s now just watching me
        as I slowly turn the pages, which doesn’t feel as creepy as I thought it would."
    "After finishing a chapter Digi speaks up."

    show digi
    with dis
    Digibro casualstanding casualneutral "So, what do you think of Boogiepop and Others?"

    menu:
        "How should I react?"

        "It’s great, thanks for suggesting it to me!":
            jump scene5DigiApproves
        "It’s ok I guess, but I’d rather be reading The Asterisk War right now.":
            jump scene5DigiDisapproves

label scene5DigiApproves:
    show digi
    with dis
    Digibro casualstanding casualblush1 "R-really? It’s pretty dense on your first read, I’m glad you liked it."

    show digi
    with dis
    Digibro casualstanding casualhappy1 "I was thinking that maybe you and I could hang again sometime. I… I could recommend you some more books… an…and maybe I
        could get to know you some more…"

    "My heart is pounding out of my chest. Have I finally found someone I can call a friend or maybe even… something more? I look Digi
        in the eyes and see my reflection in his sunglasses."

    "You" "Y… yeah, I’d like that."

    show digi
    with dis
    Digibro casualstanding casualblush1 "Good, I’m glad."

    "I feel myself being enraptured by the warmth in Digi’s smile. My face feels warm as it begins to redden like a tomato."

    "An awkward tension fills the air and we go back to reading for a few hours. We take occasional respites to discuss literature,
        but other than that, most of our time together was spent in silence."
    "But it’s strange. Even though we didn’t talk very much, I still relish in Digi’s company."

    "After reading, I decide that it is about time I should head home. I stand up to leave."

    show digi at center
    with dis
    Digibro casualleaning casualsad1 "You’re leaving already? Well, maybe we could hang out and read again sometime. I’ve been formulating a list of more
        books I think you would like."

    "You" "Yeah, that would be nice."

    show digi
    with dis
    Digibro casualpeace casualhappy3 "Good! I’ll make that list for the next time we hang out! Seeya later!"

    show digi at ease(center, offscreenleft, 1.0)
    with Dissolve(0.5)
    "I leave the library and head home, filled with a subtle satisfaction that I am getting to know more and more people at this new
        school in a more {i}intimate{/i} way."

    jump endDayOne

label scene5DigiDisapproves:
    #stop music
    show digi casualleaning casualangry3 at center
    with Dissolve(0.5)
    with vpunch
    "Digi lurches upward from his seat, snatching the book from my hands. I jump backwards, surprised."

    "You" "Are you okay?"

    show digi
    with dis
    Digibro casualfolded casualblush3 "I AM FUCKING NOT OKAY!"

    "Digi wields a slight smile so as to suggest that his anger is all in jest… or at least I hope that is the case."

    show digi
    with dis
    Digibro casualfolded casualhappy2 "How in the FUCK do you think that is passable in any way?"

    "Digibro pulls out another copy of ‘The Asterisk War’ off the bookshelf, flips to a random page, and shoves the book in my face while
        pointing at it."

    show digi
    with dis
    Digibro casualfolded casualhappy3 "Look at this shit! LOOK AT THIS SHIT! This is GARBAGIO! This is garbage! I can not believe that you are ok with this!
        This is a FUCKING PROBLEM!"

    "The Professor then takes a few deep breaths, almost as if he’s hyperventilating. He then immediately calms down, almost making me
        doubt he was even angry in the first place."

    #play music lib fadein 2.0
    show digi
    with dis
    Digibro casualpeace casualneutral "Well, see you next class."

    show digi at ease(center, offscreenleft, 1.0)
    with Dissolve(0.5)
    "Digi went from seething with rage to perfectly calm in a matter of moments. I’m not really sure of what to make of that. I wonder
        if I ruined my friendship with him…"

    "I check the clock. It is getting pretty late, so I decide to head home for the evening."

    jump endDayOne

label scene5Munchy:
    ### Scene #5B ###

    scene 711
    with fade
    play music work
    pause .5

    "Why did Prof. Tinyhats mention this place for a meeting? A 7 Eleven doesn’t seem like a place where anyone would want to spend their
        time."
    "This one in particular seems like a hot spot for homeless guys and losers. I wonder if that sewer guy from this morning
        hangs around here too."

    show munchy campuscrossing campushappy1 at ease(offscreenright, right, 1.0)
    with dis
    Munchy "Oh, there you are. I knew someone would come!"

    "You" "Hey Professor! So, what’s this private tutoring all about?"

    show munchy
    with dis
    Munchy campusstanding campushappy3 "Ahhh! Did I really call it private tutoring? Ok, well then, let me tutor you!"

    "The professor then suddenly lowers his voice to a whisper. He almost seems like a different person."

    show munchy
    with dis
    Munchy campuscrossing campusneutral "How much exactly do know about PCP University, little student?"

    "You" "Not much honestly. I did hear that it’s the only school in this city though."

    show munchy
    with dis
    Munchy "Don’t you think that’s weird? Such a big city with only one educational facility?"

    "You" "Should I be concerned about that?"

    show munchy
    with dis
    Munchy campusstanding campussad1 "No, no, but, keep your eyes open anyways. Nothing in the University is what it seems. The WAR, the gangs, all these wacky
        personalities… I think the whole plan is doomed to fail. The other professors don’t see it coming, but I certainly do."

    "You" "What \"plan\" are you talking about?"

    show munchy
    with dis
    Munchy campusstanding campusconfused1 "I'm not gonna say anything explicitly, but... I like you. Just take this as a little warning."

    "His words kinda concern me, but before I was able to ask for more information-"
    show 911 Standing at ease(offscreenleft, left, 1.0)
    with dis
    n11 "Sorry to crash into your little party here, but I’ve been ordered to tell you that you need to leave."

    show munchy
    with dis
    Munchy campussquatting squattinghappy3 "HEYYY! My favorite reality-distorting abstract character! What are you doing here!?"

    show 911 Pewpew
    with dis
    n11 "Hey my old friend! I’m working here now. Trying to save up for my own jet!"

    "You" "What do you need a jet for?"

    n11 "Uhh well lets just say it’s for a real BOOMing idea hahaha."

    show munchy
    with dis
    Munchy campussquatting squattinghappy2 "Hey did you know that I was born almost EXACTLY a year before you?"

    show 911 Concern
    with dis
    n11 "Well you never miss telling me that everytime we see each other on campus my dude!"

    show 911 Standing
    with dis
    n11 "You know what another annoying thing I also hear on campus, these rumours that Bush somehow “did” me. I am not THAT easy
        okay. Even though Bush is a handsome hunk of a man, I am in no way homosexually attracted-"

    show munchy
    with vpunch
    "???:" "YOU BETTER NOT BE TALKING SMACK ABOUT ME BEHIND MY BACK 9/11! QUIT FUCKING AROUND AND GET THE FUCK BACK IN HERE!"

    show munchy
    with dis
    Munchy campusstanding campusconfused2 "Wait… that voice… is that the 43rd president of the United States George W. Bush himself?!?!"

    $ n11 = Character("9/11", what_color = "#ffffff")
    show 911 Concern
    with dis
    n11 "Yeah. God knows how he ended up being my manager."

    "You" "Talk about a fall from grace. A manager of a 7 Eleven of all things!"

    show munchy
    with dis
    n11 "Hard times, I guess."

    show munchy
    with vpunch
    "Bush:" "WHERE THE FUCK ARE YOU 9/11?"

    show 911 Standing
    with dis
    n11 "Well, I better go now before Bush fucks me like he fucked this country."

    show 911 Boi
    with dis
    n11 "You should go too. Bush said I can’t allow loitering in front of the store. Real sorry 'bout that."

    show 911 Boi at ease(left, offscreenleft, 1.0)
    with Dissolve(0.5)

    show munchy campusstanding campushappy1
    with dis
    Munchy "It seems like our time here is over. You should go home now to get some of your important TWEEN HOURS!"

    show munchy
    with dis
    Munchy campusstanding campusangry1 "School starts early tomorrow, make sure to be on time. Professor Bestman hates it when someone is late!"

    "You" "Thanks for the advice, Professor Tinyhats!"

    $ Munchy = Character("{color=#ff80d4}Munchy{/color}", what_color = "#ff80d4", image = "munchy")
    Munchy campusstanding campussmitten1 "Ohhhh, you can call me Munchy now."

    $ Munchy = Character("{color=#ff80d4}Professor Munchy{/color}", what_color = "#ff80d4", image = "munchy")
    Munchy campussquatting squattingangry3 "PROFESSOR Munchy of course!"

    "You" "Uh, sure thing, Professor Munchy."

    show munchy
    with dis
    Munchy campusstanding campushappy1 "Atta boy. See ya later, and remember..."

    show munchy at ease(right, center, 0.5):
        yalign 0.01
        ease .5 zoom 1.5
    with dis
    Munchy campusstanding campusneutral "Nobody is safe."

    show munchy at ease(center, offscreenright, 1.0):
        yalign 1
        ease .5 zoom 1
    with dis
    "Munchy then walks away leaving me with those cryptic words, but before I can decipher them he vanishes into the darkness of the
        night. I look around me and decide to hurry back home before the homeless here try to mug me or something."


    jump endDayOne

label scene5Hippo:
    ### Scene #5C ###

    play music homenight
    scene park
    with fade
    pause .5

    "The park was quite further away from the school than I originally expected, so by the time I got here it was already sunset."
    "Unfortunately, the park itself is less exciting than I thought it would be, being mostly an empty field of grass and trees."
    "There is that purple forest looking area near the end of the walkway. Since it’s the only notable thing in the park, I make my
        way towards it."

    #(Background zooms in slightly and shakes up and down as PCP Guy is walking)

    #suggestion: mention Zen Huxtable?
    "However, it’s only a matter of time before boredom takes over, and like the filthy millennial I am I pull out my phone to check
        Twitter. I can't even enjoy a short walk in the park without social media consuming my every thought, how shameful."
    "Yet before I can even scroll past the usual stream of liked hentai posts, someone runs into me and we both fall over."

    show hippo campushandsup campussad2
    with dis
    with vpunch
    "After getting back up, I see a familiar cloud of hair in front of me."

    show hippo campusgrabby campussad2
    with dis
    Hippo "Owie owchie my head!"

    "You" "Sorry Hippo, I guess I didn’t see you there."

    show hippo
    with dis
    Hippo campusstanding campussad1 "Nah that’s fine. It really was my fault for not looking up from my phone."

    "You" "What were you doing on your phone anyways?"

    show hippo
    with dis
    Hippo campushappy1 "I was just playing Pokémon Have."

    "You" "Pokémon Have?"

    show hippo
    with dis
    Hippo campusneutral "Oh, I guess you would call it Pokémon Go."

    "You" "Do people even play that anymore?"

    show hippo
    with dis
    Hippo campusclenched campusangry1 "Hey it's still a great game. Just because it's no longer popular doesn't mean you shouldn't play it."

    "You" "I guess so."

    "After only playing Pokémon Go once when it first blew up, I never really returned to it. I don’t exactly know why though, since it
        seemed like something I would enjoy. I guess I never had anyone to play it with."

    show hippo
    with dis
    Hippo campuspress campushappy1 "Why don’t you join me? We could have a grand ol’ time catching Pokémon together."

    menu:
        "While I still don’t particularly care for Pokémon Go, I don’t really have anything else to do at the moment. So I guess I could,
            if I really wanted to. I mean I did kinda want to check out that purple forest too, though. What should I say?"

        "Yea sure.":
            jump scene5HippoGo
        "Nah, maybe another time":
            jump scene5PurpleForest

label scene5HippoGo:

    "You" "Yea sure, let me download it first."
    scene black
    with fade
    scene park
    with fade
    play music date
    "We spend the rest of the evening catching Pokémon. Hippo teaches me quite a few tricks about the game, like how to throw Pokéballs
        correctly and where to find which Pokémon."
    "It’s strange, the few hours we’ve spent together catching Pokémon were probably the
        best hours I’ve ever had playing a video game. Is this what being a normie feels like?"

    "After Pokemon Going around for a while, we find a small beautiful lake with some ducks hidden between the trees."
    "The benches here weren’t that comfortable, so we decided to sit down on the grass overlooking the water, and anyways, this way we
        have a better view of the ducks as they swim by."

    show hippo campusgrabby campusneutral at center:
        ypos 1280
    with Dissolve(.5)

    "I snatch a quick glance of Hippo and find him mesmerized by the ducks. He seems to really like animals and cute things."

    "You" "So I’ve been meaning to ask, why do you carry your plushies around with you?"

    show hippo
    with dis
    Hippo campusclenched campusangry2 "Why wouldn’t I? They’re soft and cuddly and I love them. Why don’t YOU carry plushies around with YOU, huh?"

    "You" "Oh uh, yeah, I guess you’re right."

    "You" "..."

    "You" "So, what are their names?"

    show hippo
    with dis
    Hippo campushandsup campushappy1 "Well, in the bag here we have Pumk, a wily pumpkin lass who don’t take no guff from no BIG CHEESE. She’s the coolest."

    "You" "I see…"

    show hippo
    with dis
    Hippo campushandsup campusneutral "Next to her is Guin, Lord of Sin. Other than going on a bloodthirsty rage for vengeance over the death of Club Penguin every
        so often, he’s a pretty chill guy."

    "You" "Well that’s nice to hear."

    show hippo
    with dis
    Hippo campusstanding campushappy2 "And finally, this little Hippopotamus is Fiona. I saved her from the zoo and gave her a hat so now she hangs out with me
        wherever I go."

    "You" "Saved her from the zoo?"

    show hippo
    with dis
    Hippo campusgrabby campusconfused1 "I mean I technically stole her from there, but she is just the cutest little baby that I’ve ever seen and I just couldn’t
        leave her there all alone."

    show hippo
    with dis
    Hippo campusstanding campusshock1 "I have so many more back at my place! I mean, you haven’t even met Vriska yet. You should totally stop by sometime."

    "You" "I’ll uhh, consider it."

    show hippo at center
    with Dissolve(0.5)
    "Hippo then stands up and stretches."

    show hippo
    with dis
    Hippo campusneutral "Speaking of my place, it’s getting late so I better go home. I had a very nice time hanging out with you today, so I hope
        we can do it again sometime."

    "You" "Yeah, same here."

    show hippo
    with dis
    Hippo campussmitten1 blushies "Well, see you tomorrow then."

    show hippo at ease(center, offscreenleft, 1.0)
    with Dissolve(0.5)
    "Hippo then walks off leaving me alone with the ducks. Other than being a little strange he really seems like a nice guy. I hope I
        can get to know him better."

    jump endDayOne

label scene5PurpleForest:
    "You" "Nah, maybe another time. I only really wanted to check out the park for a bit."

    show hippo
    with dis
    Hippo campusstanding campussad1 "Oh no worries. Well I still have some catching to do so I guess I’ll see ya tomorrow then."

    "You" "Yea, see you then."

    show hippo at ease(center, offscreenright, 1.0)
    "I watch as Hippo walks off, phone in hand, and wonder if I should have just gone with him. Too late now I guess. I continue onwards
        towards the purple forest."

    stop music fadeout 2.0
    play music homemorning fadein 2.0

    "As I near closer a figure comes walking out, and soon I realize that it’s Mage. Something looks a little different about her…
        probably just her clothes. I run up to say hi."
    show mage casual3 casualneutral
    with Dissolve(.5)
    "You" "Hey Mage!"

    show mage casual3 casualhappy1
    with dis
    Mage "Oh hey [player_name], what brings you here?"

    "You" "I don’t know, maybe the purple forest that’s right behind you? What were you doing in there anyways?"

    show mage
    with dis
    Mage casual1 casualshock1 "No need to be so suspicious of me, I was just enjoying the scenery."

    show mage
    with dis
    Mage casual2 casualhappy1 "I just love forests and trees, especially how peaceful and powerful they can look. This forest in particular is one of my
        favourites. Everything comes together to make it feel magical."

    "You" "Wow, that sounds wonderful. But, what’s with the outfit then?"

    show mage
    with dis
    Mage casual3 casualblush1 "Oh, I just think this looks cute, so I try to wear it wherever I can. What, do you not think it’s cute?"

    "You" "Uhh, y-yeah it's pretty c-cute on you."

    "You" "Well, um, I'll be checking out the forest now, so I guess I'll see you tomorrow then."

    stop music
    show mage
    with dis
    with vpunch
    Mage casual4 casualshock2 "WAIT! I mean, I wouldn't recommend you going in there."

    "You" "Wait, why not? After how much you praised it, I'd imagine you’d want more people to see it."

    show mage
    with dis
    Mage casual4 casualangry2 "It’s a secret! But what I can tell you is that I think it would be unwise of you to enter now."

    "I'm taken aback by this drastic change in her usual attitude. Maybe I should just trust her on this one."

    play music homenight fadein 5.0
    "You" "Uh, yeah. Sure. I won't go in there."

    show mage
    with dis
    Mage casual3 casualhappy2 "Well, thank you. It’s getting late, so you shouldn’t stay out too long. See ya tomorrow!"

    "You" "Yeah, see you then."

    show mage at ease(center, offscreenleft, 1.0)
    with Dissolve(0.5)
    "As Mage walks away I feel as though I’ve stumbled onto something I really shouldn't have. I mean, what possible reason would she have
    for asking me to not enter? I take a long look at the forest before turning around and heading back home."

    jump endDayOne
