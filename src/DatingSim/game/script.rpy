# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = DynamicCharacter('player_name')
define player_thinking = Character(what_italic = True)

define roomie = Character("Roommate")

# define romanceable characters
define dom = Character("Dominic")
define victoria = Character("Victoria")
define august = Character("August")
define finley = Character("Finley")

# define characters in debate
define debateStudent = Character("Student")

# Pronoun data setup
default subj_pron = ""
default obj_pron = ""
default posses_adj = ""
default posses_pron = ""
default reflex_pron = ""

# General Flags
default club = "no club"
default meetPrep = "false"
default skipped_class = "false"
default haunted_house = "none"
default messedUpDebate = "false"
default knowAugust = "false"
default sidedWithAugust = "false"
default joinedDebateTeam = "false"
default assholeToAugust = "false"

# Flags for Dom route
default slept_in = "false"
default answered_door = "false"

image heart = Image("images/heart.png", xalign=0.5, yalign=0.5)


label start:
    $ portrait_number = 0
    $ badboyPoints = 0
    $ prepPoints = 0
    $ artistPoints = 0
    $ tsunPoints = 0

    play music "music/on-my-way.mp3" loop fadein 1.0
    scene dorm room

    "DATING SIM DEMO"

    #####################################################################
    #
    #  FIRST SCENE
    #  > Roommate introduction
    #  > Name input
    #  > Pronoun choice
    #  > Portrait choice
    #  > Personality test
    #
    #####################################################################

    # Andrea: Start proper story?
    roomie "Oh my goodness you're here! You're here!"
    show roommate happy with moveinleft
    roomie "You're my new roommate, right?"

    # ALEXIS: Name input
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Default"
    $ player_name = name

    roomie "Ah [player_name]! It's so nice to meet you!"
    player "It's nice to meet you too!"

    # # ANDREA: Pronoun Selection
    roomie "Ah, also, what are your pronouns?"
    player "Oh, thanks for asking! I use..."
    menu:
        "They/Them":
            $ subj_pron = "they"
            $ obj_pron = "them"
            $ posses_adj = "their"
            $ posses_pron = "theirs"
            $ reflex_pron = "themselves"
        "She/Her":
            $ subj_pron = "she"
            $ obj_pron = "her"
            $ posses_adj = "her"
            $ posses_pron = "hers"
            $ reflex_pron = "herself"
        "He/Him":
            $ subj_pron = "he"
            $ obj_pron = "him"
            $ posses_adj = "his"
            $ posses_pron= "his"
            $ reflex_pron = "himself"

    roomie "Well, it's wonderful to meet you [player_name]. I already know we're going to have a lot of fun together."
    player "What do you mean?"
    roomie "Well, first things first, let's get you settled in!"

    hide roommate happy with dissolve

    "Your roommate helps you put your bags down, and leaves you to start unpacking. There's a mirror next to your bed you glance at yourself in."

    player_thinking "What do I look like?"

    # AMELA: Character appearance selection

    screen portrait_selection():
        # Screen that displays 4 image buttons in a 2x2 grid.
        # The player clicks on an image to set their "appearance".

        vpgrid:
            cols 2
            spacing 20

            xalign 0.5
            yalign 0.5

            imagebutton auto "portraits/portrait1_%s.png" action Return(1)
            imagebutton auto "portraits/portrait2_%s.png" action Return(2)
            imagebutton auto "portraits/portrait3_%s.png" action Return(3)
            imagebutton auto "portraits/portrait4_%s.png" action Return(4)

    call screen portrait_selection

    # player appearance set by portrait selected
    $ portrait_number = _return

    roomie "Finished?"
    player "Yeah, I'm almost done. Why, what's up?"
    roomie "I found this personality quiz on a blog earlier, you should take it!"

    show roommate happy with moveinright

    player "A personality quiz?"
    "She hands you a piece of torn notebook paper with some questions written down on them."

    #start of quiz
    roomie "Would you rather..."
    menu:
            "Read a book at home":
                $ artistPoints += 1
                $ prepPoints += 1
            "Go out to a raging party":
                $ badboyPoints += 1
                $ tsunPoints += 1

    roomie "Would you rather have..."
    menu:
        "A close group of friends":
            $ artistPoints += 1
            $ tsunPoints += 1
        "A large number of acquaintances":
            $ badboyPoints += 1
            $ prepPoints += 1

    roomie "On a first date, you would prefer to go to... "
    menu:
        "To a movie theater":
            $ artistPoints += 1
            $ badboyPoints += 1
        "On a picnic":
            $ prepPoints += 1
            $ tsunPoints += 1

    player "What kind of blog did you find this on, again?"
    roomie "No matter, thanks!"
    "She looks down at your answers and seems to be counting."
    player_thinking "What was that about?"
    roomie "Ah! I don't know."
    player "Don't know what?"
    roomie "Who you'd be cuter with!"
    player "What do you mean?"
    roomie "My friends! I'd love for you to meet them soon."
    roomie "Some of them have been looking for someone, some haven't but really should."
    roomie "They're really nice! I'm sure you'd like them."
    roomie "Dominic is my oldest friend. He's a bit of a tease but he's got the whole badboy look going on."
    roomie "AND he's a serious hottie."
    roomie "Victoria is honest. She can be blunt, but she's also the most sincere person I've met."
    roomie "August I didn't meet until freshman year, but they've been super helpful whenever I'm feeling down."
    roomie "They have the softest heart."
    roomie "And then there's Finley. They have a tough exterior, but they are really sweet once you get to know them."
    roomie "But! You'll meet them all eventually, I'm sure."
    roomie "Look at me prattling on. I should let you get some rest before tomorrow! First day!"

    hide roommate happy with dissolve

    player_thinking "First day... I'm a little nervous. I wonder what tomorrow will be like."

    #####################################################################
    #
    #  SECOND SCENE -- Choose Club
    #  > Choose Club
    #  > If Graphic Design -- Meet Artist
    #  > If Debate Team -- Meet Prep
    #  > If No Club -- Meet Tsundere
    #
    #####################################################################

    scene outside campus 1 with fade

    player_thinking "The first day of school is nerve-wracking, but generally uneventful."
    player_thinking "All of my classes went smoothly. Mostly reading through syllabuses. Syllabi?"
    player_thinking "It's been a long day, but there's one last thing I should do before I leave..."
    player_thinking "At orientation they mentioned a number of clubs. Maybe I should join one."

    menu:
        "Graphic Design Club":
            $ club = "graphic design club"
            "I think I'll join the graphic design club."
            jump meet_artist
        "Debate Team":
            $ club = "debate team"
            "I think I'll join the debate team."
            jump meet_prep
        "No club":
            $ club = "no club"
            player_thinking "None of the clubs sound right for me right now. I think I'll get some food."
            jump meet_tsun

# Meet Artist: Andrea
label meet_artist:
    scene design club with dissolve
    play music "music/windswept.mp3" loop fadein 1.0
    player_thinking "There's only one spot left..."
    show artist with moveinleft
    $ knowAugust = "true"
    $ assholeToAugust = "false"
    player_thinking "The person sitting next to me is looking at me. Why are they blushing?"
    menu:
        "Introduce yourself":
            player "Hi, I'm [player_name]. I'm new here."
            play sound "audio/artist_laugh.mp3"
            "The person sitting next to you is smiling at their screen."
            august "I'm August."
            player "August? I like your name!"
            august "Really? I like yours too..."
            player_thinking "Am I blushing now?"
            "You start up your laptop and open your most recent design project"
            august "Oh wow, you're really talented!"
            player "Ah, you think so? Thank you!"
        "...":
            pass

    "The club president calls everyone's attention and introduces you to all the club members. They are very welcoming."
    "The person sitting next to you, August, keeps glancing at you. "

    menu:
        "Ask August about what they are working on":
            player "What have you been working on?"
            august "Do you want to see?"
            player "Absolutely!"
            "August shows you a sketch of a creepy but beautiful mermaid."
            menu:
                "Oh wow, that's stunning!":
                    play sound "audio/artist_laugh.mp3"
                    august "Thank you!"
                    show heart with zoomin
                    hide heart with dissolve
                    $ artistPoints += 1
                "...Ew, that's weird. Don't talk to me.":
                    august "Oh. Sorry."
                    $ assholeToAugust = "true"
        "Tell August they're being creepy":
            player "What are you looking at me for?"
            august "Oh! I uh..."
            player "You what? huh? need anything?"
            august "No, no! I'm sorry, I didn't mean to bother you."
            player "Yeah, I don't care, just stop being creepy."
            $ assholeToAugust = "true"
        "..."

    "You spend the rest of the hour desigining in August's company."
    if assholeToAugust == "true":
        "They looked really uncomfortable the entire time."
    else:
        "It was nice."

    stop music fadeout 1.0
    jump skip_class

label meet_tsun:
    #meet TSUN
    play music "music/easy-lemon.mp3" loop fadein 1.0
    scene school store

    player_thinking "Hey, that person over there looks familiar. I should go say hi."

    show finley

    finley "Hey what are you staring at?"

    menu:
        "I like your shirt.":
            $ tsunPoints += 1
            play sound "audio/tsundere.mp3"
            show heart with zoomin
            hide heart with dissolve
            finley "Thanks for the compliment, not that I needed one. You must be Jane's roommate. Name's Finley."
            player_thinking "Are they blushing? And is that a soft smile on their face?"

        "I think you're friends with my roommate.":
            finley "Oh, you must be Jane's roommate. Name's Finley."

    finley "So what are you doing here?"
    player "I was hungry so I decide to go get some food."
    finley "You should try the grilled cheese. It's very good."

    menu:
        "I love grilled cheese!":
            finley "I know right? It is just so good, or whatever."
            player_thinking "Their smile is so bright."

        "I was actually thinking some pizza.":
            finley "Yeah, pizza is good too."

    finley "Well I should get going. See you later. Not that I'm excited to run into you again."

    hide finley

    stop music

    jump skip_class

label meet_prep:

    $ meetPrep = "true"

    $ joinedDebateTeam = "true"

    player_thinking "I guess there's a debate team recruiting event going on today. I could probably improve my argumentation skills..."

    player_thinking "I guess I'll give it a try."

    scene debate room

    play music "music/acid-trumpet.mp3" loop fadein 1.0

    player_thinking "The room I enter is filled to the brim with other students."

    player_thinking "I walk up to a table filled with debate team keychains, pens, and pamphlets."

    player_thinking "A student is standing next to the table, scribbling something on a clipboard. "

    player_thinking "Her hair is a deep brown, and her eyes are grey."

    player_thinking "She's wearing a beige sweater with black slacks, a pretty bland outfit overall."

    player_thinking "But despite that, something about her is sort of intimidating..."

    player_thinking "She notices me after a few seconds and steps towards me."

    show prep with dissolve

    victoria "So you think you might be good enough to join the debate team, huh?"

    victoria "It's not going to be up to me, but I can tell you right now that it's not easy."

    victoria "I'm Victoria, by the way. I've seen you around before. "

    victoria "You're Jane's roommate, [player_name]."

    player "Yep, that's me."

    player_thinking "She smirks and looks down at her clipboard again."

    victoria "So, you still want to sign up?"

    menu:
        "Heck yeah!":
            $ prepPoints += 1
            show heart with zoomin
            hide heart with dissolve
            player "Yeah, I could hold my own in a debate!"

            victoria "Wow, you seem really confident. I hope that means you're actually good."

            victoria "Good luck! I'll see you around."

            player "Thanks!"

            player_thinking "She turns around and walks towards another student."

            player_thinking "She seems hard to please, and a bit bland (at least fashion-wise), but maybe there's more to her."

            player_thinking "And now I have to try out... let's see how this goes."

            scene dorm room

            player_thinking "I crushed it! I get to be on the debate team!"

            player_thinking "I wonder what Victoria has to do with the team... she must be pretty high-up in the ranks."

        "I'm not sure...":
            player "I don't know... I guess I'll give it a shot..."

            victoria "You won't make it with that attitude. Maybe a less competitive club would suit you better?"

            player "Um... I'm sorry?"

            victoria "*groan*"

            victoria "Whatever. Later."

            hide prep

            player_thinking "She turns around and walks towards another student."

            player_thinking "Since I'm here, I'll try out anyways."

            player_thinking "I doubt I'll make it, though."

            scene dorm room

            player_thinking "Somehow, I got in. I think I did well enough."

            player_thinking "Victoria doesn't seem to like me, though."

            player_thinking "Maybe I'll have another chance to prove myself."

    stop music fadeout 1.0

    jump skip_class

    #####################################################################
    #
    #  THIRD SCENE -- Free time
    #  > If skip class == meet bad boy
    #  > Free time
    #    > If library == see prep
    #    > If school store == see artist
    #    > If tennis court == see bad boy
    #    > If dorm == see tsundere
    #
    #####################################################################

label skip_class:
    play music "music/easy-lemon.mp3" loop
    scene dorm room with fade
    "BRRRING BRRRING..."
    player_thinking "Ah... another day of university..."
    player_thinking "Hrrg... I'm not really feeling it today. Do I skip class?"

    menu:
        "Skip class":
            jump meet_badboy
        "Go to class":
            player_thinking "Yeah, I guess I should. That's what I'm paying for, anyway."
            scene outside campus 1 with fade
            player_thinking "I went to my only class of the day, which in itself felt like a massive undertaking. I can feel myself getting smarter, though."

    jump free_time_1

label meet_badboy:
    $ skipped_class = "true"

    player_thinking "You know what? I think I will skip class."
    player_thinking "I deserve a break! I'm only human, right?"

    scene outside campus 2

    player_thinking "I find myself taking a pleasant stroll throughout campus."
    player_thinking "Around me I hear people chatting, leaves gently rustling, the distant ringing of bells..."
    player_thinking "It's really peaceful. I'm glad I took this time for myself."
    player_thinking "Even if I might regret it later..."
    player_thinking "As I walk around, someone catches my eye."

    show badboy
    play music "music/acid-trumpet.mp3" loop fadein 1.0

    player_thinking "A boy wearing all black, with facial piercings and what looks like a snake tattoo peeking out of his shirt."
    player_thinking "He looks so... edgy."
    player_thinking "I don't realize that I'm staring until he looks right back at me with a devilish smirk."
    dom "You like what you see?"

    menu:
        "I like it a lot, actually":
            player "Yes! A lot, actually!"
            dom "Whoa! Didn't expect that..."
            player_thinking "Eep. Was that too forward?"
        "W-what?":
            $ badboyPoints += 1
            player "Er, sorry, I didn't mean to stare..."
            play sound "audio/badboy_laugh.mp3"
            show heart with zoomin
            hide heart with dissolve
            dom "Haha! I was just teasing."

    dom "So, what're you up to? Heading to class?"
    player "No, I'm... skipping class, actually..."
    dom "Whoa! Got ourselves a rule-breaker over here!"
    player_thinking "I feel my face going pink..."
    dom "I'm doing the same, actually. Going to class is lame."
    player_thinking "He's so right."
    dom "You just moved in to Jane's place, right? [player_name], is it?"
    player_thinking "Oh! This must be Dominic."
    player "Yeah. She told me about you. I didn't expect to bump into you like this."
    dom "Heh. I'm sure she only had great things to say about me..."
    dom "Well, you're least likely to find me in a classroom-setting, that's for sure."
    dom "Because I'm too cool for school, y'know."
    dom "Anyways, I gotta bounce. Got hooligan activities to attend to. Because I'm a hooligan."
    player_thinking "He sounds like he's kidding, but somehow I can't tell."
    dom "I'm sure we'll bump into each other again. Later!"

    hide badboy

    player_thinking "Before I can even say goodbye, he starts sprinting past me like a madman."
    player_thinking "Those hooligan activities must be urgent..."

    play music "music/easy-lemon.mp3" loop fadein 1.0

    jump free_time_1

# Free time choice, MAP UI interaction
label free_time_1:

    player_thinking "I have some free time... what should I do?"

    call screen MapUI(1)

    return

label library_1:
    player_thinking "I'll go to the library. Maybe I can get some homework done."

    scene library

    play music "music/past-sadness.mp3" loop fadein 1.0

    player_thinking "I walk into the library, and look around for a good spot to study."

    if meetPrep == "true":
        player_thinking "However, I notice Victoria sitting in a dark corner of the library at a desk."
    else:
        $ meetPrep = "true"
        player_thinking "I notice a girl I recognize sitting in a dark corner of the library at a desk."
        player_thinking "I realize it's Victoria, one of Jane's friends. She showed me a picture of her last night."


    player_thinking "She has earphones in and looks really focused, with multiple textbooks, papers, and a laptop scattered about her desk."

    player_thinking "I probably shouldn't bother her... but seeing the look on her face if I startle her might be worth it."

    menu:
        "No scaring today. Go in front of her and wave.":
            $ prepPoints += 1
            player_thinking "Nah, I don't feel like messing with her. It's probably not a good idea anyways."

            player_thinking "I walk closer to her desk and give a little wave. She surprisingly looks up at me, smiles, and takes out her earphones."

            show prep with dissolve
            show heart with zoomin
            hide heart with dissolve
            play sound "audio/prep_hey.mp3"
            victoria "Hey, [player_name]! Long time no see!"

            player "Hi, Victoria! You look like you're hard at work. I don't mean to bother you. I'm here to study, myself."

            player_thinking "Her face lights up at this. I haven't seen her this happy to see me before."

            victoria "Oh, it's no problem! I'm studying for my public policy test. Have I ever told you that I'm majoring in political science?"

            player_thinking "She pats the chair next to her. I have a seat and set my backpack down."

            player "I don't think you have. I have some homework to do, do you mind if I do it here?"

            victoria "Not at all!"

            player_thinking "For a couple hours, we sit together and study our respective materials, occasionally exchanging small-talk and glancing over at one another. A few of her glances linger."

            victoria "Sigh."

            victoria "Alright, I think I'm done for the day. I'm going back to my dorm. I have plans with my roommate tonight."

            victoria "It was fun studying with you, let's do it again sometime!"

            player "Yeah, let's!"

            hide prep with moveoutleft

            player_thinking "I watch her walk away. I'm starting to think that we could become friends! Or possibly more..."
        "Go behind her and scare her!":
            player_thinking "Yeah, why not? This will be hilarious!"

            player_thinking "She hasn't noticed me yet, so I sneak around the edge of the room until I'm behind her, and slowly approach."

            player "BOO!"

            player_thinking "I grab her shoulders."

            show prep with dissolve

            victoria "Aaaah!"

            player_thinking "She screams and shoots out of her seat, nearly knocking over her desk."

            player_thinking "She immediately turns around."

            victoria "What the heck, [player_name]? What was that for!?!"

            player "I just thought it would be funny..."

            victoria "Well, you were dead wrong, buddy. No one's laughing at your stupid prank."

            victoria "Just go away."

            player_thinking "I notice she's rubbing her knee. She must've slammed it into the desk when she stood up."

            player_thinking "Oops."

            player_thinking "She huffs, turns away, and sits back down, not giving me any time to respond."

            hide prep

            player_thinking "I should probably go. I shouldn't have done that... that was mean."

            player_thinking "As I walk out of the library, I notice everyone is staring at me. I really messed up."

            player_thinking "I'll do my homework in my dorm room."
    stop music fadeout 1.0
    jump halloween_party

################ See Artist in school store (Andrea) ################
label schoolstore_1:
    scene school store with dissolve
    play music "music/windswept.mp3" loop fadein 1.0
    "You decided you need to buy some supplies at the school store."

    if knowAugust == "true":
        "Walking around, you see a familiar figure."
        player "August?"
        show artist with dissolve
        if assholeToAugust == "true":
            august "[player_name]."
            hide artist with moveoutright
            menu:
                "Apologize":
                    player "August, wait!"
                    show artist with dissolve
                    august "Yes?"
                    player "I wanted to apologize about what I said during graphic design club. It was mean and you didn't deserve it."
                    august "Oh?"
                    player "I don't know why I said those cruel things, I promise I'm not usually like that."
                    august "Okay. It's okay... We all have bad days."
                    player "Yeah, but it's still no excuse."
                    play sound "audio/artist_laugh.mp3"
                    $ assholeToAugust = "false"
                "...":
                    "You get your supplies and leave."
                    jump halloween_party
        else:
            august "[player_name]! It's lovely to see you again."
            player "It's lovely to see you too! What are you up to?"
            august "Oh! I was just buying some supplies for our next meeting, but then I got distracted by the snacks."
            player_thinking "They're funny in a kind of awkward way..."
            august "I was planning on getting some chocolates for Jane, she really likes them! I'll probably drop by your dorm at some point to give these to her."
            august "If that's okay with you, of course."
            player "Absolutely!"

    else:
        "You run into someone by the art supply section."
        show artist with dissolve
        "They seem to recognize you"
        august "Hey, you're Jane's new roommate, aren't you?"
        player "I am!"
        august "My name is August! What's your name?"
        player "I'm [player_name]."
        august "It's really nice to meet you!"
        $ knowAugust = "true"

    # If you just met them, if you were nice to them, and if you apologized.
    player "Are you and Jane close?"
    august "We are! At least, I think we are. We've only been close for a little bit, but I consider her one of my best friends!"
    player_thinking "They look embarassed..."
    menu:
        "Well, I should get going":
            player "It'll be a long day tomorrow, and I should really go work on my homework."
            august "I completely understand, it was nice seeing you!"
            player "It was nice seeing you too!"
            jump halloween_party
        "I can tell you're a good friend":
            pass
    play sound "audio/artist_laugh.mp3"
    august "I! Well, I try to be! She's a wonderful friend to me, too."
    player "She told me you take really good care of her."
    august "Well... I haven't had that many friends in my life. I just want to make sure the friends I have are happy."
    player "You haven't had many friends?"
    august "No, I'm not sure why... People make me really nervous sometimes."
    player "You don't seem nervous right now."
    august "...I'm not. I'm really comfortable around you, I don't know why."
    menu:
        "I'm glad you feel that way. I feel that way about you, too":
            play sound "audio/artist_laugh.mp3"
            august "I guess that means we have to be friends!"
            player "Yeah, I guess so!"
            show heart with zoomin
            hide heart with dissolve
            $ artistPoints += 1
        "I just try to be nice and honest.":
            play sound "audio/artist_laugh.mp3"
            august "I wish more people were like you then."
            show heart with zoomin
            hide heart with dissolve
            $ artistPoints += 1
        "You just met me.":
            august "...Yeah. You're right."

    "August's phone starts ringing."
    august "It's my mom. I should take this. It was nice seeing you, though, [player_name]."
    player "It was nice seeing you too."

    hide artist with dissolve
    stop music fadeout 1.0

    jump halloween_party

label tenniscourts_1:
    scene tennis courts
    play music "music/windswept.mp3" loop fadein 1.0
    player_thinking "I make my way over to the school tennis courts."
    player_thinking "They're pretty huge, with multiple courts arranged in a grid. I walk onto one that isn't occupied and can see some other students having an intense game past the gate in front of me."
    player_thinking "The fresh air is pretty nice."
    stop music

    if skipped_class == "true":
        dom "Well, well, well, if it isn't the rule-breaker! You skipping class again?"
        player_thinking "That voice sounds familiar..."
        show badboy
        play music "music/acid-trumpet.mp3" loop fadein 1.0
        player_thinking "It's Dominic!"
        player "No! I just had some free time, actually. I haven't seen the tennis courts before..."
    else:
        dom "Hey! You're Jane's friend, right? What're you doing here?"
        player_thinking "Who could that be?"
        show badboy
        play music "music/acid-trumpet.mp3" loop fadein 1.0
        player_thinking "This must be Dominic."
        player "I just had some free time. I hadn't seen the tennis courts yet..."

    dom "Well, I gotta tell you, there isn't much to see..."
    dom "Apart from me, of course."
    player_thinking "He's so smug..."
    player "Do you come here to play tennis, or just to loiter like a hooligan?"
    player_thinking "He cracks a smirk at that."
    dom "I think you know the answer to that."
    dom "But since we're both here, might as well have ourselves a game, no?"
    player "Pausing the hooligan activities for now?"
    dom "There's always time for them."
    player_thinking "I guess we're playing a friendly game of tennis."
    player_thinking "Should I..."

    menu:
        "Try my best":
            player_thinking "I go full tryhard mode. I'm running around the court as swiftly as my legs can take me."
            player_thinking "Dominic looks surprised. Guess he didn't expect me to go so hard."
            player_thinking "But I play to win!"
        "Not sweat it":
            $ badboyPoints += 1
            player_thinking "I don't try too hard. I can see that Dominic clearly doesn't, either."
            player_thinking "We both goof off as we swing our rackets around with the mindset of 'If I don't hit the ball, I don't hit the ball. Big whoop.'"
            player_thinking "By the end of it, we're both laughing at each other."
            play sound "audio/badboy_laugh.mp3"
            show heart with zoomin
            hide heart with dissolve

    dom "Are the tennis courts everything you hoped for?"
    player "Oh, yes. And so much more."
    dom "Heh. That was actually the first time I'd done anything besides loitering at this place. Was pretty fun."
    player_thinking "Is it really loitering if they're open to anyone...?"
    player_thinking "I peek down at my watch and realize it's almost time for my next class."
    player "Hey, I've got class to get to, but thanks for the game."

    if skipped_class == "true":
        dom "Going to class? I'm surprised."
        player "Hey!"

    dom "For sure. I also have... things. But good game."

    hide badboy

    player_thinking "Before I can open my mouth to speak, Dominic sprints towards the nearest tennis net, leaps over it, and continues sprinting towards the exit gate."
    player_thinking "That guy must not have a care in the world..."

    jump halloween_party

label dorms_1:
    scene dorm room

    play music "music/easy-lemon.mp3" loop fadein 1.0

    #"DORMS 1: TSUN IS THERE"
    show finley

    player_thinking "I want to go hangout in my dorm."

    player_thinking "Is that Finley hanging out with Jane?"

    finley "Hey [player_name], me and Jane were just trying to plan a prank on Dominic. Wanna join us? Not that we really need you."

    menu:
        "Sure, sounds like fun!":
            $ tsunPoints += 1
            play sound "audio/tsundere.mp3"
            show heart with zoomin
            hide heart with dissolve
            finley "Awesome. I was thinking something with spiders since Dominic is afraid of them."
            player "What about a plastic spider that drops down when he opens the door?"
            finley "That is perfect! I need to go buy a plastic spider then. See you later [player_name]!"
            player_thinking "They are really blushing with such a bright smile. They must really like pranks."

        "No thanks. I am going to head to my room to relax.":
            finley "That's fine. Have fun relaxing."
            player_thinking "They're frowning at me... ah well."

    hide finley

    stop music

    jump halloween_party

    #####################################################################
    #
    #  FOURTH SCENE: Halloween Party Events
    #  > If Haunted House
    #       > Go with Bad boy +Point
    #       > Go with Tsundere +Point
    #  > If Pumpkin Patch
    #       > Go with Artist +Point
    #       > Go with Prep +Point
    #
    #####################################################################

label halloween_party:
    scene autumn trees with fade
    play music "music/the-show-must-be-go.mp3" loop fadein 1.0
    player_thinking "It's Halloween and the festivities on campus are kicking in."
    player_thinking "I'm surprised how many people are walking around in costume. I feel a little out of place."
    player_thinking "I don't have any classes today, so I might as well have some fun."
    player_thinking "There's a haunted house attraction, and I heard there's a pumpkin patch nearby..."
    player_thinking "Where should I go?"

    menu:
        "Haunted house":
            jump haunted_house
        "Pumpkin patch":
            jump pumpkin_patch

# Haunted House Event - Badboy and Tsundere
label haunted_house:
    scene haunted house outside
    play music "music/dark-times.mp3" loop fadein 1.0

    player_thinking "So this is the haunted house... I wonder if it's actually scary..."
    player_thinking "Wait, those two look familiar."

    show badboy at left with easeinleft
    show finley at right with easeinright

    dom "C'mon, don't be such a wuss! Let's go in!"
    finley "Says the man willing to do any dare."
    dom "And what about it?"
    player "Hey! What's going on?"
    finley "Dominic wants to go to the haunted house, but I don't want to be the minority character at the start of a horror movie."
    dom "Finley here is a wuss who thinks they might actually die if they go inside."
    player "I mean, it does look pretty scary..."
    finley "What do you think, [player_name]? Would you go in?"

    menu:
        "Side with Dominic":
            $ badboyPoints += 1
            $ haunted_house = "true"
            player "Yeah, why not? It looks fun."
            play sound "audio/badboy_laugh.mp3"
            show heart at left with zoomin
            hide heart with dissolve
            player_thinking "A smug grin overtakes Dominic's face, showing the triumph he feels over coming out the victor in this battle."
            player_thinking "Finley looks like they're over it."
            dom "See? [player_name] has the right idea."
            dom "So, whaddaya say we go inside?"
            player "Let's do it!"
            finley "Have fun possibly dying. I'm gonna get some food."
            player_thinking "And with that, Finley unbothered-ly vacated the haunted house premises."
            hide badboy
            hide finley
            scene haunted house inside
            play music "music/unseen-horrors.mp3" loop fadein 1.0 fadeout 1.0
            player_thinking "As I enter the haunted house, I suddenly question the choice I made."
            player_thinking "It's dark, weird noises are coming from everywhere, the decorations are spooky..."
            player_thinking "Dominic still has that smug look on his face as always. I think he's having a good time."
            player_thinking "Suddenly, someone with zombie makeup jumps out at both of us and yells Boo!"
            player "Eeeeeek!"
            dom "Haha! Gonna have to do better than that, kid!"
            player_thinking "I clung closely to Dominic as we traversed through the rest of the house, with ghosts and ghouls meeting us at every corner."
            player_thinking "Hearing him laugh made my uneasiness fade and by the end of it, I was laughing along with him."
            player_thinking "I think I might have caught him blushing, too..."
            scene haunted house outside
            show badboy with dissolve
            play music "music/acid-trumpet.mp3" loop fadein 1.0
            dom "Well, that was as stupid as I expected."
            player "Yeah. Totally."
            dom "What? You were totally scared!"
            player "They got me the first time, yeah, but the scares got kinda cheap after that..."
            dom "Well, as corny as it was, it was pretty fun."
            dom "Finley missed out, for sure. Probably eating cheese curds somewhere."
            dom "We should do more stupid stuff together sometime."
            player "Oh. Yeah, I'd like that."
            dom "Sweet. Catch you later, nerd!"
            hide badboy
            stop music
            player_thinking "Aaaaaaaaand he's gone..."
            player_thinking "I think this was a Halloween well spent."
        "Side with Finley":
            $ tsunPoints += 1
            play sound "audio/tsundere.mp3"
            show heart at right with zoomin
            hide heart with dissolve
            $ haunted_house = "false"
            player "No, you have a point, Finley. Why risk it?"
            player_thinking "Are they blushing? Dominic looks tired."
            if subj_pron == "they":
                finley "See, [subj_pron] get it. You have fun, Dominic."
            else:
                finley "See, [subj_pron] gets it. You have fun, Dominic."
            dom "You know what? I think I will. See ya later, losers!"
            hide badboy
            player_thinking "And with that, Dominic almost comically skipped off into the darkness past the haunted house's front door."
            finley "I'm going to go get some cheese curds. You want to come or not?"
            player "Sure!"
            hide finley
            play music "music/the-show-must-be-go.mp3" loop fadein 1.0
            scene autumn trees
            show finley
            player_thinking "I think the cheese curd stand isn't far from here. Finley is coming back from the counter with two baskets of cheese curds."
            finley "Here, you want one? Not that I bought you some for siding with me or anything. It was just cheaper to buy two."
            player "Sure, thanks. We should probably find somewhere to eat these."
            finley "That tree over there looks pretty comfy. Let's head over there."
            player_thinking "I take a bite of my cheese curds and taste the gooey goodness of the cheese wash over my taste buds."
            player_thinking "I look over to see Finley with their eyes closed and the softest smile on their face."
            finley "What are you looking at?"
            player "Nothing. These cheese curds are really good."
            finley "Of course they are. It's fried cheese. What could be better?"
            finley "I guess we should probably go make sure Dominic isn't dead."
            hide finley
            player_thinking "As we head back to the haunted house, I can still see Finley's soft smile in my head."
            stop music

    jump free_time_2

# Pumpkin Patch event - Artist & Prep
label pumpkin_patch:
    scene pumpkin_patch with fade
    "After deciding to go to the pumpkin patch, you run into..."
    show prep at left with dissolve
    show artist at right with dissolve
    victoria "I told you already, I don't want you to draw me! I have hay everywhere!"
    august "And yet you still look beautiful! I need some practice... please?"
    victoria "No!"

    #   Depending on who you've met...
    if knowAugust == "true":
        if assholeToAugust == "true":
            august "Oh... I should go."
            hide artist with moveoutright
            show prep at center with move
            victoria "...I guess that settles that! Let's go to the corn maze!"
            $ prepPoints += 1
            show heart with zoomin
            hide heart with dissolve
            jump corn_maze
        # If you know August and Victoria
        if meetPrep == "true":
            "Victoria and August!"
        # If you only know August
        else:
            $ meetPrep = "true"
            "August! and someone you don't recognize."
            august "Oh hey! It's [player_name]."
    else:
        # If you only know Victoria
        if meetPrep == "true":
            "Victoria! and someone you don't recognize."
            victoria "Oh look, there's [player_name]. Help me get out of this, please."
        # If you know Neither
        else:
            $ meetPrep = "true"
            "Two strangers are having a heated argument!"

    august "Sorry, we were just trying to figure out what we wanted to do..."
    victoria "I want to go to the corn maze!"
    august "I just want to sit here sketch stuff out, it's so lovely out here."
    player_thinking "What do I want to do?"
    menu:
        # Go with prep, jump to corn_maze
        "Go with Victoria to the Corn Maze":
            player "I haven't gone to a corn maze in a really long time, that sounds really fun!"
            victoria "YAY!"
            august "Ah, I think I'll just hang back here and draw the pumpkins... I hope you two have fun though!"
            hide artist with dissolve
            show prep at center with move
            victoria "Let's go, [player_name]!"
            show heart with zoomin
            hide heart with dissolve
            $ prepPoints += 1
            jump corn_maze

        # Go with artist, jump to draw_pumpkins
        "Keep August Company":
            $ sidedWithAugust = "true"
            player "It's beautiful out here, you should definitely draw something August."
            player "If Victoria wants to go to the corn maze, I can keep you company instead."
            victoria "I have an idea... you should draw [player_name]! I'll go to the maze!"
            august "Are you sure? Well, I hope you have fun!"
            hide prep with dissolve
            show artist at center with move
            august "...let's go find a spot to sit."
            show heart with zoomin
            hide heart with dissolve
            $ artistPoints += 1
            $ halloweenCompany = "August"
            jump draw_pumpkins

label corn_maze:
    scene corn maze
    play music "music/easy-lemon.mp3" loop fadein 1.0
    show prep with dissolve

    player_thinking "We arrive at the corn maze together, and we walk through the entrance."
    victoria "Oooh, this is so cool! Let's try to go through it super fast! Ready?"
    player "Yes!"
    victoria "Let's go!!"
    player_thinking "She grabs my hand and we take off running. We go right, then left, then right, then right again."
    player_thinking "We go left, and hit a dead end. I have too much momentum and run straight into Victoria."
    player "Oops! Sorry! Are you okay?"
    player_thinking "Victoria is obviously fine, and giggles."
    victoria "I'm fine! You didn't knock me over or anything. Ooh, let's go this way!"
    player_thinking "She grabs my hand and we're off again, going right, straight, left, straight, left, left, right, and straight."
    player_thinking "Somehow, we stumble upon the exit. Jeez, that was fast!"
    victoria "We did it! That was super fun! I feel like a little kid again."
    player_thinking "She smiles at me and laughs. I smile back."
    player "That was fun! How did you get so lucky?"
    victoria "Dunno… hey, let's go get some apple cider! My treat!"
    player_thinking "She grabs my hand yet again and pulls me over to the snack bar. We sit at a table with our apple ciders and watch the sun go down."
    player_thinking "Then, we say our goodbyes and part ways."
    hide prep with dissolve
    stop music fadeout 1.0
    jump free_time_2

label draw_pumpkins:
    stop music fadeout 1.0
    scene sittin spot with fade
    play music "music/windswept.mp3" loop fadein 1.0
    show artist with dissolve
    august "This is a nice spot, right?"
    player "Yeah, I think so!"
    august "So... about what Victoira said."
    player "About you drawing me?"
    august "Yeah! Uh-- How would you feel about that? Would that be okay?"
    menu: 
        "I'd like that":
            play sound "audio/artist_laugh.mp3"
            august "Really?! That's great!" 
            august "My friends never really let me draw them, so I've never had a live model! I'm so excited!"
            player "I wouldn't call myself a model..."
            august "I mean, you're modeling for me, so-- wait sit still."
            "August pulls out a sketchpad and charcoal from a bag they seem to carry everywhere."
            menu: 
                "I mean, don't models have to be gorgeous?":
                    august "Not really. Even if they were, you *are* gorgeous so,"
                    player_thinking "Did they just-"
                    august "I mean--! I- Sorry, I hope I didn't meake you uncomfortable!"
                    player "No no! It's okay..."
                    player "Do you really think I'm beautiful?"
                    august "... absolutely."
                    player_thinking "Can they tell that I'm blushing?"
                    august "Now sit still so I can draw you."
                    "While August sketches out your outline, they start humming softly."
                "Okay, okay, I'll sit still.":
                    "While August sketches out your outline, they start humming softly."
                "Actually, I changed my mind...":
                    august "Oh! that's alright then, do you just want to sit and talk?"
                    player "Yeah, that sounds nice."
        "I'm not really comfortable with that":
            august "Do you want to just sit and talk for a bit?"
            player "Yeah, that sounds nice."
        
    "You spent the rest of the day talking with August. They seem to really like you."
    stop music fadeout 1.0
    jump free_time_2

    #####################################################################
    #
    #  FIFTH SCENE -- Free Time pt. 2
    #    > If library == see tsundere
    #    > If school store == see bad boy
    #    > If tennis court == see prep
    #    > If dorm == see artist
    #
    #####################################################################

label free_time_2:
    scene dorm room with fade
    play music "music/on-my-way.mp3" loop fadein 1.0

    if haunted_house == "true":
        player_thinking "It's been a week since I went to the haunted house with Dominic."
    elif haunted_house == "false":
        player_thinking "It's been a week since I hung out with Finley."
    else:
        player_thinking "A week has passed since Halloween. I find myself still missing all of the festivities."

    player_thinking "I wish it could be Halloween every day..."
    player_thinking "Well, I have some free time now. What should I do?"

    call screen MapUI(2)

    return

label library_2:
    #"LIBRARY 2: TSUN IS THERE"

    play music "music/easy-lemon.mp3" loop fadein 1.0

    scene campus library  #is this the scene call for the library

    show finley

    player_thinking "Is that Finley at that table over there? I should go see what they're doing."

    player "What are you doing here Finley?"

    finley "Hey [player_name]. I have this big test coming up so I really need to study."

    menu:
        "Do you want some help?":
            $ tsunPoints += 1
            play sound "audio/tsundere.mp3"
            show heart with zoomin
            hide heart with dissolve
            finley "Really? Thanks for the help. Not that I couldn't manage on my own."
            player_thinking "Finley is blushing so much."
            player_thinking "Finley and I spent the next three hours studying for their test."

        "I'll leave you alone to study.":
            finley "Sure. See you some other time."
            player_thinking "I should get back to looking for some books."

    hide finley

    stop music

    jump route_determination

label schoolstore_2:
    player_thinking "I might as well head to the school store and shop with my eyes."

    scene school store

    player_thinking "As I peruse the various university-branded whats-its and thingy-mabobs, I spot a familiar figure in the corner of my eye..."

    show badboy
    play music "music/acid-trumpet.mp3" loop fadein 1.0

    player_thinking "...now, directly in front of my eyes."
    player "Dominic!"

    if skipped_class == "true":
        dom "Hey, class-skipper!"
    elif club == "debate team":
        dom "Hey, debate team!"
        player_thinking "Eh? He knows I'm on the debate team?"
    elif club == "graphic design":
        dom "Hey, graphic designer!"
        player_thinking "Eh? He knows I'm in the graphic design club?"
    else:
        dom "Hey, Jane's roomie!"

    player "What're you doing here? Doesn't seem like a place I'd find you at."
    dom "Why not? Where else would I shoplift, if not at a shop?"
    player "You shoplift?!"
    dom "Pfft! Duh! I've got an image to maintain!"
    player_thinking "I can't tell if he's joking..."
    dom "Whaddaya say? Wanna help me pocket a keychain without getting caught?"

    menu:
        "Yeah! Let's do it!":
            dom "Whoa, really? Well, alright! Stand in front of me but don't look suspicious."
            player_thinking "I can't believe I'm doing this... those keychains are overpriced, anyway, I suppose."
            player_thinking "I stood with my back to Dominic, doing my best to not look shady, but no doubt failing."
            dom "Got it. Good work, comrade."
            player "Do you even want the thing? It's not even a cool keychain..."
            player_thinking "His face got really serious, but I can't tell if it was an act or not."
            dom "It's not about the keychain. It's about the message."
            player_thinking "Almost magically, his face returns to its comfortable smug state."
            dom "Well, time for me to dip."
            dom "You should probably pay for that keychain in your pocket, though."
            player_thinking "I stick my hands in my pockets and sure enough, there's a keychain in one of them."
            player "What? How did you--"
            dom "Toodle-loo!"
            hide badboy
            player_thinking "Aaaaand he's gone..."
            player_thinking "Guess I better put this keychain back before I leave."
        "What? Of course not!":
            $ badboyPoints += 1
            play sound "audio/badboy_laugh.mp3"
            show heart with zoomin
            hide heart with dissolve
            dom "Haha! Don't want to make yourself an accomplice... no matter. I am a professional, anyhow."
            dom "Aaaand done."
            player "What?! You didn't even move!"
            dom "Sure I did. But to your untrained eyes, I remained completely still."
            player_thinking "Again, I have no idea if he's being serious."
            player_thinking "If he did snag it, his sleight of hand skills are really impressive..."
            player_thinking "...he must be great at card tricks..."
            dom "Well, my work here is nearly done."
            dom "There's one last thing I have to do. Come with me to the register?"
            player "Uh... sure."
            hide badboy
            player_thinking "I awkwardly follow him to the cash register, a little confused."
            player_thinking "My confusion grew when he produced a keychain from one pocket and his wallet from the other."
            show badboy
            dom "Smell you later, nerd. Also -- check your pocket."
            player "Check my pocket?"
            hide badboy
            player_thinking "Aaaand he's gone."
            player_thinking "I stick my hands in both of my pant pockets and felt something small and metallic."
            player_thinking "Confused beyond belief, with a shiny new keychain in my hand, I stood there, dumbfounded."

    stop music
    player_thinking "I'll never understand that guy."

    jump route_determination

label tenniscourts_2:
    scene dorm room
    player_thinking "I don't exercise enough, so I think I'll head to the tennis courts."
    player_thinking "I change into some gym clothes, grab my water bottle, and head out."
    player_thinking "I don't own a tennis racket, so maybe I'll be able to borrow one."

    scene tennis courts
    play music "music/windswept.mp3" loop fadein 1.0
    player_thinking "As I walk into the tennis court area, I see a couple sets of fellow students actually playing tennis."
    player_thinking "Everyone else seems to be just talking and standing around."
    player_thinking "Out of the corner of my eye, I notice someone sitting by the supplies shed, throwing a tennis ball against the brick wall over and over."
    player_thinking "I get closer, and I realize it's Victoria."
    player_thinking "I can't fully see her face, but she seems to be throwing the ball really aggressively. I should go check in with her."
    player_thinking "I walk up to Victoria and she notices me out of the corner of her eye."
    show prep with dissolve
    if sidedWithAugust == "true":
        victoria "Hmph. What do you want?"
        player_thinking "She sounds cold, and she continues to throw the tennis ball at the wall over and over as she waits for my reply."
        player "I'm sorry for hanging out with August at the pumpkin patch. How was the corn maze?"
        victoria "Hmph. I guess I forgive you. It was really fun, I was the fastest!"
        player "Well, I'm glad!"
    else:
        player_thinking "She relaxes her shoulders a little and turns toward me."
        victoria "Hi, [player_name]."
        player "Hi, Victoria."
    victoria "So what's up?"
    player_thinking "I twiddle my thumbs. She seemed upset before she noticed me. Should I ask her about it?"
    menu:
        "Ask her what's wrong!":
            $ prepPoints += 1
            show heart with zoomin
            hide heart with dissolve
            player "I noticed you seemed pretty upset before I came over here. Is something the matter?"
            player_thinking "Victoria sets down the ball and sighs, then pats the ground next to her, motioning me to sit down."
            player_thinking "I go over and sit."
            victoria "It shouldn't be a big deal… really. I don't know why I'm so bothered by it?"
            player "What is it?"
            victoria "My parents have really high expectations for me… and sometimes they feel too high. It's too much pressure."
            victoria "They found out that I'm struggling in my organic chemistry class… it's not even required for my degree, but they wanted me to take higher-level science classes anyway."
            victoria "So they are giving me the cold shoulder."
            player "I'm so sorry… is there anything I can do?"
            victoria "Nah, it'll be fine, probably. You wanna play some tennis?"
            player "Sure!"
            player_thinking "We play tennis till it starts getting dark outside, then we call it a day. We both go back to our separate dorms, tired but fulfilled."
            hide prep with dissolve
            scene dorm room
            player_thinking "Tennis is really fun. I didn't know that her parents are like that, but maybe that's why she's such an overachiever."
        "Let's play tennis!":
            player "Do you want to play a game of tennis?"
            victoria "Not really. I think I'm going to go back to my dorm room. I guess I'll see you later."
            victoria "Bye."
            player_thinking "She leaves, and after bouncing a tennis ball off the wall for a while, I leave as well."
    stop music fadeout 1.0
    jump route_determination

################ See Artist in Apartment (Andrea) ################
label dorms_2:
    play music "music/windswept.mp3" loop fadein 1.0
    scene dorm room with fade
    show artist with dissolve
    "You enter your apartment and see August sitting on your couch."
    if knowAugust == "false":
        august "Oh! I was wondering when I'd run into you. You're [player_name], right?"    
    if assholeToAugust == "true":
        august "Oh, I'm sorry. I should go."
        menu:
            "Yes, you should.":
                "August looks sad."
                august "All of my friends think you're really nice... I don't understand it."
                august "Why do you hate me? ...No, I don't want to know."
                august "I'm sorry if I did or said anything that lead you to be so uncomfortable around me."
                august "I'll stay out of your way."
                hide artist with moveoutright
                $ artistPoints = 0
                jump route_determination 
            "No, it's okay, stay. I should apologize.":
                august "It's okay."
                player "No it's not. I should've apologized a long time ago. You don't deserve to be treated like that."
                august "That... is really kind of you. You confuse me, [player_name]."
    else:
        august "[player_name]! It's good to see you..."

    august "Sorry, I don't mean to invade your space. I was just waiting for Jane to finish getting ready."
    player "Are you two going somewhere?"
    august "Yes? She was just gonna drive me to a little forest nearby so I can finish up a project I've been working on."
    player "What kind of project?"
    august "Well... It's a little weird. I might show you at some point, though. I've only shown Jane, so far."
    menu:
        "Go to your bedroom":
            player "Well, I'll let you wait. I should go work on some homework."
            august "Alright!"
            hide artist with dissolve
            scene bedroom 
            "You've been working on homework for half hour when you hear a knock on the door."
            august "Hey, [player_name]? Do you know where Jane went?"
            player "What do you mean? I thought you were waiting for her."
            august "I was, but I've been waiting for a little bit. I think she left."
            menu:
                "You can catch her next time then. Bye!":
                    august "Oh, alright. I'll see you later then."
                    jump route_determination
                "What do you mean she left?":
                    scene dorm room
                    show artist with dissolve 
                    "You come out of your bedroom to talk to August again."
                    
        "Stay with August":
            player "How long have you been waiting for her?"
            august "About half an hour."
            player "Half an hour? That's a really long time. I can go check on her for you."
            august "It's okay! I can wait. I don't really mind."
            player "No, don't worry, I'll just go make sure everything is okay."
            august "This happens sometimes, but I'm patient, you don't need to stress."

    "You check Jane's room and find it empty. She's definitely left."
    august "Ah, she texted me back."
    player "What did she say?"
    august "Shes hanging out with someone else... That's okay. I guess I'll go home."
    
    menu:
        "But you were really excited!":
            pass
        "Okay, bye now.":
            august "Have a nice day okay?"
            hide artist with dissolve
            jump route_determination
    august "I was. But like I said, this happens sometimes. She's a busy person, she has a lot of friends."
    player "She could have at least told you she was leaving."
    august "She said she forgot I was here."
    player "That's not okay..."
    menu:
        "We should do something together.":
            player "I know it's not what you originally had planend... but you're already here!"
            august "You want to hang out with me?"
            player "Yeah! What do you want to do? We can play board games, I have a few in my room. We could play video games. We could draw together. Anything you want! Something fun."
            august "Really? Ah, [player_name], you don't have do comfort me."
            player "I don't have to, but I want to. Let's do something fun!"
            play sound "audio/artist_laugh.mp3"
            august "... okay. Let's do something fun." 
            show heart with zoomin 
            hide heart with dissolve 
            $ artistPoints += 1
            "You and August spent the rest of the day together, and it meant the world to them."
        "But I'm sure she meant no harm.":
            player "I don't know her well yet, but she seems like a kind person."
            august "She is, most of the time."
            player "Most of the time?"
            august "I'm starting to worry she doesn't really like me..."
            player "I'm sure she does!"
            august "You don't know that..."
            player "I know that you're a very likeable person, though. So if she doesn't like you, then it's her being silly."
            august "She's my friend."
            player "And so am I, now. Because I know you're a good friend, so I want to be a good friend to you too."
            august "I should get going."
            player "You can stay if you want to."
            play sound "audio/artist_laugh.mp3"
            august "... I'll stay then."
            show heart with zoomin 
            hide heart with dissolve 
            $ artistPoints += 1
            "You and August spent the rest of the day together, and it meant the world to them."
        "Maybe she doesn't love you.":
            august "I know. I know that she doesn't."
            player "Then what are you doing here?"
            august "I don't know. Being stupid, I guess. I should go home."
            player "Okay."
            august "Okay."
            $ assholeToAugust = "true"
            hide artist with dissolve

    jump route_determination

label route_determination:
    # "Badboy points: [badboyPoints], prepPoints: [prepPoints], artistPoints: [artistPoints], tsunPoints: [tsunPoints]"
    python:
        points = [badboyPoints, prepPoints, artistPoints, tsunPoints]
        # print("Max points is " + str(max(points)))
        # print("Index of max points is " + str(points.index(max(points))))
        index_num = points.index(max(points))

    $ route_number = index_num

    if route_number == 0:
        jump BADBOY_START
    elif route_number == 1:
        jump PREP_START
    elif route_number == 2:
        jump ARTIST_START
    else:
        jump TSUNDERE_START

    return

    #####################################################################
    #
    #  ROUTES BASED ON POINTS
    #    > Badboy Route
    #    > Prep route
    #    > Artist route
    #    > Tsundere route
    #
    #####################################################################    

label BADBOY_START:
    scene bedroom
    play music "music/easy-lemon.mp3" loop fadein 1.0

    player_thinking "BRRING BRRING..."
    player "... another great day to be alive."
    player_thinking "I sleepily rise from bed and look at the time. I really don't feel like going to class today."
    player_thinking "I should..."

    menu:
        "Sleep in":
            $ slept_in = "true"
            player "I won't die if I miss this one class."
            if skipped_class == "true":
                player "I probably shouldn't make this a habit, though... I think Dom's rubbing off on me..."
            player_thinking "Before I'm able to crawl back into bed, I hear a knock at the door."
        "Get out of bed":
            $ slept_in = "false"
            player "Yeah, I guess I better get out of bed."
            player "Life is hard, being a human with obligations."
            player_thinking "Before I take even one step out of my room, I hear a knock at the door."

    stop music
    player_thinking "That's weird. That can't be Jane. She has a key, and would text if she lost it."
    player_thinking "Jane's also in class right now, so she wouldn't have a friend over, right?"
    player_thinking "Who could that be...? Are we expecting maintenance or something?"

    menu:
        "Answer the door":
            $ answered_door = "true"
            scene dorm room
            player_thinking "A little apprehensively, I rise from bed, still in my pajamas, and make my way to the front door."
            player_thinking "I'm really curious who it could be... is it a prank?"
            player_thinking "I open the door to a unexpected familiar face."
            show badboy
            play music "music/acid-trumpet.mp3" loop fadein 1.0
            dom "Hey, does [player_name] live here?"
            player "Um... no."
            dom "Oh. Bummer. I'll try all the other rooms, then."
            player "Er... did you need something? Jane's in class."
            dom "Yeah, I have some hooligan errands I need to run and could use some assistance. You in?"
            player "Like, what kind of 'hooligan errands'?"
            dom "Like loitering outside the lecture halls. If I don't, who else will?"
            player_thinking "Is this how he asks people to hang out? 'Hey, come loiter with me'?"
            player "That's a fair point. Let's go!"
            hide badboy
            jump dominic_event_1
        "Ignore it":
            $ answered_door = "false"
            if slept_in == "true":
                player "Maybe they have the wrong dorm. I'll pretend I didn't hear that."
                player_thinking "Time to enjoy some shut-eye!"
            else:
                player "Er... I really don't wanna get that..."
                player_thinking "I'll get ready and leave once I think they're gone."

    # Time skip to MC with Jane at the dorm

    scene dorm room with fade
    play music "music/on-my-way.mp3" loop fadein 1.0
    show roommate happy

    roomie "Hey, were you here around 10 this morning?"
    player "Yeah, why do you ask?"
    roomie "Dominic sent me a text earlier saying that he came by but no one answered the door."
    roomie "I was in class, but I thought you were still home."
    player_thinking "Oh, shoot... what should I say?"
    menu:
        "I didn't hear it":
            player "Oh, really? I didn't hear anything. Maybe he came while I was still asleep."
            roomie "Haha! Bummer. He's the spontaneous type, as you've probably noticed."
            roomie "I'll let him know to knock louder next time."
        "I didn't know who it was":
            player "Er... I didn't answer because I thought it was a stranger..."
            roomie "Haha! You're a careful one. It was just Dom."
            roomie "He seemed kinda bummed. I'll tell him to text next time, but he's not one to plan things."

    roomie "Oh, well. Don't tell him I said this, but I think he likes you."
    player "Huh? What makes you say that?"
    roomie "I don't know. It's just a feeling. I could be wrong."
    roomie "I think you remind him of someone..."
    roomie "Well, I've got some cramming to do. Talk to you later?"
    player "Yeah, me too. Catch you later."

    hide roommate happy
    stop music
    scene bedroom with fade

    player_thinking "I remind him of someone?"
    player_thinking "I sat on my bed and did some homework, but it was difficult to concentrate."

    jump dominic_event_2

label dominic_event_1:
    scene outside campus snow
    show badboy
    player_thinking "So... loitering, I guess."
    player "Is this your idea of fun?"
    dom "It isn't yours?"
    player_thinking "Does he really not do anything else? Does he just like to idle with other people?"
    player_thinking "Is it just with me...?"
    player "Don't you have any other hobbies?"
    dom "Like what?"
    player "I don't know. Sports, art, music... anything like that?"
    player_thinking "He takes a second to think."
    dom "I like tagging buildings. And riding my motorcycle."
    player_thinking "How stereotypical. Is he joking?"
    player "You ride a motorcycle? How come I've never seen it?"
    dom "Not around campus. I keep it in a safe spot."
    dom "Maybe one of these days I'll let you witness it."
    player "Er, anything else?"
    dom "Arson is pretty fun."
    player_thinking "Arson?!"
    player_thinking "Silence."
    player "Is that it?"
    dom "Tax evasion."
    player "Is that a hobby?"
    dom "Nah, I'm just messing with you on that one. But all the others are true."
    player "You actually commit arson?!"
    dom "Once in a while, yeah. What about you? What do you do for fun?"
    player_thinking "How can he just breeze past that?"
    player_thinking "Well, what do I do for fun?"

    menu:
        "Tag buildings":
            player "I like to tag buildings too, actually. Do it all the time."
            player_thinking "Dominic raises an eyebrow."
            dom "Yeah?"
            player "Yeah."
            player_thinking "I'm a terrible liar."
            dom "Impressive. I would have never thought."
            player_thinking "He's just playing along..."
        "Write poetry":
            $ badboyPoints += 1
            player "I write poetry sometimes."
            player "It's less work than writing full novels. It can be kinda cathartic, too."
            play sound "audio/badboy_laugh.mp3"
            show heart with zoomin
            hide heart with dissolve
            dom "Really? That's kinda cool. That's not a common answer."
            dom "Can I read it sometime?"
            player_thinking "This guy wants to read poetry?"
            player "Sure. It's nothing special, though..."
            dom "I'm sure it's great."
        "Sleep":
            player "Um... sleeping is pretty fun. I do that a lot."
            dom "Ah. You like to live dangerously."
            dom "In the vulnerability of unconsciousness..."
            player_thinking "What is he talking about?"

    player_thinking "We spent the day having somewhat weird conversations before he abruptly made a run for the parking lot with a quick goodbye."
    hide badboy
    player_thinking "Even if it was kinda weird, I had a fun time hanging out with Dominic. I even learned some things about him."

    jump dominic_event_2

label dominic_event_2:
    scene outside dorms snow with fade
    play music "music/past-sadness.mp3" loop fadein 1.0

    player_thinking "Man, it's cold outside. But it's kinda nice."
    player_thinking "With the end of the semester approaching, I've had a lot on my plate."
    player_thinking "The cold air is refreshing."
    player_thinking "After a couple minutes of aimless vibing, I take a look around and see a familiar figure a few feet away."
    player_thinking "I walk over to him, leaving footprints in the snow behind me."

    show badboy

    player "Hey, Dominic. What are you doing here?"
    player_thinking "I catch him a little off guard. Something seems different about him."

    dom "Oh, hey, [player_name]. Loitering, of course."
    player_thinking "He doesn't have the usual smugness about him."
    player_thinking "We stand in silence for a bit. It's more comforting than awkward."
    player_thinking "After stewing in the silence, Dominic sighs."

    dom "... you know, I wasn't always like this."
    player "What do you mean?"
    dom "I wasn't always this... fake edgy 'hooligan' type I make myself out to be."
    player_thinking "His voice's usual brightness is gone, along with the default smirk on his face."
    player_thinking "For the first time, I'm certain he's serious."
    player "Well, what were you like before?"
    player_thinking "He ponders that question for a moment, takes a short breath."
    dom "I was... a 'good kid'. I think. As good as I could be compared to my brother, at least."
    dom "Then I stopped trying because it felt pointless. All work, no play wasn't working for me."
    dom "Heh. I'm surprised I'm still in school, to be honest. I think part of me still doesn't want to disappoint my folks."
    player "Huh. I can't imagine you being that different."
    player_thinking "Suddenly, the familiar smirk returns to his face."
    dom "Can't picture me being a hard-worker, eh? I guess I have changed a lot."
    player_thinking "Snowflakes begin to gently fall onto us."
    player_thinking "Is this the real Dominic? Has he been putting on an act this whole time?"
    player_thinking "I wonder what's gotten into him..."

    if skipped_class == "true":
        dom "... you shouldn't skip class, [player_name]. Even if it's just one time, it's easy to keep doing it."
        player "Wow. You, telling me I should go to class? I'm shocked!"
        player_thinking "This whole time, I thought Dominic didn't have a care in the world. He must really care to give me advice like that."

    dom "[player_name]... do you think I did the right thing?"
    player "What do you mean?"
    dom "Becoming a delinquent...  should I have kept trying?"
    player_thinking "What should I tell him?"

    menu:
        "Do what makes you happy":
            player "I think life is too short to be perfect all the time."
            player "If trying to stack up against your brother was bringing you pain, I can see why you stopped trying."
            player "If that makes you happier, I say it was the right decision."
            player "Pleasing yourself is more important than pleasing others, right?"
            dom "Wow. That's what you think, huh?"
            dom "At least someone approves of my lifestyle..."
            player_thinking "Despite his words, he looks a little disappointed. Did I say the wrong thing?"
        "Do what's best for you":
            $ badboyPoints += 1
            player "Well... to be honest, I think you should have kept trying in school."
            player "Even if it's hard, or you feel like you're not good enough, it's for your own good."
            player "It's easy to do what makes you happy in the short-term, but harder to do what's best for the long-run."
            player "I'd love to skip class all the time and do what I want, but I know it'd only hurt me in the future."
            player "I can't tell you how to live your life, but that's the way I see it."
            dom "Hm."
            player_thinking "There's a silence. Was I too harsh?"
            play sound "audio/badboy_laugh.mp3"
            show heart with zoomin
            hide heart with dissolve
            dom "You know, only one other person has actually said that to me before."
            dom "Not even my parents told me that. There was no protest when I started getting in trouble. It was like they expected it."
            if answered_door == "false":
                player_thinking "One other person... could that be who Jane mentioned?"

    player_thinking "Dominic takes my hands in his and looks down at them pensively. My heart beats loud in my chest."
    player_thinking "He lets go and looks back up at me."
    dom "Thanks for the talk. I think I've done enough loitering today. It's pretty cold, anyway."
    player "No problem. Catch you later."

    hide badboy
    stop music

    player_thinking "That was weird... I've never seen that side of him before..."
    player_thinking "I hope he's okay."

    jump dominic_event_3

label dominic_event_3:
    play music "music/past-sadness.mp3" loop fadein 1.0
    scene outside campus snow with fade

    player_thinking "A couple weeks have passed since I spoke to Dominic in the snow."
    player_thinking "I've been thinking about the conversation we had. He showed a completely different side of him."
    player_thinking "I hadn't bumped into him anywhere on campus since then, which was odd. I normally see him hanging around somewhere."
    player_thinking "I texted him, but he hasn't replied..."
    player_thinking "I hope he's okay."

    scene dorm room with fade
    show roommate happy

    player "Hey, Jane, have you heard from Dominic recently?"
    roomie "Oh, you haven't heard?"
    player "Haven't heard what?"
    roomie "He got arrested. Tagged some buildings on campus."
    player "What?!"
    player_thinking "So that's why I haven't seen him..."
    roomie "Usually he gets left off the hook, but he actually got jailtime this time."
    player_thinking "How can she be so nonchalant about this? Has he been arrested before?"
    player "When does he get out?"
    roomie "Today, I think. I'm not sure."
    player "You're his friend and you don't know when he's getting out of jail?!"
    player "How are you so okay with this?"
    player_thinking "Jane looks a little embarrassed."
    roomie "I mean... that's just the way he is... You've noticed that by now, right?"
    player "Just because that's how he is doesn't make it right!"

    scene bedroom with fade
    player_thinking "I head to my room to think. I take out my phone and text Dominic right away."
    player_thinking "Is this really so normal for him? He must have been caught a lot for them to actually arrest him this time."
    player_thinking "I need to talk to him."

    scene outside dorms snow with fade
    player_thinking "It's the next day. Dominic texted me back and said he'd meet me by the dorms."
    player_thinking "After waiting a bit, I see him approaching in the distance."

    show badboy

    dom "What's up, [player_name]? You wanted to see my beautiful face?"
    player_thinking "There's the smug Dominic I've come to know."
    player "Hey. Are you okay?"
    dom "Never been better. Why?"
    player "Why? Jane told me you were in jail for the past two weeks!"
    dom "Oh, that? Yeah, it happens. What did you think the life of a bad boy was like?"
    player_thinking "He's put up this joking, teasing wall around himself again. Months ago, I would have played along, but this has gone too far."
    player "I need to say something to him..."

    menu:
        "Stop causing trouble":
            $ badboyPoints += 1
            player "I know your whole thing is that you do what you want and you like breaking rules, but I think it's getting out of hand."
            player "Having a criminal record isn't a minor thing, Dom. It can only get worse from here."
            player "If you get caught breaking the law again, they could lock you up for even longer..."
            player "I was worried. Jane didn't even seem concerned when she told me."
            player_thinking "The smug air around him faded. The facade, the mask he puts on, finally came off."
            player_thinking "He looked down at the ground, like a dog with its tail between its legs."
            player_thinking "Why am I scolding a grown adult? Did I overstep?"
            play sound "audio/badboy_laugh.mp3"
            show heart with zoomin
            hide heart with dissolve
            dom "You know, [player_name], you remind me a lot of this buddy I had growing up."
            dom "He was my best friend in school. I messed with him all the time because his reactions were funny."
            dom "I never told him I was having a hard time. We only had fun together. I didn't want to have it any other way."
            dom "When I started skipping school, he was the only one who cared."
            dom "Not my parents, not my brother, only him."
            dom "Y'know, Jane and them, I don't blame them for not saying anything. They accept me as I am, and I'm grateful for it."
            dom "But you... you are the only person to tell me what I'm doing is wrong. And I know it's because you care."
            player_thinking "This is the most sentimental I've seen him."
            player "Do you still talk to your friend?"
            dom "No, he's not around anymore. Hasn't been since we graduated."
            player "Oh. I'm sorry."
            dom "Nothing to be sorry about. He wouldn't want me to be sad about it."
            dom "He passed in the winter, too. That's why I get so weird this time of the year."
            dom "You know... he called me Dom, too."
            dom "Anyway, thanks for that. I needed to hear it."
            player_thinking "As he starts walking away, he stops in his tracks and turns to look at me."
            dom "[player_name]. Never change, okay?"
            player "I'll try not to."
            hide badboy
            player_thinking "He laughs at this before giving me a wink and heading on his way."
            player_thinking "Now, I can see the difference between this happiness and the usual smugness he comes to me with. This one is genuine."
        "Don't get caught next time":
            player "Look, tag buildings as much as you want, but you really need to be more careful."
            player "And why would you do it on campus? There are always people around. No wonder you got caught."
            player "If you're going to cause trouble, you shouldn't be so careless about it..."
            player_thinking "Dominic cracked a chuckle, but one that almost sounded a little sad."
            dom "I've been doing this a long time, [player_name]. I know the risks, and I can't say I really care."
            dom "It happens all the time. Trust me, it's not a big deal. 'Preciate the concern, though."
            dom "I can't imagine how hard it must have been without having me around to mess with you."
            player_thinking "I'm not sure how to respond to that. It's like he's put up a wall that I can't break through."
            player_thinking "He awkwardly looks at his feet before sighing. Is he annoyed?"
            dom "Is that all you had to say?"
            player "Um... yeah."
            dom "Aight. Well, I've got some more tagging to do, so I'm gonna go."
            dom "I won't get caught this time, though. I'll be careful."
            player_thinking "He gives me a wink and starts walking away."
            dom "See ya around."
            hide badboy
            player_thinking "Maybe I'll never understand him..."

    jump FINAL_PARTY

label PREP_START:
    # prep route
    scene dorm room with fade
    play music "music/past-sadness.mp3" loop fadein 1.0
    player_thinking "Here I am in Victoria's dorm room. I never thought she would invite me here."
    player_thinking "In fact, we've actually become friends!"
    player_thinking "She left the room for a minute to grab something… should I look around?"
    menu:
        "Snoop!":
            player_thinking "I haven't heard any footsteps, so I'm going to be a little nosy."
            player_thinking "I get up and look at the top of her dresser."
            player_thinking "It's a regular dresser just like mine, but it's cluttered with papers, books, and clothes."
            player_thinking "I notice that one of the visible papers is a quiz."
            player_thinking "It looks like there's a lot of red ink on it. I pick it up to get a closer look."
            player_thinking "Oof. Looks like she failed a quiz. I should put it back-"

            show prep with dissolve

            victoria "What are you doing?"
            player_thinking "She notices what's in my hand, and snatches it away."
            victoria "Give that back! What gives you the right to look through my stuff?!"
            victoria "What did you do, look through my dresser too?"
            player "I - I was just curious. I'm sorry. I swear I didn't look at anything else!"
            player_thinking "She sighs and sits on her bed."
            victoria "Sorry, I guess I might have overreacted. Do you want to watch a movie now?"
            player "S - sure."
            player_thinking "My face is red, and I kind of want to escape because that was embarrassing."
            player_thinking "But I sit on the bed next to her and we watch a movie together in silence."
            player_thinking "When it concludes, she gives me a short hug goodbye and I trudge back to my dorm room."
            hide prep with moveoutleft
            scene outside campus snow
            player_thinking "That could have gone better."
            stop music
            jump victoria_event_2
        "Wait for her to get back.":
            $ prepPoints += 1
            player_thinking "It's probably not a good idea, Victoria likes her privacy. I'll sit tight."
            player_thinking "After a couple minutes, she walks back in with a DVD in hand."

            show prep with dissolve
            show heart with zoomin
            hide heart with dissolve

            victoria "Okay, here! This is my favorite movie."
            player_thinking "She hands it to me and looks at me expectantly."
            victoria "So, do you want to watch it?"
            player "Sure! Pop it in. I've never seen this before."
            player_thinking "She seems almost giddy with excitement. She takes the DVD back from me and inserts it into the DVD player."
            player_thinking "She sits next to me on her bed, and the movie starts"
            player_thinking "As the movie progresses, she scoots closer and closer to me, until we are right next to each other."
            player_thinking "Then she grabs my arm and puts her head on my shoulder."
            player_thinking "This is really nice."
            hide prep
            stop music
            jump victoria_event_2


label victoria_event_2:
    # victoria's second event (debate)
    scene debate room
    play music "music/funk-game-loop.mp3" loop fadein 1.0
    if joinedDebateTeam == "false":
        player_thinking "After hanging out with Victoria, she convinced me to join the debate team."
    player_thinking "It's almost time for the debate! Victoria and I have been hanging out a couple times a week to practice for this."
    player_thinking "Well, we didn't practice every time, but sometimes. I hope it goes well."
    show prep with dissolve
    player_thinking "I'm sitting in the debate room at the front, waiting for our opponents to finish preparing. Victoria and I are ready to go."
    player_thinking "I notice Victoria's foot tapping, and I reach for her hand to give a reassuring squeeze."
    player "Hey, we've practiced a lot for this. We'll do great!"
    victoria "I know. Doesn't make me less nervous. Are you nervous at all?"
    player "I mean, yeah."
    player "But just because I'm nervous doesn't mean I'm not confident! You can be both."
    player_thinking "An announcement booms over the speakers. It's time to begin."
    player_thinking "The topic is: Should extracurricular activities be given more funding?"
    player_thinking "Our team is arguing for yes, and the other is arguing for no."
    player_thinking "I watch Victoria and a member of the other team walk up to the designated microphones."
    player_thinking "The other team starts. Each side gives their opening statements, and then the debate begins."

    hide prep

    debateStudent "College students are too busy for extracurricular activities. They should be focusing on their academics!"
    show prep with dissolve

    victoria "Isn't the point of college to also broaden your horizons and try new things? Extracurricular activities give students the opportunity to do that at little or no cost."
    victoria "Plus, extracurricular activities can offer stress relief to students, so they do better academically."
    hide prep

    player_thinking "The argument goes back and forth for 5 minutes, and then they are stopped by the moderator. "
    player_thinking "I think Victoria did a better job, but I may be biased."
    player_thinking "Victoria sits back down next to me. I stand up and make my way to the podium."
    player_thinking "We each give our opening statements, and my opponent goes first once more."

    debateStudent "College students already have an issue with sleep and mental health."
    debateStudent "Extracurriculars have enough funding as-is because students do not need to get any more involved."

    menu:
        "You're right about their mental health and sleep.":
            $ prepPoints += 1
            show heart with zoomin
            hide heart with dissolve
            player "Yes, college students are notorious for terrible sleep schedules and bad mental health states, but that's not a reason to withhold more funding for extracurriculars."
            player "Like my teammate said, extracurricular activities are stress-relievers for many college students, and more funding might get them more involved, but this would only help their mental health!"
            player_thinking "We continue debating for 5 minutes, and then we are stopped."
            player_thinking "I have a seat next to Victoria once more, and we watch the rest of the debate."
            player_thinking "Once it's over, the moderator announces our team as the winner!"
            player_thinking "We cheer and high five, and head outside to celebrate."
            player_thinking "Victoria gives me a big hug and we make plans to go to the after party that one of our teammates planned."
            stop music
            jump victoria_event_3

        "College students' mental health is just fine!":
            $ messedUpDebate = "true"
            player "College students are doing fine in the mental health department. They totally have the time and energy for more extracurriculars!"
            player_thinking "I hear the audience chuckle."
            debateStudent "That's blatantly false; everyone knows that college students are struggling. Don't make up facts to help your case."
            player_thinking "The audience cheers at this response, and I want to go hide in the corner."
            player_thinking "We finish our portion of the debate, and I sit down."
            player_thinking "Victoria does not make eye contact with me."
            player_thinking "We watch the rest of the team's debates, and the moderator announces that our team won, despite my mishap."
            scene dorm room
            player_thinking "I'm too embarrassed to talk to everyone right now, so I walk back to my dorm without saying goodbye. Maybe I can make amends at the after party tonight."
            stop music
            jump victoria_event_3

label victoria_event_3:
    # victoria's third event (after party)
    scene apartment
    play music "music/easy-lemon.mp3" loop fadein 1.0
    player_thinking "I'm standing by myself at the after party. One of our teammates is hosting it in their apartment."
    if messedUpDebate == "true":
        player_thinking "We won the debate,  no thanks to me. I hope Victoria can still look me in the eye after this."
        player_thinking "I couldn't even look myself in the eye when I was getting ready to come here."
        player_thinking "I've been keeping an eye on the front door for about 10 minutes, and Victoria finally walks in."
        player_thinking "She looks absolutely stunning, wearing a red romper with a black blazer on top."
        player_thinking "I've never seen her this dressed-up before, but this look suits her well."
        player_thinking "Her eyes meet mine and she approaches me."
        show prep with dissolve
        player_thinking "She grabs my hand."
        victoria "Come with me."
        scene balcony
        show prep with dissolve
        player_thinking "Before I can respond, she yanks my hand and we go out the back door, to the porch."
        player_thinking "No one is out here."
        player "Look, I'm sorry for messing up in the debate today. I was too embarrassed to face you, so that's why I left without celebrating with you guys."
        victoria "I'm not mad at you. I wasn't happy with you at first."
        victoria "I got plenty of secondhand embarrassment from you, sure, but I can't act like I've never messed up at the podium before."
        victoria "Plus, it was your first real debate! I think you did decent, considering that."
        player "Th-thank you. Thank you for being so understanding."
        player_thinking "Victoria being apologetic is a rare thing, I've noticed."
        player_thinking "So, this is cool."
        player_thinking "She takes my hands and pulls me in for a hug."
        player_thinking "Or is it something else…?"
        player_thinking "Should I go for a kiss?"
        menu:
            "Kiss her!":
                player_thinking "I'm going in for a kiss!"
                player_thinking "Our lips meet, and I realize that she was also going in for a kiss!"
                player_thinking "It's a nice, short kiss, and Victoria pulls away first."
                victoria "Oh, I totally forgot! I have to introduce you to my friend from my public policy class! Follow me!"
                hide prep
                scene apartment
                player_thinking "And so, for the rest of the party, I am dragged around by Victoria as she excitedly introduces me to her friends outside of the debate team."
                player_thinking "The night ends, and we go our separate ways."
                player_thinking "We haven't made anything official, but I hope we will soon."
                stop music
                jump FINAL_PARTY
            "Hug her!":
                player_thinking "Let's go for a hug."
                player_thinking "I go to give her a regular old hug, and Victoria tries to kiss me."
                player_thinking "I jump back a little bit."
                victoria "Oh crap! I'm sorry, I didn't mean to do that… I thought you might feel that way about me. I'm so sorry!"
                player "It's fine, don't worry about it! I like you, I just didn't know you wanted to kiss me!"
                victoria "Oh, you're just saying that to make me feel better. I'm serious, I'm so sorry! I'll go inside now."
                hide prep with moveoutright
                scene apartment
                player_thinking "She opens the door and hurries back inside, her face a bright red."
                player_thinking "She spends the rest of the party avoiding me, probably too embarrassed to face me."
                player_thinking "I do like her, I just wasn't prepared for that yet."
                player_thinking "I hope we can still work it out."
                stop music
                jump FINAL_PARTY

    else:
        player_thinking "We won the debate, thanks to Victoria and I."
        player_thinking "I've been keeping an eye on the front door for about 10 minutes, and Victoria finally walks in."
        player_thinking "She looks absolutely stunning, wearing a red romper with a black blazer on top."
        player_thinking "I've never seen her this dressed-up before, but this look suits her well."
        player_thinking "Her eyes meet mine and she approaches me."
        show prep with dissolve
        player_thinking "She grabs my hand."
        victoria "Come with me."
        player_thinking "Before I can respond, she yanks my hand and we go out the back door, to the porch."
        scene balcony
        show prep with dissolve
        player_thinking "No one is out here."
        player "What's up?"
        victoria "I just wanted to tell you that you did so well in the debate today!"
        victoria "I didn't know how well you were going to do, to be honest."
        victoria "Especially since it was your first real debate."
        victoria "But you did nearly as well as me! Good for you!"
        player_thinking "I giggle."
        player "Almost as well as you, huh? I guess I'll take that as a compliment. Thanks."
        player "And you did amazingly, by the way. You would make a great lawyer."
        play sound "audio/prep_thankYou.mp3"
        victoria "Thank you."
        player_thinking "We stand in silence for a minute or two and look at the stars. It's chilly, but beautiful outside tonight."
        player_thinking "I look over at Victoria and catch her staring at me."
        player_thinking "She smiles and takes my hands. She then starts pulling me into a hug."
        player_thinking "Or is it something else…?"
        player_thinking "Should I go for a kiss?"
        menu:
            "Kiss her!":
                $ prepPoints += 1

                player_thinking "I'm going in for a kiss!"
                show heart with zoomin
                hide heart with dissolve
                player_thinking "Our lips meet, and I realize that she was also going in for a kiss!"
                player_thinking "It's a nice, short kiss, and Victoria pulls away first."
                victoria "Oh, I totally forgot! I have to introduce you to my friend from my public policy class! Follow me!"
                hide prep
                scene apartment
                player_thinking "And so, for the rest of the party, I am dragged around by Victoria as she excitedly introduces me to her friends outside of the debate team."
                player_thinking "The night ends, and we go our separate ways."
                player_thinking "We haven't made anything official, but I hope we will soon."
                stop music
                jump FINAL_PARTY
            "Hug her!":
                player_thinking "Let's go for a hug."
                player_thinking "I go to give her a regular old hug, and Victoria tries to kiss me."
                player_thinking "I jump back a little bit."
                victoria "Oh crap! I'm sorry, I didn't mean to do that… I thought you might feel that way about me. I'm so sorry!"
                player "It's fine, don't worry about it! I like you, I just didn't know you wanted to kiss me!"
                victoria "Oh, you're just saying that to make me feel better. I'm serious, I'm so sorry! I'll go inside now."
                hide prep with moveoutright
                scene apartment
                player_thinking "She opens the door and hurries back inside, her face a bright red."
                player_thinking "She spends the rest of the party avoiding me, probably too embarrassed to face me."
                player_thinking "I do like her, I just wasn't prepared for that yet."
                player_thinking "I hope we can still work it out."
                stop music
                jump FINAL_PARTY

#####################################################################
#
#  ARTIST ROUTE START (Andrea)
#
#####################################################################

label ARTIST_START:
    scene black
    "You seem to have taken a fondness to August. It's been a few days since you last saw them."
    play music "music/windswept.mp3" loop fadein 1.0
    scene dorm room with fade
    "Just when you think you are starting to miss them, they ask you if they can come over."
    show artist with dissolve

    august "Thank you for letting me coming over, [player_name]. I know it was a little bit last minute, but I haven't seen you in a while."
    player "Not a problem at all! I was honestly really glad you called."
    august "You were?"
    player "Yeah... I kinda missed you. So, do you have anything in mind that you want to do?" 
    august "Yeah! I was kinda hoping we could just go on a walk and talk for a little bit."
    player "Absolutely, let me get my shoes."

    ####### Scene 1
    scene autumn trees with fade
    show artist with dissolve 
    player "So, what did you want to talk about?"
    august "Well, we've been spending some time together lately..."
    player "Yes?"
    august "But I've kind of been hoping to get to spend more time with you."
    menu:
        "I would like that": 
            play sound "audio/artist_laugh.mp3"
            august "I really like you [player_name]!"
        "I don't know about that...":
            august "Oh? do you not want to?"
            player "That's not what I said. I just need to think about it, yeah?"
            august "Absolutely, take all the time you need." 
    player "Is there anything else you had in mind?"
    august "I don't know, there are always a lot of things on my mind."
    player "Like what?"
    august "Like the way the trees move look like they're waving us goodbye, like we're going on a long journey, or they are. Especially when they're losing leaves like this."
    menu: 
        "Ugh, August, why do you say such weird things?":
            $ assholeToAugust = "true"
            august "Oh. Sorry, I didn't mean to say something weird." 
            player "Well, you did. But it's okay, I still like you."
            "August smiles, but they look confused."
        "Who do you think is going on a journey?":
            player "The leaves or us?"
            august "Could be both, could be neither. I guess we'll just have to find out."
    august "But that's what I'm thinking about. I really like the ambiance of fall. It makes me want to sit and watch the leaves, maybe sketch or write."
    menu: 
        "Why don't we do that?":
            august "Actually, yeah, why not?"
            player "Yeah! Why not! We can find a tree to be creative under."
            play sound "audio/artist_laugh.mp3"
            august "absolutely"
            "August sits down on the floor and pulls out a sketchpad."
            august "Tell me about yourself."
            "They watch you as they passively sketch something out in their artist pad. They seem to be having a lot of fun doing so."
            show heart with zoomin
            hide heart with dissolve
            $ artistPoints += 1
        "Not right now. I know you need to practice, your art obviously needs work. But I'll get so bored...":
            player "I mean, I'm right here in front of you, aren't I important?"
            august "Wait, you don't like my art?"
            player "I mean, it's amazing for your audience, I'm guess. Just not my preference."
            august "Oh? Uh. Okay... we can do something else."
            player "Yeah! I really like you, I'm so excited to spend time with you."
            august "You are? Yeah, okay, sure! ...Let's do something together."
            "You both end up going back to your apartment and watching a show you pick out."
            $ assholeToAugust = "true"

    ####### Scene 2
    scene black with fade
    "You've been texting more with August recently and you're starting to get to know them better. They seem to really like you."
    if assholeToAugust == "true":
        "Even if they get a little skittish around you."
    "So a couple of days later, they invite you to their favorite coffee shop."
    scene coffee shop with fade
    show artist at right with dissolve
    august "I'm glad you're here. What do you want to drink? I'll get it for you."
    menu:
        "What do you recommend?":
            august "I love their lattes! They have some really cool and unique flavors... do you want me to pick something for you?"
            player "I've never been here, I bet you have the best recommendations! I like drinks that are more balanced between sweet and coffee."
            august "I know exactly what to get!"
        "How about I'll treat you this time? What do you want?":
            august "Oh! You don't have to do that... that's so sweet."
            player "I want to! You can buy next time."
            play sound "audio/artist_laugh.mp3"
            august "Alright, alright! I think I want a toffee latte."
            player "Coming right up, cutie!"
            "You see august blush."
        "Nothing here really looks good...":
            august "Ah, just try it out? Please? It's one of my favorite shops."
            player "Alright, I guess I can give it a try. Just cause you're cute."
            "August seems flustered."
            august "Are you craving anything special?"
            player "Just get me whatever, but come back soon."
    
    "A few moments later you both sit with coffees in hand. August is fidgeting with his cup."
    menu:
        "Is everything okay?":
            august "Yeah! Yeah, everything is alright."
            player "It doesn't seem alright..."
            august "No, it is! It is, I promise... I just really like being around you."
            player "I like being around you too."
            august "No, like-- A lot. I want to be around you more often."
            player "....I want to be around you more often too."
            player "Do you want to go out on a date?"
        "C'mon, why aren't you happy? We came here for you.":
            august "Sorry, sorry. You just make me nervous. But in a good way! I think..."
            player "Well, that's good. Because I really like you."
            august "You do? Sometimes I wonder... cause I get nervous, that you only hang out with me cause you feel sorry for me."
            player "Don't be silly!"
            player "We should go on a date."
            $ assholeToAugust = "true"
    player "like a proper date."
    august "I think I would like that..."
    player "... Does this, right now, feel a little bit like a date to you?"
    august "It does... would you want it to be? A date? Are you serious about it? Do you like me... in that way." 

    if assholeToAugust == "true":
        player "I'm falling in love with you."
        august "You are??"
        player "I am."
        august "We've only known each other for a short time."
        player "Does that matter? You are... something else. There's just something about you that I can't ignore." 
    else:
        player "I do. I really do."
        show heart at right with zoomin
        hide heart at right with dissolve
        $ artistPoints += 1
    "August doesn't say anything else about it, but you both talk comfortably for a while after that. Neither of you wants to get up and leave that moment."
    if assholeToAugust == "true":
        "You're going to have so much fun with them."
    else:
        "Something wonderful seems to be starting."

    ####### Scene 3
    scene black with fade
    "A couple of weeks later, you and August are spending more and more time together."
    
    if assholeToAugust == "true":
        "You take them out on a stroll around campus in the snow."
        jump freezing_walk
    else:
        "They finally decide to show you their secret project."
        jump secret_project
    
label freezing_walk:
    scene outside dorms snow with fade
    show artist with dissolve
    august "Thank you for bringing me here, [player_name]"
    player "Anything for my sweet heart."
    august "You're being so kind to me..."
    player "I'm always kind to you."
    "August starts chewing his lips nervously, a habit you noticed a couple of weeks ago."
    player "What's making you nervous, August?"
    august "I just never know how you're going to respond."
    player "What do you mean?"
    august "Sometimes you treat me like I mean the world to you, and sometimes..."
    player "I know I have a bit of a temper."
    august "It's more than that. You're really unpredictable."
    player "Isn't that a good thing?"
    august "I suppose..."
    player "I love you."
    "You've been saying it to each other openly since that day at the coffee shop."
    player "I love you more than anyone has ever loved you, and more than anyone ever will."
    "August looks like they want to cry. Out of joy or sadness, neither of you can tell."
    jump FINAL_PARTY

label secret_project:
    august "I've been building this for... probably over a year now."
    "You've been following them through the forest for a bit now, going deeper into the thicket."
    player "Building? Is that why your hands are calloused?"
    august "Ah! Yeah, actually. I'm surprised you noticed that!"
    scene cabin with fade
    show artist at right with dissolve 
    august "What do you think?"
    player "August! This is so cool! I didn't even know you could build!"
    august "I know it's really childish, I just never got a treehouse as a kid, and I was really excited to make a little creative space for myself."
    player "I'm amazed! You're so talented! How did you manage this! Where even are we?"
    august "It's a little forest in the property of a distant family member. They don't come by a lot, but they let me built this here."
    player "It reminds me of a tiny little cottage."
    august "Yes! That's exactly what I wanted. I've always had this escapist dream of running away to a cottage in the woods."
    player "Sometimes you have to make those dreams a reality, right? That's what you've been doing."
    august "Just... trying to make a little space that makes me happy."
    player "And you wanted to share it with me?"
    august "I did... because you make me happy."
    show heart at right with zoomin
    hide heart at right with dissolve
    "You spend the rest of the day together creating art together in the tiny cabin. August looks so happy."
    jump FINAL_PARTY
    


    
    







# Tsundere Start

label TSUNDERE_START:
    # tsundere route
    #"TSUNDERE ROUTE START"

    #first event
    play music "music/white.mp3" loop fadein 1.0
    scene outside campus 2  #is this the scene for campus

    show finley

    player_thinking "I think that's Finley over there."

    finley "Hey [player_name], do you want to go thrift shopping with me? Not that I want to hangout. I just need someone to help me carry bags."

    menu:
        "Sure, I would love to go thrift shopping!":
            $ tsunPoints += 1
            play sound "audio/tsundere.mp3"
            show heart with zoomin
            hide heart with dissolve
            finley "Cool. Let's head over there now."

            scene thrift_shop

            show finley

            player "So Finley, why do you love thrift shopping?"

            finley "Well, I am the youngest of 8 kids so I always got my siblings' hand-me-downs."

            finley "After a while I grew to love mismatched mess so now I go thrift shopping to see what weird and wonderful things I might find."

            player_thinking "Finley reaches over to a shirt on the rack."

            finley "This would look really good on you. You should go try it on."

            player_thinking "I take the shirt from Finley and go put it on. I come out to see Finley try to cover their blush."

            finley "That really does look good on you."

            player_thinking "We spent the rest of the afternoon shopping together."

            finley "I had fun. Maybe you're not so bad to hangout with."

            player_thinking "I can see the smirk and blush on Finley's face. They had more fun than they are saying."

        "No thanks. I have other things I need to get done.":
            finley "That's fine or whatever."

            player_thinking "I can see the sad look on their face as they walk away."

    hide finley

    #second event

    scene outside campus 2  #should be the campus

    show finley

    player_thinking "Finley is over there."

    finley "Hey [player_name], do you want to come over to my dorm to watch some movies?"

    player_thinking "If Finley had a tail it would be wagging right now."

    player "Sure, sounds like fun!"

    finley "Awesome. See you tonight. Not that I really wanted you to say yes."

    scene dorm room

    player_thinking "I should knock on Finley's door."

    show finley

    finley "Hey [player_name], I am just finishing up with the popcorn if you want to go pick a movie."

    menu:
        "Choose the bad movie":
            $ tsunPoints += 1
            play sound "audio/tsundere.mp3"
            show heart with zoomin
            hide heart with dissolve
            finley "That movie is so bad it's amazing. Good choice!"
            player_thinking "Finley's face lit up like a christmas tree when I chose this movie. Finley picks up the movie to put it in the DVD player."
        "Choose the good movie":
            finley "That's a cool choice."
            player_thinking "Is Finley sad that I didn't choose the bad movie?"

    player_thinking "We spent the night watching movies together."

    hide finley

    scene outside campus 2 #should be the college campus

    finley "Is that Finley walking over to me?"

    show finley

    finley "Hey [player_name], I was wondering if you want to come over and cook with me tonight?"

    menu:
        "No thanks, I want to chill in my dorm.":
            finley "Well whatever so you later."

            player_thinking "Finley seems really sad that I said no."

        "Sure, cooking with you sounds like a lot of fun!":
            $ tsunPoints += 1
            play sound "audio/tsundere.mp3"
            show heart with zoomin
            hide heart with dissolve

            finley "Well, see you tonight!"

            player_thinking "Did Finley ask me to hangout without hiding their feelings, or their blush?"

            player_thinking "Must have been my imagination."

            scene dorm room

            player_thinking "Here I am at Finley's dorm... I am going to knock."

            show finley

            finley "Hey, come on in. I was just setting everything up. We are making grilled cheese."

            player "Do you like to cook?"

            finley "When I was young my mom taught me how to cook. She would make me grilled cheese every time I was sick. So now when I am homesick I use her grilled cheese recipe."

            player_thinking "Finley helped me cook some delicious looking grilled cheese we sat down to dig into them."

            finley "[player_name], thanks for hanging out me I really like your company."

            player_thinking "Finley just told me they like to hangout with me with no mean comment. They are even blushing with the softest smile. I can't believe what is happening!"

            player "Thank you for inviting me Finley. I like hanging out with you too."

    hide finley

    scene dorm room

    stop music

    jump FINAL_PARTY

label FINAL_PARTY:
    # new year's party event

    # I'm at the New Year's Party... who should I ask to dance with? (or something)
    # - pick one of the four characters
    # - need at least 6 points with the chosen character to get their "good ending" (a picture of the character with them)
    # OTHERWISE bad ending picture / MC dances alone :(

    scene final party

    player_thinking "I'm at the New Year's party. Everything's nicely decorated, everyone's dressed their best..."

    player_thinking "Who should I ask to dance with?"

    menu:
        "Dominic":
            if(badboyPoints >= 6):
                player_thinking "I asked Dominic to dance with me. He said yes!"
                if(portrait_number == 1):
                    show dominic portrait 1
                    player_thinking "The End"
                elif(portrait_number == 2):
                    show dominic portrait 2
                    player_thinking "The End"
                elif(portrait_number == 3):
                    show dominic portrait 3
                    player_thinking "The End"
                elif(portrait_number == 4):
                    show dominic portrait 4
                    player_thinking "The End"
            else:
                player_thinking "I asked Dominic to dance with me. He called me a loser and walked away."
                jump BAD_END

        "Victoria":
            if(prepPoints >= 6):
                player_thinking "I asked Victoria to dance with me. She said yes!"
                if(portrait_number == 1):
                    show victoria portrait 1
                    player_thinking "The End"
                elif(portrait_number == 2):
                    show victoria portrait 2
                    player_thinking "The End"
                elif(portrait_number == 3):
                    show victoria portrait 3
                    player_thinking "The End"
                elif(portrait_number == 4):
                    show victoria portrait 4
                    player_thinking "The End"
            else:
                player_thinking "I asked Victoria to dance with me. She glared at me like I was a peasant before vacating the premises."
                jump BAD_END

        "August":
            if(artistPoints >= 6):
                player_thinking "I asked August to dance with me. They said yes!"
                if(portrait_number == 1):
                    show august portrait 1
                    player_thinking "The End"
                elif(portrait_number == 2):
                    show august portrait 2
                    player_thinking "The End"
                elif(portrait_number == 3):
                    show august portrait 3
                    player_thinking "The End"
                elif(portrait_number == 4):
                    show august portrait 4
                    player_thinking "The End"
            else:
                player_thinking "I wanted to ask August, but I can't find them anywhere... maybe they didn't show up?"
                jump BAD_END

        "Finley":
            if(tsunPoints >= 6):
                player_thinking "I asked Finley to dance with me. They said yes!"
                if(portrait_number == 1):
                    show finley portrait 1
                    player_thinking "The End"
                elif(portrait_number == 2):
                    show finley portrait 2
                    player_thinking "The End"
                elif(portrait_number == 3):
                    show finley portrait 3
                    player_thinking "The End"
                elif(portrait_number == 4):
                    show finley portrait 4
                    player_thinking "The End"
            else:
                player_thinking "I asked Finley to dance with me. They asked why they would want to dance with *me* before walking off."
                jump BAD_END
    return

label BAD_END:
    # general bad ending
    player_thinking "I guess I'm dancing on my own..."
    scene bad ending
    player_thinking "END"
    return